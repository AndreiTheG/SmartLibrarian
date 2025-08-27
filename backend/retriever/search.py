from ..embedding.embedder import get_embedding
from backend.chroma_config import collection
from backend.database.Database import SessionLocal
from backend.model.SummaryBook import SummaryBook
from sqlalchemy import or_

def extract_keywords(query: str) -> list[str]:
    stopwords = {
        "i", "want", "a", "book", "about", "please", "find", "me", "can", "do", "you",
        "show", "like", "know", "am", "is", "are", "recommend", "need"
    }

    words = query.lower().split()
    keywords = [word for word in words if word not in stopwords and len(word) > 2]
    return keywords

def search_books_by_theme(query: str, n=3):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n
    )
    print("📦 Număr vectori în colecție:", collection.count())
    print("🔍 Rezultate găsite:", results['documents'][0])
    return results

def search_books_by_theme_db(query: str, max_results:int=3) -> dict:
    db = SessionLocal()
    keywords = extract_keywords(query)

    if not keywords:
        return {"documents": [[]], "metadatas": [[]]}

    print("🔑 Cuvinte cheie:", keywords)

    conditions = [
        or_(
            SummaryBook.summary.ilike(f"%{word}%"),
            SummaryBook.title.ilike(f"%{word}%")
        )
        for word in keywords
    ]

    books = db.query(SummaryBook).filter(or_(*conditions)).limit(max_results).all()
    db.close()

    print("🧱 Căutare SQL pe:", query)
    print("📚 Rezultate SQL:", len(books))
    for book in books:
        print("→", book.title)

    if not books:
        return {"documents": [[]], "metadatas": [[]]}  # compatibil cu generate_response()

    documents = [book.summary for book in books]
    metadatas = [{"title": book.title} for book in books]

    return {"documents": [documents], "metadatas": [metadatas]}


def get_summary_by_title(title:str):
    data = collection.get()

    titles = data["metadatas"]
    summaries = data["documents"]

    for i, meta in enumerate(titles):
        book_title = meta["title"]
        if title.lower() in book_title.lower():
            summary = summaries[i]
            return f" *{book_title}*\n{summary}"

    return "No book with this title was found"

# def get_summary_by_title(title: str) -> str:
#     data = collection.get()
#
#     for i, meta in enumerate(data["metadatas"]):
#         book_title = meta["title"]
#         if title.lower() in book_title.lower():
#             return f"📖 Summary for *{book_title}*:\n{data['documents'][i]}"
#
#     return "❌ No book with this title was found."



def get_summary_by_title_from_db(title: str) -> str:
    db = SessionLocal()
    book = db.query(SummaryBook).filter(SummaryBook.title.ilike(f"%{title}%")).first()
    db.close()

    if book:
        return f"📖 Summary for *{book.title}*:\n{book.summary}"
    else:
        return "❌ No book with this title was found in the database."
