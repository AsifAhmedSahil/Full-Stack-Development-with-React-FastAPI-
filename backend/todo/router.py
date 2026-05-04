from fastapi import APIRouter,Response,status
from utils.dummy import dummy_data,order_by
from typing import Optional
from .schema import Todo,Todo_request

router = APIRouter(
    prefix="/todo",
    tags=["todo"]
)


# aikahne optional er value None na pathale api mone korbe value nai error dibe , order optional dile aivabe dite hbe ?order=something , na dile auto None jabe mane null
# aita holo jkono kichu query te deya jabe mane fixed kichu nai 
# @app.get("/item/all")
# async def all_item(order : Optional[str] = None):
#     return {"order":"this is the order","order":order}

# aita holo same ager tar moto but order er value fixed Enum use kore 
@router.get("/item/all")
async def all_item(order : order_by = None):
    return {"order":"this is the order","order":order}

# ## duyamic path k niche rakhte hbe nahoi er niche same static path asle kaj korbe na, fastapi er default behaviour aita serially execute kore api
@router.get("/item/{id}")
async def item(id:int,response:Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND   
        return {"error":"item not found"}
    return {"item":f'the number of item is {id}'}


@router.post("/new_todo",response_model=Todo)
async def new_todo(todo:Todo_request):
    return {
        "id":420,
        # aikhane ** holo js er spread operator er moto kaj kore , r pydantic model use kroar karone aita automatic conversion kore na tai model_dump() use kora hoise.
        **todo.model_dump()
    }