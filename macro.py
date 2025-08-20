# backend.py
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
 # your existing code
import shutil

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/ask")
def ask_text(req: TextRequest):
    answer = marco.get_ai_response(req.text)
    return {"marco": answer}

@app.post("/ask-audio")
def ask_audio(file: UploadFile = File(...)):
    with open("voice.wav", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # Process the audio file if needed
    return {"message": "Audio received"}
