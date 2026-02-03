import os
import json
import time
from typing import Dict, List, Optional, Union, Type
from openai import AsyncOpenAI
from loguru import logger
import tiktoken
from tenacity import retry, stop_after_attempt, wait_exponential

from app.models.chat import ChatMessage, UserContext, UserRole
from app.models.ai_responses import (
    StructuredAIResponse, QuickAnswer, ComplianceAnalysis, TechnicalGuidance, 
    ErrorResponse, KnowledgeSource, ActionItem, ComplianceCheck, FollowUpSuggestion,
    ResponseType, ConfidenceLevel, ComplexityLevel, RegulationType
)
from app.services.knowledge_base import KnowledgeBase

class EnhancedOpenAIService:
    """
    Enhanced OpenAI service met structured outputs en knowledge base integratie
    """
    
    def __init__(self):
        api_key = os.getenv("GREENPT_API_KEY")
        demo_mode = os.getenv("DEMO_MODE", "false").lower() == "true"
        
        if not api_key or api_key == "your_greenpt_api_key_here":
            if not demo_mode:
                raise ValueError("GREENPT_API_KEY environment variable is required. Set DEMO_MODE=true voor demo functionaliteit.")
            else:
                logger.info("Running in DEMO MODE - using mock responses")
                api_key = "demo-key-for-demo-mode"  # Dummy key voor demo
        
        self.client = AsyncOpenAI(api_key=api_key)
        self.demo_mode = demo_mode
        self.model = os.getenv("GREENPT_MODEL", "gpt-4o-2024-08-06")  # Updated voor structured outputs
        self.max_tokens = int(os.getenv("GREENPT_MAX_TOKENS", "2000"))
        self.temperature = float(os.getenv("GREENPT_TEMPERATURE", "0.3"))  # Lower voor consistentie
        
        # Initialize tokenizer
        try:
            self.encoding = tiktoken.encoding_for_model("gpt-4")
        except:
            self.encoding = tiktoken.get_encoding("cl100k_base")
        
        # Initialize knowledge base
        self.knowledge_base = KnowledgeBase()
        
        logger.info(f"Enhanced OpenAI service initialized with model: {self.model}")
        logger.info(f"Knowledge base statistics: {self.knowledge_base.get_statistics()}")

    def _determine_response_type(self, message: str, context: UserContext) -> Type:
        """Bepaal welk response type het beste past bij de vraag"""
        message_lower = message.lower()
        
        # Check voor compliance gerelateerde termen (ook gerelateerde concepten)
        compliance_terms = ['gdpr', 'ai act', 'woo', 'compliance', 'regelgeving', 'wet', 'dpia', 
                           'privacy', 'gegevensbescherming', 'avg', 'archiefwet', 'transparantie',
                           'rechtmatige grondslag', 'bewaartermijn', 'toestemming']
        
        if any(term in message_lower for term in compliance_terms):
            return ComplianceAnalysis
        
        # Check voor technische termen
        technical_terms = ['architectuur', 'implementeer', 'api', 'technical', 'code', 'systeem',
                          'database', 'server', 'cloud', 'security', 'integratie', 'deployment',
                          'microservices', 'container', 'kubernetes', 'docker']
        
        if any(term in message_lower for term in technical_terms):
            return TechnicalGuidance
        
        # Voor zeer korte vragen (minder dan 5 woorden) -> QuickAnswer
        if len(message.split()) < 5 and '?' in message and not any(term in message_lower for term in compliance_terms + technical_terms):
            return QuickAnswer
            
        # Default naar structured response voor uitgebreide antwoorden
        return StructuredAIResponse

    def _build_context_prompt(self, context: UserContext, relevant_docs: List[Dict]) -> str:
        """Build enhanced context prompt met knowledge base informatie"""
        
        base_prompt = f"""Je bent een AI assistant voor Nederlandse gemeentes, gespecialiseerd in digitale transformatie en AI implementatie.

GEBRUIKER CONTEXT:
- Rol: {context.roleName or context.role}
- Projectfase: {context.projectPhase or 'Niet gespecificeerd'}
- Focusgebieden: {', '.join([area.value for area in context.focusAreas]) if context.focusAreas else 'Algemeen'}
- Specifieke context: {context.customContext or 'Geen extra context'}

RELEVANTE KENNISBANK INFORMATIE:
"""
        
        # Voeg relevante documenten toe
        for i, doc in enumerate(relevant_docs[:3], 1):  # Max 3 docs voor context
            base_prompt += f"""
{i}. {doc['title']} ({doc['type']})
   {doc['summary']}
   Relevantie: {doc['score']}
"""
        
        base_prompt += """

INSTRUCTIES:
1. Gebruik de kennisbank informatie om accurate, brongestuurde antwoorden te geven
2. Wees specifiek over regelgeving en compliance requirements
3. Geef praktische, uitvoerbare adviezen
4. Verwijs naar menselijke experts voor complexe juridische interpretaties
5. Houd altijd rekening met de Nederlandse overheidscontext
6. Wees transparant over beperkingen van je kennis

RESPONSE FORMAT:
Geef een duidelijke hoofdrespons die de vraag volledig beantwoordt.
Voeg GEEN bronverwijzingen, vervolgvragen of escalatie-informatie toe - deze worden automatisch toegevoegd door het systeem.
"""
        
        return base_prompt

    def _extract_knowledge_sources(self, relevant_docs: List[Dict]) -> List[KnowledgeSource]:
        """Convert relevante documenten naar KnowledgeSource objecten"""
        sources = []
        
        for doc in relevant_docs:
            source = KnowledgeSource(
                title=doc['title'],
                url=doc.get('url', f"#{doc['document_id']}"),
                snippet=doc.get('content_snippet', doc['summary']),
                relevance_score=min(doc['score'] / 10.0, 1.0),  # Normalize score
                document_type=self._map_doc_type_to_enum(doc['type'])
            )
            sources.append(source)
            
        return sources

    def _map_doc_type_to_enum(self, doc_type: str) -> str:
        """Map document types naar enum values"""
        mapping = {
            'privacy_law': 'law',
            'ai_regulation': 'law', 
            'transparency_law': 'law',
            'technical_standard': 'guideline',
            'municipal_guidance': 'best_practice',
            'official_guidance': 'guideline'
        }
        return mapping.get(doc_type, 'guideline')

    def _assess_complexity_and_confidence(self, message: str, context: UserContext, relevant_docs: List[Dict]) -> tuple:
        """Assess complexity level en confidence gebaseerd op verschillende factoren"""
        
        complexity_indicators = {
            'expert_required': ['juridisch advies', 'contract', 'aanbesteding', 'rechtszaak', 'boete'],
            'complex': ['implementatie strategie', 'architectuur design', 'compliance framework'],
            'moderate': ['best practices', 'richtlijnen', 'standaarden'],
            'simple': ['wat is', 'hoe werkt', 'definitie', 'uitleg']
        }
        
        message_lower = message.lower()
        complexity = ComplexityLevel.MODERATE  # Default
        
        for level, indicators in complexity_indicators.items():
            if any(indicator in message_lower for indicator in indicators):
                complexity = ComplexityLevel(level)
                break
        
        # Confidence gebaseerd op knowledge base matches
        confidence = ConfidenceLevel.MEDIUM  # Default
        if relevant_docs:
            avg_score = sum(doc['score'] for doc in relevant_docs) / len(relevant_docs)
            if avg_score > 7:
                confidence = ConfidenceLevel.HIGH
            elif avg_score < 3:
                confidence = ConfidenceLevel.LOW
        
        return complexity, confidence

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    async def generate_structured_response(self, chat_message: ChatMessage, force_response_type: Type = None) -> Union[StructuredAIResponse, QuickAnswer, ComplianceAnalysis, TechnicalGuidance, ErrorResponse]:
        """Generate structured AI response met knowledge base integratie"""
        
        start_time = time.time()
        
        try:
            # Search knowledge base voor relevante documenten
            relevant_docs = self.knowledge_base.search_documents(
                chat_message.message,
                max_results=5
            )
            
            # Voeg role-specific documenten toe
            role_docs = self.knowledge_base.get_role_specific_documents(
                chat_message.context.role.value if chat_message.context.role else 'other'
            )
            
            # Combine en deduplicate
            all_docs = {doc['document_id']: doc for doc in relevant_docs + role_docs[:3]}
            final_docs = list(all_docs.values())[:5]
            
            # Always use StructuredAIResponse
            response_type_class = StructuredAIResponse
            
            # Build context prompt
            system_prompt = self._build_context_prompt(chat_message.context, final_docs)
            
            # Assess complexity en confidence
            complexity, confidence = self._assess_complexity_and_confidence(
                chat_message.message, chat_message.context, final_docs
            )
            
            # Check token limits
            prompt_tokens = self._count_tokens(system_prompt + chat_message.message)
            if prompt_tokens > 6000:  # Leave room for response
                logger.warning("Token limit approached, truncating context")
                system_prompt = system_prompt[:4000]
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": chat_message.message}
            ]
            
            # Voor demo doeleinden: gebruik mock structured response
            # In productie: gebruik echte OpenAI structured outputs API
            use_demo_mode = os.getenv("DEMO_MODE", "false").lower() == "true"
            
            if use_demo_mode or os.getenv("GREENPT_API_KEY", "").startswith("demo"):
                # Demo structured response
                logger.info("Using demo structured response")
                structured_response = self._create_demo_structured_response(
                    chat_message.message, response_type_class, final_docs, complexity, confidence
                )
            else:
                try:
                    # Real OpenAI completion (niet structured outputs voor nu)
                    logger.info(f"Using real OpenAI API with {response_type_class.__name__}")
                    
                    # Enhanced system prompt voor structured response
                    enhanced_prompt = system_prompt + f"""

VERY IMPORTANT: Je MOET een {response_type_class.__name__} response geven. 

Antwoord altijd in het Nederlands en geef concrete, actionable informatie.
Focus op gemeente-specifieke context en Nederlandse regelgeving.

BELANGRIJK: Voeg GEEN bronverwijzingen, vervolgvragen of escalatie-secties toe aan je antwoord.
Deze worden automatisch door het systeem toegevoegd.

Voor ComplianceAnalysis: Focus op GDPR, AI Act, Woo, en andere relevante wetgeving
Voor TechnicalGuidance: Focus op Common Ground, open standaarden, en overheids-architectuur
Voor StructuredAIResponse: Geef uitgebreide, gestructureerde antwoorden met concrete actiepunten
"""
                    
                    completion = await self.client.chat.completions.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": enhanced_prompt},
                            {"role": "user", "content": chat_message.message}
                        ],
                        max_tokens=self.max_tokens,
                        temperature=self.temperature
                    )
                    
                    response_text = completion.choices[0].message.content
                    
                    # Voor nu: converteer text response naar structured format
                    structured_response = self._convert_text_to_structured(
                        response_text, response_type_class, final_docs, complexity, confidence
                    )
                    
                except Exception as e:
                    logger.warning(f"OpenAI API failed: {e}")
                    # Fallback to demo response
                    structured_response = self._create_demo_structured_response(
                        chat_message.message, response_type_class, final_docs, complexity, confidence
                    )
            
            # Post-process response met additional metadata
            if isinstance(structured_response, StructuredAIResponse):
                # Add knowledge sources
                structured_response.knowledge_sources = self._extract_knowledge_sources(final_docs)
                
                # Add processing metadata
                structured_response.processing_time_ms = int((time.time() - start_time) * 1000)
                structured_response.token_usage = completion.usage.total_tokens if completion.usage else None
                
                # Set confidence en complexity
                structured_response.confidence_level = confidence
                structured_response.complexity = complexity
                
                # Generate follow-up suggestions
                structured_response.follow_up_suggestions = self._generate_follow_up_suggestions(
                    chat_message.context, chat_message.message
                )
            
            logger.info(f"Generated {type(structured_response).__name__} in {time.time() - start_time:.2f}s")
            return structured_response
            
        except Exception as e:
            logger.error(f"Error in structured response generation: {e}")
            return ErrorResponse(
                error_type="api_error",
                error_message="Er ging iets mis bij het genereren van het antwoord. Probeer het opnieuw.",
                technical_details=str(e),
                suggested_action="Probeer je vraag opnieuw te stellen of neem contact op met een expert.",
                needs_human_help=True
            )

    def _generate_follow_up_suggestions(self, context: UserContext, message: str) -> List[FollowUpSuggestion]:
        """Generate contextuele follow-up suggestions"""
        
        base_suggestions = {
            UserRole.DIGITAL_GUIDE: [
                ("Hoe zorg ik voor draagvlak bij stakeholders voor dit project?", "process", 0.9),
                ("Welke risico's moet ik monitoren tijdens de implementatie?", "process", 0.8),
                ("Wie zijn de belangrijkste stakeholders om te betrekken?", "process", 0.8)
            ],
            UserRole.CIVIL_SERVANT: [
                ("Welke andere regelgeving is relevant voor mijn situatie?", "legal", 0.9),
                ("Hoe documenteer ik compliance voor audits?", "legal", 0.8),
                ("Wat zijn de sancties bij non-compliance?", "legal", 0.7)
            ],
            UserRole.IT_MANAGER: [
                ("Welke technische standaarden moet ik volgen?", "technical", 0.9),
                ("Hoe zorg ik voor schaalbaarheid van dit systeem?", "technical", 0.8),
                ("Wat zijn de security best practices?", "technical", 0.8)
            ],
            UserRole.PROJECT_MANAGER: [
                ("Hoe plan ik de volgende fase van dit project?", "process", 0.9),
                ("Welke resources heb ik nodig voor implementatie?", "process", 0.8),
                ("Hoe meet ik het succes van dit project?", "process", 0.7)
            ],
            UserRole.DEVELOPER: [
                ("Waar vind ik documentatie voor deze APIs?", "technical", 0.9),
                ("Welke testing strategie moet ik hanteren?", "technical", 0.8),
                ("Hoe zorg ik voor code kwaliteit?", "technical", 0.7)
            ]
        }
        
        role = context.role or UserRole.OTHER
        suggestions_data = base_suggestions.get(role, [
            ("Waar kan ik meer informatie vinden over dit onderwerp?", "general", 0.7),
            ("Wie kan me verder helpen met specifieke vragen?", "general", 0.6)
        ])
        
        # Map categories to valid enum values
        category_mapping = {
            'general': 'process',
            'proces': 'process',
            'techniek': 'technical',
            'juridisch': 'legal',
            'beleid': 'policy'
        }
        
        valid_suggestions = []
        for q, cat, rel in suggestions_data[:3]:
            valid_cat = category_mapping.get(cat, cat)
            if valid_cat in ['technical', 'legal', 'process', 'policy']:
                valid_suggestions.append(FollowUpSuggestion(question=q, category=valid_cat, relevance=rel))
        
        return valid_suggestions

    def _extract_action_items(self, response_text: str) -> List[ActionItem]:
        """Extract action items from response text"""
        # Simple heuristic - look for numbered lists or action words
        action_items = []
        
        # Look for common action patterns
        if any(word in response_text.lower() for word in ['implementeer', 'opstel', 'voer uit', 'controleer', 'raadpleeg']):
            action_items.append(ActionItem(
                title="Review implementatie",
                description="Bekijk de voorgestelde stappen en implementeer waar nodig",
                priority="medium",
                timeline="1-2 weken"
            ))
        
        if any(word in response_text.lower() for word in ['gdpr', 'privacy', 'compliance', 'dpia']):
            action_items.append(ActionItem(
                title="Compliance check",
                description="Voer compliance verificatie uit voor de voorgestelde oplossing",
                priority="high",
                timeline="Voor implementatie"
            ))
        
        return action_items

    def _identify_regulations(self, response_text: str) -> List[str]:
        """Identify relevant regulations mentioned in response"""
        regulations = []
        text_lower = response_text.lower()
        
        if any(term in text_lower for term in ['gdpr', 'avg', 'privacy']):
            regulations.append('GDPR/AVG')
        if any(term in text_lower for term in ['ai act', 'kunstmatige intelligentie']):
            regulations.append('AI Act')
        if any(term in text_lower for term in ['woo', 'openbaarheid']):
            regulations.append('Woo')
        if any(term in text_lower for term in ['common ground', 'architectuur']):
            regulations.append('Common Ground')
        
        return regulations

    def _convert_text_to_structured(self, response_text: str, response_type_class: Type, docs: List[Dict], complexity: ComplexityLevel, confidence: ConfidenceLevel):
        """Convert text response to structured format"""
        
        # Always return StructuredAIResponse
        return StructuredAIResponse(
            main_answer=response_text,
            response_type=AIResponseFormat.STRUCTURED,
            confidence_level=confidence,
            complexity=complexity,
            knowledge_sources=self._extract_knowledge_sources(docs),
            action_items=self._extract_action_items(response_text),
            follow_up_suggestions=[],  # Will be filled later
            needs_human_expert=complexity == "high" or confidence == "low",
            relevant_regulations=self._identify_regulations(response_text),
            processing_time_ms=0  # Will be set later
        )
        
        # Old complex logic - keeping for reference but not used
        if False and response_type_class == ComplianceAnalysis:
            # Determine regulation type from response content
            regulation_type = RegulationType.AI_ACT if 'ai act' in response_text.lower() else RegulationType.GDPR
            
            return ComplianceAnalysis(
                regulation_type=regulation_type,
                compliance_status="needs_assessment",
                requirements=[
                    "Data Protection Impact Assessment (DPIA) uitvoeren",
                    "Privacy notice opstellen en publiceren",
                    "Rechtmatige grondslag vastleggen en documenteren",
                    "Beveiligingsmaatregelen implementeren"
                ],
                gaps=[
                    "DPIA nog niet uitgevoerd",
                    "Privacy notice ontbreekt", 
                    "Compliance review nodig"
                ],
                immediate_actions=[
                    ActionItem(
                        title="Review AI Analyse",
                        description=f"Review de gegenereerde analyse: {response_text}",
                        priority="high",
                        timeline="Voor go-live",
                        resources=["DPO", "Legal team"]
                    ),
                    ActionItem(
                        title="DPIA opstarten",
                        description="Data Protection Impact Assessment uitvoeren voor het AI systeem",
                        priority="high",
                        timeline="Voor go-live",
                        resources=["DPO", "Legal team"]
                    )
                ],
                risk_assessment="Medium risico: AI systeem verwerkt mogelijk persoonlijke gegevens van burgers. Compliance verificatie is verplicht.",
                timeline="6-8 weken voor volledige compliance",
                budget_implications="Circa €15.000-25.000 voor compliance consultancy en implementatie"
            )
        elif response_type_class == TechnicalGuidance:
            return TechnicalGuidance(
                solution_approach=response_text,
                architecture_recommendations=[
                    "Gebruik API-first design principes",
                    "Implementeer microservices architectuur", 
                    "Volg Common Ground standaarden",
                    "Zet cloud-native oplossing op"
                ],
                implementation_steps=[
                    ActionItem(
                        title="Analyseer technische vereisten",
                        description="Review de volledige AI guidance en identificeer specifieke technische behoeften",
                        priority="high",
                        timeline="Deze week",
                        resources=["IT Architect", "Development team"]
                    )
                ],
                technology_stack=[
                    "FastAPI/Node.js voor backend",
                    "React/Vue.js voor frontend",
                    "PostgreSQL voor database",
                    "Docker voor containerization",
                    "Kubernetes voor orchestration"
                ],
                common_pitfalls=[
                    "Onvoldoende security maatregelen",
                    "Geen backup en disaster recovery plan",
                    "Inadequate monitoring en logging",
                    "Verkeerde API versioning strategie"
                ],
                best_practices=[
                    "Implementeer comprehensive testing",
                    "Gebruik Infrastructure as Code",
                    "Zet proper monitoring op",
                    "Documenteer alle API endpoints",
                    "Volg security best practices"
                ],
                testing_strategy="Unit tests, integration tests, end-to-end tests en security testing",
                monitoring_requirements=[
                    "Application performance monitoring",
                    "Infrastructure monitoring",
                    "Security monitoring en alerting",
                    "User experience tracking"
                ]
            )
        else:
            # StructuredAIResponse
            knowledge_sources = self._extract_knowledge_sources(docs) if docs else []
            
            return StructuredAIResponse(
                main_answer=response_text,
                response_type=ResponseType.DIRECT_ANSWER,
                confidence_level=confidence,
                complexity=complexity,
                action_items=[],
                compliance_checks=[],
                knowledge_sources=knowledge_sources,
                follow_up_suggestions=self._generate_follow_up_suggestions(
                    UserContext(role=UserRole.OTHER), response_text
                ),
                needs_human_expert=complexity == ComplexityLevel.EXPERT_REQUIRED,
                expert_reason="Complex onderwerp vereist expert beoordeling" if complexity == ComplexityLevel.EXPERT_REQUIRED else None,
                expert_type="legal" if complexity == ComplexityLevel.EXPERT_REQUIRED else None,
                relevant_regulations=[RegulationType.GENERAL],
                stakeholders=[],
                processing_time_ms=1000,
                token_usage=None
            )

    def _create_demo_structured_response(self, message: str, response_type_class: Type, docs: List[Dict], complexity: ComplexityLevel, confidence: ConfidenceLevel):
        """Create demo structured response voor development/testing"""
        message_lower = message.lower()
        
        # Create response text based on message content
        response_text = ""
        
        # GDPR/Compliance specific demo - check for any compliance terms
        compliance_terms = ['gdpr', 'dpia', 'privacy', 'compliance', 'avg', 'gegevensbescherming', 'wet', 'regelgeving']
        if any(term in message_lower for term in compliance_terms):
            response_text = f"""## GDPR Compliance voor Gemeente AI Systeem

Voor de implementatie van een AI systeem binnen de gemeente zijn de volgende GDPR maatregelen essentieel:

### 🔒 Rechtmatige Grondslag
- **Gerechtvaardigd belang** voor publieke dienstverlening
- **Wettelijke verplichting** voor overheidstaken
- Documenteer en communiceer de grondslag duidelijk aan gebruikers

### 📋 Transparantie & Informatieplicht
- Stel een duidelijke **privacy notice** op voor gebruik
- Leg uit dat gebruikers met een AI systeem interacteren
- Vermeld doeleinden van gegevensverwerking
- Geef contactgegevens van de DPO (Data Protection Officer)

### 🛡️ Dataminimalisatie & Beveiliging
- Verzamel alleen **noodzakelijke** gegevens voor de service
- Gebruik **encryptie** voor data in transit en at rest
- Implementeer toegangscontrole voor beheerders
- Voer regelmatige security assessments uit

### ⏰ Bewaartermijnen
- Stel duidelijke bewaartermijnen vast voor chat data
- Implementeer automatische verwijdering na afloop termijn
- Documenteer retentiebeleid in DPIA"""

        elif any(term in message_lower for term in ['architectuur', 'technisch', 'implementatie', 'api', 'system']):
            response_text = f"""## Technische Architectuur voor Gemeente AI Systeem

Voor een robuuste en schaalbare AI implementatie adviseer ik de volgende technische aanpak:

### 🏗️ Aanbevolen Architectuur
- **Microservices** architectuur voor schaalbaarheid
- **API Gateway** voor centraal beheer en security
- **Container orchestration** met Docker/Kubernetes
- **Cloud-agnostic** deployment voor vendor onafhankelijkheid

### 💻 Technology Stack
- **Frontend**: React/Vue.js met TypeScript
- **Backend**: FastAPI (Python) of Express.js (Node.js)
- **Database**: PostgreSQL voor structured data
- **Caching**: Redis voor session management
- **AI Integration**: OpenAI API met LangChain orchestration

### 🔐 Security & Compliance
- HTTPS/TLS 1.3 encryptie verplicht
- OAuth 2.0 / OIDC authenticatie
- API rate limiting en monitoring
- Comprehensive audit logging
- Regular security assessments

### 📊 Monitoring & Observability
- Application Performance Monitoring (APM)
- Infrastructure monitoring met alerts
- API response times en error rate tracking
- User behavior analytics voor optimalisatie"""

        else:
            response_text = f"""## Gemeente AI Assistant Response

Bedankt voor je vraag: "{message}"

Als gemeente professional help ik je graag met digitale transformatie vraagstukken. Gebaseerd op de beschikbare knowledge base met {len(docs)} relevante documenten, kan ik je ondersteunen bij:

### 🎯 Algemene Aanbevelingen
- Raadpleeg de relevante gemeente richtlijnen
- Volg best practices voor digitale dienstverlening
- Zorg voor adequate stakeholder betrokkenheid
- Implementeer iteratieve aanpak met feedback loops

### 📚 Knowledge Base Informatie
Er zijn {len(docs)} relevante documenten gevonden die aansluiten bij je vraag. Deze bevatten specifieke richtlijnen en best practices voor gemeente digitalisering.

### 🔍 Vervolgstappen
1. Review de aangeleverde bronnen uit de knowledge base
2. Bepaal welke aspecten specifiek van toepassing zijn op jouw situatie
3. Overleg met relevante stakeholders en experts
4. Stel een implementatieplan op met concrete mijlpalen"""

        # Always return StructuredAIResponse
        return StructuredAIResponse(
            main_answer=response_text,
            response_type=AIResponseFormat.STRUCTURED,
            confidence_level=confidence,
            complexity=complexity,
            knowledge_sources=self._extract_knowledge_sources(docs),
            action_items=self._extract_action_items(response_text),
            follow_up_suggestions=[],  # Will be filled later
            needs_human_expert=complexity == "high" or confidence == "low",
            relevant_regulations=self._identify_regulations(response_text),
            processing_time_ms=1000
        )
            
            # Determine regulation type based on message content
            regulation_type = RegulationType.AI_ACT if 'ai act' in message_lower else RegulationType.GDPR
            if 'woo' in message_lower or 'wet open overheid' in message_lower:
                regulation_type = RegulationType.WOO
            
            # Generate main AI response without metadata
            main_response = f"""Bij de implementatie van een chatbot binnen een gemeentelijke context moet je rekening houden met verschillende wet- en regelgeving om te zorgen voor compliance. Hier zijn de belangrijkste wetten en regels:

**Algemene Verordening Gegevensbescherming (AVG/GDPR):** Deze Europese wetgeving is cruciaal voor de bescherming van persoonsgegevens. Zorg ervoor dat de chatbot alleen de noodzakelijke gegevens verzamelt en dat er duidelijke toestemming is van de gebruikers.

**Wet open overheid (Woo):** Deze wet verplicht overheden om informatie actief openbaar te maken. Zorg ervoor dat de chatbot geen vertrouwelijke informatie verstrekt.

**AI Act (EU):** Deze nieuwe wetgeving stelt eisen aan AI-systemen zoals chatbots, met focus op transparantie, risicobeheer en menselijke controle.

**Algoritmekader:** Dit Nederlandse kader helpt bij het waarborgen dat algoritmen voldoen aan wettelijke en ethische normen. Transparantie over besluitvorming is essentieel.

Het is aan te raden om samen te werken met een juridisch expert om ervoor te zorgen dat de implementatie volledig compliant is."""
            
            return ComplianceAnalysis(
                regulation_type=regulation_type,
                compliance_status="needs_assessment",
                main_answer=main_response,  # Add main answer field
                requirements=[
                    "Data Protection Impact Assessment (DPIA) uitvoeren",
                    "Privacy notice opstellen en publiceren", 
                    "Rechtmatige grondslag vastleggen en documenteren",
                    "Bewaartermijnen definiëren voor chat logs",
                    "Beveiligingsmaatregelen implementeren (encryptie, toegangscontrole)",
                    "Algoritmekader compliance check uitvoeren",
                    "Transparantie documentatie opstellen"
                ],
                gaps=[
                    "DPIA nog niet uitgevoerd",
                    "Privacy notice ontbreekt",
                    "Bewaartermijn policy niet vastgesteld",
                    "Algoritmekader assessment ontbreekt",
                    "AI Act compliance review niet uitgevoerd"
                ],
                immediate_actions=[
                    ActionItem(
                        title="DPIA opstarten",
                        description="Data Protection Impact Assessment uitvoeren voor de chatbot implementatie",
                        priority="high",
                        timeline="Voor go-live",
                        resources=["DPO", "IT Security", "Legal team"]
                    ),
                    ActionItem(
                        title="Privacy notice schrijven",
                        description="Duidelijke gebruikersinformatie opstellen over dataverwerking",
                        priority="high",
                        timeline="2 weken",
                        resources=["Communications team", "Legal counsel"]
                    ),
                    ActionItem(
                        title="Algoritmekader assessment",
                        description="Compliance check uitvoeren volgens het Nederlandse Algoritmekader",
                        priority="medium",
                        timeline="4 weken",
                        resources=["Data team", "Legal team"]
                    )
                ],
                risk_assessment="Medium risico: chatbot verwerkt mogelijk persoonlijke gegevens van burgers. GDPR en AI Act compliance is verplicht voor overheidsorganisaties.",
                timeline="6-8 weken voor volledige compliance",
                budget_implications="Circa €15.000-25.000 voor externe compliance consultancy en implementatie"
            )
        
        # Technical guidance demo
        elif 'architectuur' in message_lower or 'technical' in message_lower or response_type_class == TechnicalGuidance:
            return TechnicalGuidance(
                solution_approach="Cloud-native microservices architectuur met Common Ground principes",
                architecture_recommendations=[
                    "API-first design met OpenAPI 3.0 specificaties",
                    "Containerized deployment met Docker en Kubernetes",
                    "Horizontaal schaalbare backend services",
                    "Separate frontend en backend voor flexibiliteit",
                    "Message queuing voor asynchrone processing"
                ],
                implementation_steps=[
                    ActionItem(
                        title="API Gateway opzetten",
                        description="Implementeer API gateway voor routing, rate limiting en security",
                        priority="high",
                        timeline="Week 1-2",
                        resources=["DevOps engineer", "Backend developer"]
                    ),
                    ActionItem(
                        title="Database design",
                        description="Ontwerp database schema voor chat historie en gebruikersgegevens",
                        priority="high",
                        timeline="Week 2-3",
                        resources=["Database architect", "Backend developer"]
                    ),
                    ActionItem(
                        title="AI service integratie",
                        description="Integreer OpenAI API met fallback mechanismen",
                        priority="medium",
                        timeline="Week 3-4",
                        resources=["AI/ML engineer", "Backend developer"]
                    )
                ],
                technology_stack=[
                    "Frontend: React/TypeScript",
                    "Backend: FastAPI/Python of Node.js/Express",
                    "Database: PostgreSQL voor structured data",
                    "Cache: Redis voor sessions",
                    "AI: OpenAI GPT-4o met LangChain",
                    "Infrastructure: Docker, Kubernetes, Azure/AWS"
                ],
                common_pitfalls=[
                    "Vendor lock-in bij AI providers - gebruik abstractie layer",
                    "Inadequate error handling bij AI API failures",
                    "Onvoldoende rate limiting kan tot hoge kosten leiden",
                    "Security gaps in API endpoints"
                ],
                best_practices=[
                    "Implementeer comprehensive logging en monitoring",
                    "Gebruik API versioning vanaf dag 1",
                    "Zet health checks op voor alle services",
                    "Documenteer API endpoints met OpenAPI",
                    "Implementeer graceful degradation"
                ],
                testing_strategy="Unit tests voor business logic, integration tests voor API endpoints, end-to-end tests voor user flows",
                monitoring_requirements=[
                    "Application Performance Monitoring (APM)",
                    "API response times en error rates",
                    "AI service usage en kosten tracking",
                    "User behavior analytics"
                ]
            )
        
        # Quick answer demo
        elif response_type_class == QuickAnswer:
            return QuickAnswer(
                answer=f"Voor je vraag over '{message}' raad ik aan om te beginnen met het raadplegen van de relevante gemeente richtlijnen en best practices. Check de knowledge base voor specifieke documentatie.",
                confidence=0.8,
                sources=["Gemeente Digitale Agenda 2028", "Common Ground Standaarden"],
                follow_up="Wil je meer specifieke informatie over implementatie of compliance aspecten?"
            )
        
        # Default structured response
        else:
            knowledge_sources = self._extract_knowledge_sources(docs) if docs else []
            
            return StructuredAIResponse(
                main_answer=f"""## Demo Response: {message}

Als **gemeente professional** help ik je graag met je vraag over digitale transformatie.

### 🔍 Knowledge Base Resultaten
Ik heb **{len(docs)} relevante documenten** gevonden in de knowledge base met betrekking tot je vraag.

### 📋 Aanbevolen Acties
1. **Raadpleeg relevante documentatie** uit de knowledge base
2. **Check compliance vereisten** voor je specifieke use case
3. **Implementeer best practices** uit vergelijkbare projecten
4. **Plan stakeholder betrokkenheid** vanaf vroege fase

### ⚠️ Belangrijke Overwegingen
- Zorg voor GDPR compliance bij dataverwerking
- Volg Common Ground architectuurprincipes
- Implementeer privacy by design
- Plan adequate fallback procedures

**Note:** Dit is een demo response. Voor productie gebruik configureer een echte OpenAI API key.""",
                response_type=ResponseType.GUIDANCE,
                confidence_level=confidence,
                complexity=complexity,
                action_items=[
                    ActionItem(
                        title="Raadpleeg documentatie",
                        description="Review relevante documenten uit de knowledge base",
                        priority="medium",
                        timeline="Deze week"
                    ),
                    ActionItem(
                        title="Check compliance",
                        description="Analyseer specifieke compliance vereisten voor je use case",
                        priority="high",
                        timeline="Voor implementatie"
                    )
                ],
                compliance_checks=[],
                knowledge_sources=knowledge_sources,
                follow_up_suggestions=self._generate_follow_up_suggestions(
                    UserContext(role=UserRole.OTHER), message
                ),
                needs_human_expert=complexity == ComplexityLevel.EXPERT_REQUIRED,
                expert_reason="Complex onderwerp vereist expert beoordeling" if complexity == ComplexityLevel.EXPERT_REQUIRED else None,
                expert_type="legal" if complexity == ComplexityLevel.EXPERT_REQUIRED else None,
                relevant_regulations=[RegulationType.GENERAL],
                stakeholders=[],
                processing_time_ms=800,
                token_usage=None
            )

    def _count_tokens(self, text: str) -> int:
        """Count tokens in text"""
        try:
            return len(self.encoding.encode(text))
        except:
            return len(text.split())  # Fallback

    async def health_check(self) -> Dict[str, any]:
        """Enhanced health check met knowledge base status"""
        try:
            # Knowledge base statistics
            kb_stats = self.knowledge_base.get_statistics()
            
            health_data = {
                "status": "healthy",
                "model": self.model,
                "demo_mode": self.demo_mode,
                "knowledge_base": {
                    "status": "loaded" if kb_stats['total_documents'] > 0 else "empty",
                    "documents": kb_stats['total_documents'],
                    "document_types": kb_stats.get('document_types', {}),
                    "total_tokens": kb_stats.get('total_tokens', 0)
                }
            }
            
            if not self.demo_mode:
                # Test echte OpenAI API alleen als niet in demo mode
                response = await self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": "Test"}],
                    max_tokens=10
                )
                health_data["api_usage"] = response.usage.dict() if response.usage else None
            else:
                health_data["api_usage"] = "demo_mode_active"
            
            return health_data
            
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return {
                "status": "unhealthy" if not self.demo_mode else "demo_mode",
                "demo_mode": self.demo_mode,
                "error": str(e),
                "knowledge_base": {"status": "unknown"}
            }