from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import importlib

from database import startDB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_dependencies():
    try:
        await startDB()
    except Exception as e:
        print(f"Error al iniciar las dependencias: {e}")