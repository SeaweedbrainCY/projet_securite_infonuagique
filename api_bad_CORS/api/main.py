
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Item(BaseModel):
    dest: str
    amount: int 


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/account/money")
async def get_money():
    with open("money.txt", "r") as f:
        money = f.read()
    return {"amount": int(money), "currency": "CAD"}

@app.post("/account/transfert")
async def transfert_money(item: Item):
    dest = item.dest
    amount = item.amount
    with open("money.txt", "r") as f:
        money = f.read()
    if int(money) < amount:
        return {"status":"not_enough", "remaing_amout": int(money), "currency": "CAD"}
    money = int(money) - amount
    with open("money.txt", "w") as f:
        f.write(str(money))
    return {"status":"success", "remaing_amout": int(money), "currency": "CAD"}