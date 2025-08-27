from backend.database.Database import SessionLocal
from backend.model.SummaryBook import SummaryBook

def get_book_summaries_from_db():
    db = SessionLocal()
    books = db.query(SummaryBook).all()
    db.close()
    return books