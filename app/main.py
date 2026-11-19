from fastapi import FastAPI

app = FastAPI(title="Release Loop")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"item-{item_id}"}
