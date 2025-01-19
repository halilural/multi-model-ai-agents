from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.models.models import TopicRequest, TaskResponse
from app.services.services import BotService

router = APIRouter()

@router.post("/analyze", response_model=TaskResponse)
async def analyze_topic(request: TopicRequest, background_tasks: BackgroundTasks):
    task_id = BotService.create_task(request.topic)
    background_tasks.add_task(BotService.process_task, task_id, request.topic)
    return BotService.get_task_status(task_id)

@router.get("/task/{task_id}", response_model=TaskResponse)
async def get_task_status(task_id: str):
    task = BotService.get_task_status(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task