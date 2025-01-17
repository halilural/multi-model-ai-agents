import asyncio
import uuid
import logging
from typing import Dict
from .models import TaskStatus, TaskResponse
from url_insight_api.crew import UrlInsightBot

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BotService:
    _tasks: Dict[str, TaskResponse] = {}

    @classmethod
    async def process_topic(cls, topic: str) -> str:
        task_id = str(uuid.uuid4())
        cls._tasks[task_id] = TaskResponse(
            task_id=task_id,
            status=TaskStatus.PENDING
        )
        logger.info(f"Task {task_id} created with status PENDING for topic: {topic}")

        async def process():
            try:
                cls._tasks[task_id].status = TaskStatus.PROCESSING
                logger.info(f"Task {task_id} status changed to PROCESSING")
                bot = UrlInsightBot()
                result = bot.crew().kickoff(inputs={'topic': topic})
                cls._tasks[task_id].status = TaskStatus.COMPLETED
                cls._tasks[task_id].result = result
                logger.info(f"Task {task_id} completed with result: {result}")
            except Exception as e:
                cls._tasks[task_id].status = TaskStatus.FAILED
                cls._tasks[task_id].result = {"error": str(e)}
                logger.error(f"Task {task_id} failed with error: {e}")

        asyncio.create_task(process())
        return task_id

    @classmethod
    def get_task_status(cls, task_id: str) -> TaskResponse:
        task = cls._tasks.get(task_id)
        if task:
            logger.info(f"Retrieved status for task {task_id}: {task.status}")
        else:
            logger.warning(f"Task {task_id} not found")
        return task