import os
from pathlib import Path

import psycopg2
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent


@app.get("/health")
def health():
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        conn.close()
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}


app.mount("/", StaticFiles(directory=BASE_DIR, html=True), name="static")
