
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/account/money")
async def get_money():
    with open("money.txt", "r") as f:
        money = f.read()
    return {"amount": int(money), "currency": "CAD"}

@app.post("/account/transfert")
async def transfert_money(dest: str, amount: int):
    with open("money.txt", "r") as f:
        money = f.read()
    if int(money) < amount:
        raise HTTPException(status_code=403, detail="Not enough money")
    money = int(money) - amount
    with open("money.txt", "w") as f:
        f.write(str(money))
    return {"status":"success", "remaiing_amout": int(money), "currency": "CAD"}