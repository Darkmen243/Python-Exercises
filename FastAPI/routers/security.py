from fastapi import APIRouter, Header, status
from fastapi.responses import JSONResponse
import uuid

router = APIRouter()

tokens = set()

#creates a token
@router.get("/login/")
def login():
    token = str(uuid.uuid4())
    tokens.add(token)
    return {"message": "You are authenticated"}

def unauthorized():
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        content={"message": "Пользователь не найден"}
    )
         
@router.get("/profile")
def root(header: str = Header()):
    if header:
        if header.startswith("Bearer "):
            token = header.split(" ")
            token = token[1]
            print(token)
            if token in tokens:
                return token
            else:
                return unauthorized()
        else:    
            return unauthorized()
    else:
        return unauthorized()