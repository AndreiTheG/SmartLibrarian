from ..model.SummaryBookModel import SummaryBookModel, SummaryBookOut
from ..model.SummaryBook import SummaryBook
from ..database.Database import get_db
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/books_summary/")
def create_summary_book(summary_book: SummaryBookModel, db: Session = Depends(get_db)):
    db_summary_book = SummaryBook(title=summary_book.title, summary=summary_book.summary)
    db.add(db_summary_book)
    db.commit()
    db.refresh(db_summary_book)
    return db_summary_book

@router.get("/books_summary/{id}", response_model=SummaryBookOut)
def get_summary_book(id: int, db: Session = Depends(get_db)):
    summary = db.query(SummaryBook).filter(SummaryBook.id == id).first()
    if not summary:
        raise HTTPException(status_code=404, detail="Book summary not found")
    return summary

