from fastapi import FastAPI
from loguru import logger

def get_app() -> FastAPI:
    """
    FastAPI app initialization.
    """

    fastapi_app = FastAPI(
        title="Emotion classification service",
        version="0.1.0",
        debug=False,
        description="ML service for classifying emotions in text"
    )

    logger.info("FastAPI application has been initialized")
    return fastapi_app


app = get_app()