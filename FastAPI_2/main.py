from fastapi import FastAPI, Query

# let import Enum
from enum import Enum

# let import BaseModel from Pydantic
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# @app.post("/items/")
# async def create_item(item: Item):
#     return item 

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        item_dict.update({"price_with_tax" : item.price + item.tax})
    return item_dict

# let try path parameter with post request
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     result = {"iterm_id" : item_id, **item.dict()}
#     return result

# let try path and query parameter and request body
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"iterm_id" : item_id, **item.dict()}
    if q:
        result.update({"q" : q})
    return result

## Query Parameters and string Validations

## using Query()

# @app.get("/books")
# async def get_book(q: str | None = None):
#     result = {"books" : [{"maths":"class 1"}, {"english":"class 4"}]}
#     if q:
#         result.update({"q":q})
#     return result

# let do the same using Query()
@app.get("/books")
async def get_book(q: str | None = Query(None, max_length=4)):
    result = {"books" : [{"maths":"class 1"}, {"english":"class 4"}]}
    if q:
        result.update({"q":q})
    return result
## we add min, title, description etc to the query 

#to have a list as the query value
@app.get("/books_list")
async def get_book(q: list[str] | None = Query(None, max_length=4)):
    result = {"books" : [{"maths":"class 1"}, {"english":"class 4"}]}
    if q:
        result.update({"q":q})
    return result

# we can make it not to have a default value thus to make it a required one
@app.get("/book")
async def get_book(q: str = Query(..., max_length=4)):
    result = {"books" : [{"maths":"class 1"}, {"english":"class 4"}]}
    if q:
        result.update({"q":q})
    return result

# hide a query
@app.get("/book_hide")
async def get_book(q: str | None = Query(None, include_in_schema=False)):
    result = {"books" : [{"maths":"class 1"}, {"english":"class 4"}]}
    if q:
        result.update({"q":q})
    return result