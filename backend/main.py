from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from utils.dummy import dummy_data
from todo.router import router as todo_router

from pydantic import BaseModel
from typing import List


# backend run - fastapi dev main.py
# ?frontend run - pnpm dev 




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers = ["*"],
    allow_credentials = True 
)

class Todo(BaseModel):
    id:int
    title:str
    description:str
    completed:bool

app.include_router(todo_router)

@app.get("/",response_model=List[Todo],summary="This route takes noting , this is for docs purpose , there are no fucntion name in the docs ")
async def root():
    """
    this is for description like what this route takes
    - there are no query parameter just get all tasks
    """
    return dummy_data

