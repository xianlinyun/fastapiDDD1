'''
认证和用户管理路由
'''
from fastapi import APIRouter,Depends,status,HTTPException
from pydantic import BaseModel
from app.application.user.commands.register_user import RegisterUserResult

from app.interface.api.dependency import get_user_repository_handler, get_login_user_handler
from app.application.user.commands.register_user import  RegisterUserCommand, RegisterUserHandler
from app.application.user.commands.login_user import LoginUserCommand, LoginUserHandler
from app.application.common.exception import DomainException
router = APIRouter(
    prefix="/auth",tags=["认证与用户管理"]
)
class RegisterRequest(BaseModel):
    '''注册请求模型'''
    username: str
    password: str
class RegisterResponse(BaseModel):
    '''注册响应模型'''
    user_id: int 
    username: str
    message: str
class LoginRequest(BaseModel):
    '''登录请求模型'''
    username: str
    password: str
class LoginResponse(BaseModel):
    '''登录响应模型'''
    user_id: int
    username: str
    message: str
@router.post("/register",response_model=RegisterResponse,status_code=status.HTTP_201_CREATED)
async def register_user(request: RegisterRequest,
                        handler:RegisterUserHandler=Depends(get_user_repository_handler)):# 依赖领域层获取用户注册处理器实例
    '''用户注册接口'''
    try:
        command = RegisterUserCommand(
            username=request.username,
            password=request.password
        )
        result:RegisterUserResult = await handler.handle(command)
        return RegisterResponse(
            user_id=result.user_id,
            username=result.username,
            message="用户注册成功"
        )
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
@router.post("/login",response_model=LoginResponse,status_code=status.HTTP_200_OK)
async def login_user(request: LoginRequest,
                     handler:LoginUserHandler=Depends(get_login_user_handler)):# 依赖领域层获取用户登录处理器实例
    '''用户登录接口'''
    try:
        command = LoginUserCommand(
            username=request.username,
            password=request.password
        )
        result = await handler.handle(command)
        return LoginResponse(
            user_id=result.user_id,
            username=result.username,
            message="用户登录成功"
        )
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
@router.get("/all",status_code=status.HTTP_200_OK)   
async def get_all_users(handler:RegisterUserHandler=Depends(get_user_repository_handler)):
    '''获取所有用户接口'''
    try:
        users = await handler.user_repository.find_all()
        return [{"user_id": user.id.value if user.id else None, "username": user.username} for user in users]
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="服务器内部错误")