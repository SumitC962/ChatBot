from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from chatbot import get_chat_response
from pdf_handler import ingest_pdf, query_pdf
from memory import memory_store

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI chatbot is running!"}

@app.post("/chat/")
async def chat(user_input: str):
    response = get_chat_response(user_input)
    memory_store.append({"user": user_input, "bot": response})
    return JSONResponse(content={"response": response})

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    ingest_pdf(pdf_bytes)
    return {"message": "PDF processed successfully"}

@app.post("/ask-pdf/")
async def ask_pdf(question: str):
    response = query_pdf(question)
    return {"response": response}

@app.get("/history/")
async def get_chat_history():
    return {"history": memory_store}

