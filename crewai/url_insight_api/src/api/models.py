from enum import Enum
from pydantic import BaseModel
from typing import Optional, Dict, Any

class TaskStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class TopicRequest(BaseModel):
    topic: str

class TaskResponse(BaseModel):
    task_id: str
    status: TaskStatus
    result: Optional[Dict[str, Any]] = None