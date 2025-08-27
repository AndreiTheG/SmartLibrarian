from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []  # 👈 primești istoricul