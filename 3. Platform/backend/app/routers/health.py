from fastapi import APIRouter, Depends, Request
from datetime import datetime
import os

from app.models.chat import HealthCheck
from app.services.openai_service import OpenAIService
from app.services.enhanced_openai_service import EnhancedOpenAIService

router = APIRouter()

def get_openai_service(request: Request) -> OpenAIService:
    """Dependency to get OpenAI service from app state"""
    return request.app.state.openai_service

def get_enhanced_openai_service(request: Request) -> EnhancedOpenAIService:
    """Dependency to get Enhanced OpenAI service from app state"""
    return request.app.state.enhanced_openai_service

@router.get("/health", response_model=HealthCheck)
async def health_check(
    openai_service: OpenAIService = Depends(get_openai_service),
    enhanced_service: EnhancedOpenAIService = Depends(get_enhanced_openai_service)
):
    """
    Health check endpoint for monitoring service status
    """
    services_status = {}
    
    # Check legacy OpenAI service
    try:
        openai_status = await openai_service.health_check()
        services_status["openai_legacy"] = openai_status
    except Exception as e:
        services_status["openai_legacy"] = {
            "status": "unhealthy",
            "error": str(e)
        }
    
    # Check enhanced OpenAI service
    try:
        enhanced_status = await enhanced_service.health_check()
        services_status["openai_enhanced"] = enhanced_status
    except Exception as e:
        services_status["openai_enhanced"] = {
            "status": "unhealthy",
            "error": str(e)
        }
    
    # Check environment variables
    required_env_vars = ["GREENPT_API_KEY"]
    env_status = {}
    for var in required_env_vars:
        env_status[var] = "set" if os.getenv(var) else "missing"
    
    services_status["environment"] = {
        "status": "healthy" if all(status == "set" for status in env_status.values()) else "unhealthy",
        "variables": env_status
    }
    
    # Overall status
    overall_status = "healthy" if all(
        service.get("status") == "healthy" 
        for service in services_status.values()
    ) else "unhealthy"
    
    return HealthCheck(
        status=overall_status,
        timestamp=datetime.now(),
        services=services_status,
        version="1.0.0"
    )

@router.get("/ready")
async def readiness_check():
    """
    Kubernetes readiness probe endpoint
    """
    return {"status": "ready", "timestamp": datetime.now()}

@router.get("/live")
async def liveness_check():
    """
    Kubernetes liveness probe endpoint
    """
    return {"status": "alive", "timestamp": datetime.now()}