from pydantic import BaseModel, ConfigDict

class SummaryBookModel(BaseModel):
    title: str
    summary: str

class SummaryBookOut(SummaryBookModel):
    id: int
    title: str
    summary: str

    model_config = ConfigDict(from_attributes=True)