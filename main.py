from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import FastAPI
from databases import books


class Books(BaseModel):
    name: str
    author: str
    genre: str
    price: float
    ebook: bool
    status: Optional[str] = None


app = FastAPI()


@app.get("/")
def get_all_books():
    return f"here is all the books"
