from fastapi import FastAPI

app = FastAPI(title="AI Transcription Platform")


@app.get("/")
def root():
    return {"message": "AI Transcription API is running"}