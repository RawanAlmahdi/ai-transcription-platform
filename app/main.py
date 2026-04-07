from fastapi import FastAPI

# Import models (VERY IMPORTANT)
from app.db.database import engine, Base
from app.models import user

app = FastAPI(title="AI Transcription Platform")


@app.get("/")
def root():
    return {"message": "AI Transcription API is running"}


Base.metadata.create_all(bind=engine)