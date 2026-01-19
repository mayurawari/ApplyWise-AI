from fastapi import FastAPI
from dotenv import load_dotenv
import os   

load_dotenv()  # Load environment variables from .env file

app = FastAPI(title="Applywise AI",tags=["Application Tracker"])

@app.get("/")
def read_root():
    return {"Hello": "World"}   