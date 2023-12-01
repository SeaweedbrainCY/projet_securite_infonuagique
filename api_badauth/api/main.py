from fastapi import FastAPI, Depends, HTTPException, Header, Cookie, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()



origins = ["https://badauth.demo.stchepinsky.net"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "ungrandsecret"
ALGORITHM = ['HS256','None']
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database to store user information (in-memory for simplicity)
fake_users_db = [{"username": "root", "password": "root"}]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
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
        for algo in ALGORITHM:
            try:
                if algo != 'None':
                    payload = jwt.decode(sessionID, SECRET_KEY, algorithms=[algo])
                else:
                    print("Algo none for test only")
                    payload = jwt.decode(sessionID, SECRET_KEY, options={"verify_signature": False})
                return payload
            except JWTError:
                continue
    except JWTError:
        raise credentials_exception


@app.post("/api/token", response_model=dict)
async def login(username: str, password: str):
    # Verify username and password (not shown for simplicity)
    if any(user["username"] == username for user in fake_users_db):
        # Assume verification is successful, create a token
        token = create_token({"sub": username, "admin": False})

        response = JSONResponse(
            content={"access_token": token, "token_type": "bearer"},
            status_code=status.HTTP_200_OK,
        )
        # Set the cookie
        expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        expires_utc = expires.replace(tzinfo=timezone.utc)
        response.set_cookie(
            key="Authorization",
            value=f"Bearer {token}",
            expires=expires_utc,
            httponly=True,
            max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            secure=True,  # Set it to True if your app is served over HTTPS
            samesite="Lax",  # Set it to "Lax" or "Strict" if your app is served over HTTPS
            domain=".demo.stchepinsky.net",
        )

        return response
    else:
        raise HTTPException(status_code=400, detail="Username doesn't exist")
@app.post("/api/register", response_model=dict)
async def register(username: str, password: str):

    # Check if the username is already taken
    if any(user["username"] == username for user in fake_users_db):
        raise HTTPException(status_code=400, detail="Username already registered")

    # Register the new user
    fake_users_db.append({"username": username, "password": password})
    return {"message": "User registered successfully"}

@app.get("/api/protected_resource", response_model=dict)
async def get_protected_resource(current_user: dict = Depends(get_current_user)):
    print(current_user.get("admin", True))
    if current_user.get("admin", True):
        return {"message": "This is a protected resource", "user": current_user}
    else:
        raise HTTPException(status_code=403, detail="You do not have permission to access this resource")