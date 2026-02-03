from fastapi import APIRouter, HTTPException, Depends, Request
from loguru import logger
import time
from datetime import datetime

from app.models.chat import ChatMessage, ChatResponse, FeedbackRequest, ExpertContact
from app.models.ai_responses import StructuredAIResponse, QuickAnswer, ComplianceAnalysis, TechnicalGuidance, ErrorResponse
from app.services.enhanced_openai_service import EnhancedOpenAIService

router = APIRouter()

def get_openai_service(request: Request) -> EnhancedOpenAIService:
    """Dependency to get Enhanced OpenAI service from app state"""
    return request.app.state.openai_service

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    chat_message: ChatMessage,
    openai_service: EnhancedOpenAIService = Depends(get_openai_service)
):
    """
    Main chat endpoint for processing user messages
    """
    start_time = time.time()
    
    try:
        logger.info(f"Processing chat message from {chat_message.context.role}: {chat_message.message[:100]}...")
        
        # Validate message length
        if len(chat_message.message) > 1000:
            raise HTTPException(
                status_code=400,
                detail="Bericht is te lang. Maximaal 1000 karakters toegestaan."
            )
        
        # Generate response using OpenAI service
        response = await openai_service.generate_response(chat_message)
        
        # Add response time
        response.responseTime = time.time() - start_time
        
        logger.info(f"Chat response generated in {response.responseTime:.2f}s with confidence {response.confidence:.2f}")
        
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        raise HTTPException(
            status_code=500,
            detail="Er ging iets mis bij het verwerken van je bericht. Probeer het opnieuw."
        )

@router.post("/feedback")
async def submit_feedback(feedback: FeedbackRequest):
    """
    Endpoint for submitting user feedback on AI responses
    """
    try:
        logger.info(f"Received feedback: {feedback.messageId} - {'positive' if feedback.isPositive else 'negative'}")
        
        # In a real implementation, you would:
        # 1. Store feedback in database
        # 2. Use for model fine-tuning
        # 3. Analytics and monitoring
        
        # For now, just log and return success
        feedback_data = {
            "messageId": feedback.messageId,
            "isPositive": feedback.isPositive,
            "comment": feedback.comment,
            "timestamp": feedback.timestamp,
            "processed": True
        }
        
        return {
            "message": "Bedankt voor je feedback!",
            "status": "received"
        }
        
    except Exception as e:
        logger.error(f"Error submitting feedback: {e}")
        raise HTTPException(
            status_code=500,
            detail="Er ging iets mis bij het verwerken van je feedback."
        )

@router.get("/expert-contact", response_model=ExpertContact)
async def get_expert_contact():
    """
    Get contact information for human expert assistance
    """
    try:
        # In a real implementation, this would come from a database or CRM
        # and potentially route based on the user's context and location
        
        expert_contact = ExpertContact(
            name="Digitalisering Support Team",
            email="digitalisering@gemeente.nl",
            phone="+31 20 123 4567",
            department="ICT & Digitalisering",
            specializations=[
                "AI & Machine Learning",
                "GDPR & Privacy",
                "Common Ground Architectuur",
                "API Management",
                "Cloud Migratie"
            ],
            available="Maandag t/m Vrijdag: 09:00 - 17:00"
        )
        
        return expert_contact
        
    except Exception as e:
        logger.error(f"Error getting expert contact: {e}")
        raise HTTPException(
            status_code=500,
            detail="Er ging iets mis bij het ophalen van contactgegevens."
        )

@router.get("/suggestions/{role}")
async def get_role_suggestions(role: str):
    """
    Get role-specific question suggestions
    """
    try:
        suggestions_map = {
            "digital-guide": [
                "Hoe zorg ik voor draagvlak bij een AI implementatie?",
                "Welke stakeholders moet ik betrekken bij digitale transformatie?",
                "Hoe manage ik risico's bij innovatieve projecten?",
                "Wat zijn best practices voor change management?",
                "Hoe communiceer ik technische complexiteit naar bestuur?"
            ],
            "civil-servant": [
                "Welke GDPR eisen gelden voor gemeente chatbots?",
                "Hoe ga ik om met AI Act verplichtingen?",
                "Wat zijn transparantie vereisten voor AI systemen?",
                "Hoe implementeer ik privacy by design?",
                "Welke documentatie moet ik bijhouden voor compliance?"
            ],
            "it-manager": [
                "Welke architectuurprincipes moet ik volgen voor Common Ground?",
                "Hoe voorkom ik vendor lock-in bij AI leveranciers?",
                "Wat zijn security requirements voor overheids-AI?",
                "Hoe integreer ik AI met bestaande systemen?",
                "Welke monitoring en logging is vereist?"
            ],
            "project-manager": [
                "Hoe plan ik een AI implementatie stap voor stap?",
                "Welke success metrics definieer ik voor AI projecten?",
                "Hoe budget ik voor AI ontwikkeling en onderhoud?",
                "Wat zijn kritieke risico's bij AI projecten?",
                "Hoe organiseer ik multidisciplinaire AI teams?"
            ],
            "developer": [
                "Welke open standaarden moet ik gebruiken voor gemeente APIs?",
                "Hoe implementeer ik Common Ground componenten?",
                "Waar vind ik code voorbeelden voor overheids-AI?",
                "Welke testing frameworks zijn geschikt voor AI systemen?",
                "Hoe zorg ik voor reproduceerbare AI deployments?"
            ],
            "other": [
                "Waar moet ik beginnen met digitale transformatie?",
                "Welke regelgeving is relevant voor mijn AI project?",
                "Hoe kies ik de juiste AI technologie?",
                "Welke training heb ik nodig voor AI projecten?",
                "Wie kan me verder helpen met specifieke vragen?"
            ]
        }
        
        suggestions = suggestions_map.get(role, suggestions_map["other"])
        
        return {
            "role": role,
            "suggestions": suggestions,
            "total": len(suggestions)
        }
        
    except Exception as e:
        logger.error(f"Error getting suggestions for role {role}: {e}")
        raise HTTPException(
            status_code=500,
            detail="Er ging iets mis bij het ophalen van suggesties."
        )