from chromadb import Client
from chromadb.config import Settings

client = Client(Settings(persist_directory="./chroma_store"))
collection = client.get_or_create_collection("book_summaries")