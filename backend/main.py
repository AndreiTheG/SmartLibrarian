from fastapi import FastAPI
from .routers import SummaryBookRoutes
from .database.Database import create_tables
from backend.routers.chat import router as chat_router

app = FastAPI(title = "Smart Librarian")

create_tables()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(SummaryBookRoutes.router)
app.include_router(chat_router)