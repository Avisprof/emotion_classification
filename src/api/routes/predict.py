from fastapi import APIRouter, BackgroundTasks
from loguru import logger

from src.schemas.requests import TextRequest
from src.services.model import EmotionClassifier
from src.services.utils import print_logger_info

router = APIRouter()

@router.post("/predict/")
async def predict_emotion(text_request: TextRequest, background_tasks: BackgroundTasks):
    """
    Предсказание эмоции по тексту.

    Args:
        text_request (TextRequest): Текстовый запрос.

    Returns:
        dict: Результат предсказания в формате словаря.
    """
    logger.info(f"input: {text_request.text}")
    result = EmotionClassifier.predict_emotion(text_request.text)
    logger.info(f"result: {result}")
    
    background_tasks.add_task(
        print_logger_info,
        text_request.text,
        result
    )  

    return result
