from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
import os
import requests




origins = [
        "http://image-download.local:4200", 
        "https://image-download.demo.stchepinsky.net"
        ]

class Item(BaseModel):
    dest: str
    amount: int 


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/fetch/image")
async def get_money(url:str):
    img = requests.get(url)
    if img.status_code != 200:
        raise HTTPException(status_code=404, detail="Image not found")
    return Response(content=img.content)

