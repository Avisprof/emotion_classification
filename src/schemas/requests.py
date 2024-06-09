from pydantic import BaseModel, ConfigDict

class TextRequest(BaseModel):
    """
    Модель запроса для классификации эмоций по тексту.

    Attributes:
        text (str): Текст для анализа эмоций.
    """

    text: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "text": "Hello! How are you?"
            }
        }
    )
