from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()

class order_by(str,Enum):
    asc = "asc"
    desc = "desc"


@app.get("/")
def greet():
    return {"message":"welcome"}

# aikahne optional er value None na pathale api mone korbe value nai error dibe , order optional dile aivabe dite hbe ?order=something , na dile auto None jabe mane null
# aita holo jkono kichu query te deya jabe mane fixed kichu nai 
# @app.get("/item/all")
# async def all_item(order : Optional[str] = None):
#     return {"order":"this is the order","order":order}

# aita holo same ager tar moto but order er value fixed Enum use kore 
@app.get("/item/all")
async def all_item(order : order_by = None):
    return {"order":"this is the order","order":order}

# ## duyamic path k niche rakhte hbe nahoi er niche same static path asle kaj korbe na, fastapi er default behaviour aita serially execute kore api
@app.get("/item/{id}")
async def item(id:int):
    return {"item":f'the number of item is {id}'}