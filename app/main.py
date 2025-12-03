from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Backend",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!"}

@app.get("/healthz")
def health():
    return {"status": "ok"}
