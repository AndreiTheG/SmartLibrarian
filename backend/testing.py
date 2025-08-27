from backend.database.Database import SessionLocal
from backend.model.SummaryBook import SummaryBook

db = SessionLocal()
print(db.query(SummaryBook).count())