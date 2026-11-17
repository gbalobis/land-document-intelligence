# Land Document Intelligence

LLM extraction + RAG over land-style documents — built as Week 1 of a 90-day AI/ML Engineering pivot.

**Problem:** Land files are messy — scanned PDFs, leases, mineral / surface agreements, regulatory letters. Finding the key terms (parties, lands, term, royalties, obligations) means reading every page by hand.

**What this does (Week 1 skeleton):**
- FastAPI service with a `/health` check and a stub `/extract` endpoint
- Dockerised, so it runs the same locally and in CI
- pytest covering the health endpoint
- Synthetic sample documents only — **no real client, employer, or personal land data in this repo**

**What comes next:**
- Days 8–30: document ingestion (PDF / OCR), chunking, embeddings, vector search
- Days 31–60: RAG Q&A + structured extraction with evals (retrieval accuracy first, prompt second)
- Days 61–90: deploy on Azure, Databricks Gen AI cert, apply to Calgary energy-tech AI roles

## Run it

```bash
# local
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.app.main:app --reload

# docker
docker build -t land-doc-intelligence .
docker run -p 8000:8000 land-doc-intelligence
```

Then visit http://localhost:8000/health — expect `{"status": "ok"}`.

## Run tests

```bash
pytest -q
```

## Stack

Python 3.11, FastAPI, Uvicorn, Docker, pytest, httpx

## Data note

All documents in `data/samples/` are synthetic examples written for this project. Do not add real agreements, leases, or personal data here.
