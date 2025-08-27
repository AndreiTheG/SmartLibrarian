from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import SummaryBookRoutes
from .database.Database import create_tables
from backend.routers.chat import router as chat_router

app = FastAPI(title = "Smart Librarian")

# ✅ CORS: permite comunicarea cu frontendul de pe localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # adaugă și altele dacă ai nevoie
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(SummaryBookRoutes.router)
app.include_router(chat_router)