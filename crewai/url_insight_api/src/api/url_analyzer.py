from fastapi import FastAPI, HTTPException
from .models import TopicRequest, TaskResponse
from .services import BotService

app = FastAPI(title="URL Insight Bot API")

@app.post("/api/analyze", response_model=TaskResponse)
async def analyze_topic(request: TopicRequest):
    task_id = await BotService.process_topic(request.topic)
    return BotService.get_task_status(task_id)

@app.get("/api/task/{task_id}", response_model=TaskResponse)
async def get_task_status(task_id: str):
    task = BotService.get_task_status(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task