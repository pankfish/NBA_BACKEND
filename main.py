from typing import Optional
from fastapi import FastAPI
from Player_Stats import Player
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"data": "man"}

@app.get("/player/")

async def get_player(first_name: str, last_name: str):
    print(first_name)
    return Player(first_name, last_name)

