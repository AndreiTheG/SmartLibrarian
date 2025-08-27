from sqlalchemy import Column, Integer, String
from backend.database.Database import Base

class SummaryBook(Base):
    __tablename__ = "book_summaries"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    summary = Column(String)
