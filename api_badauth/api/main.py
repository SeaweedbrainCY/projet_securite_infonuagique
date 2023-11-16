from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuration de CORS pour permettre les requêtes depuis n'importe quel origine
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database to store user information (in-memory for simplicity)
fake_users_db = [{"username": "root", "password": "root"}]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception


@app.post("/token", response_model=dict)
async def login(username: str, password: str):
    # Verify username and password (not shown for simplicity)
    if any(user["username"] == username for user in fake_users_db):
        # Assume verification is successful, create a token
        token = create_token({"sub": username, "admin": False})
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Username doesn't exist")


@app.post("/register", response_model=dict)
async def register(username: str, password: str):

    # Check if the username is already taken
    if any(user["username"] == username for user in fake_users_db):
        raise HTTPException(status_code=400, detail="Username already registered")

    # Register the new user
    fake_users_db.append({"username": username, "password": password})
    return {"message": "User registered successfully"}
