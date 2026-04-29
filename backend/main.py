from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from utils.dummy import dummy_data
from todo.router import router as todo_router


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

app.include_router(todo_router)

@app.get("/")
async def root():
    return dummy_data

