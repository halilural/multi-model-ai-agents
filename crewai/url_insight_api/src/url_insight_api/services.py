import asyncio
import uuid
import logging
from typing import Dict
from .models import TaskStatus, TaskResponse
from .crew import UrlInsightBot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BotService:
    _tasks: Dict[str, TaskResponse] = {}
    
    @classmethod
    def create_task(cls, topic: str) -> str:
        task_id = str(uuid.uuid4())
        cls._tasks[task_id] = TaskResponse(
            task_id=task_id,
            status=TaskStatus.PENDING
        )
        logger.info(f"Task {task_id} created with status PENDING for topic: {topic}")
        return task_id

    @classmethod
    async def process_task(cls, task_id: str, topic: str):
        try:
            cls._tasks[task_id].status = TaskStatus.PROCESSING
            logger.info(f"Task {task_id} status changed to PROCESSING")
            bot = UrlInsightBot()
            result = await bot.crew().kickoff_async(inputs={'topic': topic})
            cls._tasks[task_id].status = TaskStatus.COMPLETED
            cls._tasks[task_id].result = result
            logger.info(f"Task {task_id} completed successfully with status {cls._tasks[task_id].status}")
        except Exception as e:
            cls._tasks[task_id].status = TaskStatus.FAILED
            cls._tasks[task_id].error = str(e)
            logger.error(f"Task {task_id} failed with error: {e}")
            
    @classmethod
    async def process_task_sleep(cls, task_id: str, topic: str):
        try:
            cls._tasks[task_id].status = TaskStatus.PROCESSING
            logger.info(f"Task {task_id} status changed to PROCESSING")
            # Simulate processing
            await asyncio.sleep(5)  # Simulate a long-running task
            cls._tasks[task_id].status = TaskStatus.COMPLETED
            cls._tasks[task_id].result = f"Processed topic: {topic}"
            logger.info(f"Task {task_id} completed successfully with status {cls._tasks[task_id].status}")
        except Exception as e:
            cls._tasks[task_id].status = TaskStatus.FAILED
            cls._tasks[task_id].error = str(e)

    @classmethod
    def get_task_status(cls, task_id: str) -> TaskResponse:
        return cls._tasks.get(task_id)