from backend.database.Database import SessionLocal
from backend.model.SummaryBook import SummaryBook

# Get the book summaries from database
def get_book_summaries_from_db():
    db = SessionLocal()
    books = db.query(SummaryBook).all()
    db.close()
    return books