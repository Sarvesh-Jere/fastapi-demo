from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

BOOKS = []

@app.get("/{name}")
def read_api(name: str):
    return {'Welcome': name}

@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book

@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    for index, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            BOOKS[index] = book
            return book

    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    for index, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            del BOOKS[index]
            return {"message": "Book deleted"}

    raise HTTPException(status_code=404, detail="Book not found")
