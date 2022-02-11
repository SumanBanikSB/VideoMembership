from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

# uvicorn <filename:<appName>

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/")
def homepage():
    return {"data" : "hello"} # Can pass JSON or HTML content
    # Is always RESTApi first