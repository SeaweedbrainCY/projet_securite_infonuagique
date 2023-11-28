from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
import os
import requests
import socket
from urllib.parse import urlparse
import ipaddress


origins = [
        "http://image-download.local:4200", 
        "http://ssrf.demo.stchepinsky.net"
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
async def fetch(url:str):
    img = requests.get(url)
    if img.status_code != 200:
        raise HTTPException(status_code=404, detail="Image not found")
    return Response(content=img.content)

@app.get("/samisafe/fetch/image")
async def fetch_samisafe(url:str):
    # refuse all private ip :
    private_ip_startwith = ["10.", "172.16.", "192.168.", "127.", "169.254.", "100.64."]
    if private_ip_startwith in url:
        raise HTTPException(status_code=403, detail="Private IP not allowed")
    img = requests.get(url)
    if img.status_code != 200:
        raise HTTPException(status_code=404, detail="Image not found")
    return Response(content=img.content)
        


@app.get("/safe/fetch/image")
async def fetch_safe(url:str):
    try:
        hostname = urlparse(url).hostname
    except Exception as e:
        print("Exception: ", e)
        raise HTTPException(status_code=404, detail="Image not found")
    print("hostname: ", hostname)
    if hostname is None:
        raise HTTPException(status_code=404, detail="Image not found")
    ip = socket.gethostbyname(hostname)
    print("ip: ", ip)
    if ipaddress.ip_address(ip).is_private:
        print("Private IP not allowed")
        raise HTTPException(status_code=403, detail="Private IP not allowed")
    img = requests.get(url, allow_redirects=False)
    if img.headers["Content-Type"] != "image/png" and img.headers["Content-Type"] != "image/jpeg" and img.headers["Content-Type"] != "image/gif" and img.headers["Content-Type"] != "image/webp" and img.header["Content-Type"] != "image/mp4":
        print("Not an image extension")
        raise HTTPException(status_code=404, detail="Image not found")
    if img.status_code != 200:
        print("Image not found")
        raise HTTPException(status_code=404, detail="Image not found")
    return Response(content=img.content, media_type="image/png")
    

    

