from fastapi import FastAPI

app = FastAPI()


items = [
    {"id": 1, "name": "Apple 🍏"},
    {"id": 2, "name": "Orange 🍊"},
    {"id": 3, "name": "Pear 🍐"},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items(page: int, limit: int):
    return {"items": items,
            "page": page,
            "limit": limit}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}
