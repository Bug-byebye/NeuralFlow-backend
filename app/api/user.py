from fastapi import APIRouter
from app.service import user_service
from pydantic import BaseModel

router = APIRouter(prefix="/user", tags=["用户管理"])

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(user: UserLogin):
    return await user_service.login_service(user.username, user.password)

@router.post("/register")
async def register(user: UserLogin):
    return await user_service.register_service(user.username, user.password)