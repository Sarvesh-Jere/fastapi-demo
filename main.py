from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Define what an Item looks like
class Item(BaseModel):
    text: str = None
    is_done: bool = False


# Temporary in-memory storage
items = []


@app.get("/")
def root():
    return {"message": "Hello Sarvesh, FastAPI is running on your Mac!"}


# Create a new item
@app.post("/items", response_model=list[Item])
def create_item(item: Item):
    items.append(item)
    return items


# List all items (up to a limit)
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]


#  Get a single item by its index (ID)
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
