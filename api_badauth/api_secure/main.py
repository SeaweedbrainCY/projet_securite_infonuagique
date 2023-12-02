from fastapi import FastAPI, Depends, HTTPException, Header
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

SECRET_KEY = "ungrandsecret"
ALGORITHM = ['HS256']
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database to store user information (in-memory for simplicity)
fake_users_db = [{"username": "root", "password": "root"}]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM[0])
    return encoded_jwt


async def get_current_user(sessionID: str = Header(..., convert_underscores=False)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(sessionID, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        raise credentials_exception


#OK ça marche
@app.post("/token", response_model=dict)
async def login(username: str, password: str):
    # Verify username and password (not shown for simplicity)
    if any(user["username"] == username for user in fake_users_db):
        # Assume verification is successful, create a token
        token = create_token({"sub": username, "admin": False})
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Username doesn't exist")

#OK ça marche
@app.post("/register", response_model=dict)
async def register(username: str, password: str):

    # Check if the username is already taken
    if any(user["username"] == username for user in fake_users_db):
        raise HTTPException(status_code=400, detail="Username already registered")

    # Register the new user
    fake_users_db.append({"username": username, "password": password})
    return {"message": "User registered successfully"}

@app.get("/protected_resource", response_model=dict)
async def get_protected_resource(current_user: dict = Depends(get_current_user)):
    if current_user.get("admin", True):
        return {"message": "This is a protected resource", "user": current_user}
    else:
        raise HTTPException(status_code=403, detail="You do not have permission to access this resource")