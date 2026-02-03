from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union
from enum import Enum

class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium" 
    LOW = "low"

class ResponseType(str, Enum):
    DIRECT_ANSWER = "direct_answer"
    GUIDANCE = "guidance"
    ESCALATION = "escalation"
    CLARIFICATION = "clarification"

class ComplexityLevel(str, Enum):
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    EXPERT_REQUIRED = "expert_required"

class RegulationType(str, Enum):
    GDPR = "gdpr"
    AI_ACT = "ai_act"
    WOO = "woo"
    ARCHIEFWET = "archiefwet"
    TOEGANKELIJKHEID = "toegankelijkheid"
    GENERAL = "general"

class ActionItem(BaseModel):
    title: str = Field(description="Korte titel van de actie")
    description: str = Field(description="Gedetailleerde beschrijving")
    priority: Literal["high", "medium", "low"] = Field(description="Prioriteit van de actie")
    timeline: Optional[str] = Field(default=None, description="Verwachte tijdlijn voor voltooiing")
    resources: Optional[List[str]] = Field(default=None, description="Benodigde resources of tools")

class ComplianceCheck(BaseModel):
    regulation: RegulationType = Field(description="Type regelgeving")
    status: Literal["compliant", "non_compliant", "unclear", "needs_review"] = Field(description="Compliance status")
    requirements: List[str] = Field(description="Specifieke vereisten")
    recommendations: List[str] = Field(description="Aanbevelingen voor compliance")
    risk_level: Literal["low", "medium", "high", "critical"] = Field(description="Risico niveau")

class KnowledgeSource(BaseModel):
    title: str = Field(description="Titel van de bron")
    url: Optional[str] = Field(description="URL naar de bron")
    snippet: str = Field(description="Relevante tekstfragment")
    relevance_score: float = Field(ge=0.0, le=1.0, description="Relevantie score van 0 tot 1")
    document_type: Literal["law", "guideline", "best_practice", "case_study", "faq"] = Field(description="Type document")
    document_id: Optional[str] = Field(description="ID van het document voor interne referentie")
    
    # Enhanced RAG specific fields
    file_path: Optional[str] = Field(description="Pad naar het bronbestand")
    section_title: Optional[str] = Field(description="Titel van de sectie binnen het document")
    chunk_index: Optional[int] = Field(description="Index van het chunk binnen het document")
    total_chunks: Optional[int] = Field(description="Totaal aantal chunks in het document")
    original_url: Optional[str] = Field(description="Originele URL van de bron")
    document_title: Optional[str] = Field(description="Originele titel van het document")

class FollowUpSuggestion(BaseModel):
    question: str = Field(description="Voorgestelde vervolgvraag")
    category: Literal["technical", "legal", "process", "policy"] = Field(description="Categorie van de vraag")
    relevance: float = Field(ge=0.0, le=1.0, description="Relevantie voor de gebruiker")

class StructuredAIResponse(BaseModel):
    """Structured response format voor gemeente AI assistant"""
    
    # Core Response
    main_answer: str = Field(description="Hoofdantwoord in markdown formaat")
    response_type: ResponseType = Field(description="Type response")
    confidence_level: ConfidenceLevel = Field(description="Betrouwbaarheidsniveau van het antwoord")
    complexity: ComplexityLevel = Field(description="Complexiteit van het onderwerp")
    
    # Actionable Information
    action_items: Optional[List[ActionItem]] = Field(description="Concrete actiepunten voor de gebruiker")
    compliance_checks: Optional[List[ComplianceCheck]] = Field(description="Relevante compliance controles")
    
    # Supporting Information
    knowledge_sources: List[KnowledgeSource] = Field(description="Bronnen die het antwoord ondersteunen")
    follow_up_suggestions: List[FollowUpSuggestion] = Field(description="Voorgestelde vervolgvragen")
    
    # Escalation Logic
    needs_human_expert: bool = Field(description="Heeft dit onderwerp menselijke expertise nodig")
    expert_reason: Optional[str] = Field(description="Reden waarom expert nodig is")
    expert_type: Optional[Literal["legal", "technical", "policy", "security"]] = Field(description="Type expert dat nodig is")
    
    # Context Awareness
    relevant_regulations: List[RegulationType] = Field(description="Relevante regelgeving voor dit onderwerp")
    stakeholders: Optional[List[str]] = Field(description="Relevante stakeholders om te betrekken")
    
    # Quality Metrics
    processing_time_ms: Optional[int] = Field(description="Verwerkingstijd in milliseconden")
    token_usage: Optional[int] = Field(description="Aantal tokens gebruikt")

class ErrorResponse(BaseModel):
    """Structured error response"""
    error_type: Literal["api_error", "validation_error", "rate_limit", "unknown"] = Field(description="Type fout")
    error_message: str = Field(description="Gebruikersvriendelijke foutmelding")
    technical_details: Optional[str] = Field(description="Technische details voor debugging")
    suggested_action: str = Field(description="Voorgestelde actie voor gebruiker")
    needs_human_help: bool = Field(default=True, description="Heeft dit situatie menselijke hulp nodig")

class QuickAnswer(BaseModel):
    """Voor eenvoudige, snelle antwoorden"""
    answer: str = Field(description="Direct antwoord")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    sources: List[str] = Field(description="Korte lijst van bronnen")
    follow_up: Optional[str] = Field(description="Optionale vervolgvraag")

class ComplianceAnalysis(BaseModel):
    """Gespecialiseerd voor compliance vragen"""
    regulation_type: RegulationType = Field(description="Type regelgeving")
    compliance_status: Literal["compliant", "non_compliant", "needs_assessment", "unclear"] = Field(description="Huidige compliance status")
    
    requirements: List[str] = Field(description="Lijst van vereisten")
    gaps: List[str] = Field(description="Geïdentificeerde compliance gaps")
    immediate_actions: List[ActionItem] = Field(description="Directe acties nodig")
    
    risk_assessment: str = Field(description="Risico-evaluatie")
    timeline: str = Field(description="Tijdlijn voor compliance")
    budget_implications: Optional[str] = Field(description="Budgetimplicaties")

class TechnicalGuidance(BaseModel):
    """Voor technische implementatie vragen"""
    solution_approach: str = Field(description="Aanbevolen aanpak")
    architecture_recommendations: List[str] = Field(description="Architectuur aanbevelingen")
    
    implementation_steps: List[ActionItem] = Field(description="Implementatie stappen")
    technology_stack: List[str] = Field(description="Aanbevolen technologie stack")
    
    common_pitfalls: List[str] = Field(description="Veelvoorkomende valkuilen")
    best_practices: List[str] = Field(description="Best practices")
    
    testing_strategy: Optional[str] = Field(description="Test strategie")
    monitoring_requirements: Optional[List[str]] = Field(description="Monitoring vereisten")

# Union type voor alle mogelijke response formats
AIResponseFormat = Union[StructuredAIResponse, QuickAnswer, ComplianceAnalysis, TechnicalGuidance, ErrorResponse]