from typing import Optional
from cassandra.cqlengine.management import sync_table # Used for syncing the database in the main file

from app.users.models import User
from fastapi import FastAPI
from pydantic import BaseModel

# Used for the config on env variables
from . import config,db
# settings = config.get_settings()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()
settings = config.get_settings()


#sync table has to be in the place where fastAPI starts

@app.on_event('startup')
def on_startup():
    # triggered when fastapi starts
    print('hello')
    db.get_session


# uvicorn <filename:<appName>

# @app.post("/items/")
# async def create_item(item: Item):
#     return item

@app.get("/")
def homepage():
    return {"data" : "hello",'keyspace_name':settings.keyspace} # Can pass JSON or HTML content
    # Is always RESTApi first

# An API endpoint to get all the user

@app.get("/users")
def user_list_view():
    q = User.objects.all().limit(10)
    return list(q)