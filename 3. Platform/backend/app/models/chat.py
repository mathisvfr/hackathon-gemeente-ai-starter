from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    DIGITAL_GUIDE = "digital-guide"
    CIVIL_SERVANT = "civil-servant"
    IT_MANAGER = "it-manager"
    PROJECT_MANAGER = "project-manager"
    DEVELOPER = "developer"
    OTHER = "other"

class FocusArea(str, Enum):
    COMPLIANCE = "compliance"
    TECHNOLOGY = "technology"
    PROCESS = "process"
    INNOVATION = "innovation"

class UserContext(BaseModel):
    role: Optional[UserRole] = None
    roleName: Optional[str] = None
    projectPhase: Optional[str] = None
    focusAreas: List[FocusArea] = []
    specificNeeds: List[str] = []
    customContext: Optional[str] = None

class ChatMessage(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    context: UserContext
    timestamp: datetime

    @validator('message')
    def validate_message(cls, v):
        if not v.strip():
            raise ValueError('Message cannot be empty')
        return v.strip()

class Source(BaseModel):
    title: str
    url: str
    snippet: Optional[str] = None
    relevance_score: Optional[float] = None

class ChatResponse(BaseModel):
    message: str
    confidence: float = Field(ge=0.0, le=1.0)
    sources: List[Source] = []
    needsHumanHelp: bool = False
    suggestions: List[str] = []
    responseTime: Optional[float] = None
    
class FeedbackRequest(BaseModel):
    messageId: str
    isPositive: bool
    comment: Optional[str] = None
    timestamp: datetime

class ExpertContact(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    department: Optional[str] = None
    specializations: List[str] = []
    available: Optional[str] = None

class HealthCheck(BaseModel):
    status: str
    timestamp: datetime
    services: Dict[str, Any]
    version: str