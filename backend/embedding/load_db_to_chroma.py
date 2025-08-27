from .embedder import get_embedding
from .extractDB import get_book_summaries_from_db
from backend.chroma_config import collection


print("📚 Start uploading the books in ChromaDB..")

book_summaries = get_book_summaries_from_db()

for book_summary in book_summaries:
    embedding = get_embedding(book_summary.summary)
    collection.add(
        ids=[str(book_summary.id)],
        embeddings=[embedding],
        documents=[book_summary.summary],
        metadatas=[{"title": book_summary.title}]
    )

print("✅ Vectori încărcați:", collection.count())