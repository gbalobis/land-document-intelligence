"""Land Document Intelligence — Week 1 skeleton.

FastAPI service. /health is live. /extract is a stub until
ingestion + RAG land in Phase 2.
"""
from fastapi import FastAPI

app = FastAPI(title="Land Document Intelligence")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/extract")
def extract_stub():
    return {
        "status": "not_implemented",
        "message": "Extraction lands in Phase 2 — ingestion, chunking, embeddings, then RAG.",
    }
