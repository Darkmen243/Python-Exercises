'''
Create FastAPI app with:

POST /user

GET /users

GET /users/{id}

Use Pydantic models.
'''
import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel, ConfigDict
from routers import security


app = FastAPI()

app.include_router(security.router)

class UserCreate(BaseModel):
    name: str

class UserRead(BaseModel):
    id: str
    name: str

Users = {}

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/user")
def create_user(user:UserCreate):
    user_id  = str(uuid.uuid4())
    new_user = {
        "id": user_id,
        "name": user.name
    }
    Users[user_id] = new_user
    return new_user
@app.get("/users")
def get_users():
    return Users
@app.get("/users/{id}", response_model=UserRead)
def get_user(id:str):
    user = Users.get(id)
    if not user:
           return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
    else:
        return user
