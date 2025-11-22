'''
依赖注入模块
'''
from fastapi import Depends

from app.domain.user.repository import UserRepository
from app.infrastructure.repository.user_impl import UserRepositoryImpl

from app.application.user.commands.register_user import RegisterUserHandler
from app.application.user.commands.login_user import LoginUserHandler
from app.application.user.queries.get_orders import GetOrdersHandler

def get_user_repository() -> UserRepository:
    '''获取用户仓库实例'''
    return UserRepositoryImpl()
def get_user_repository_handler(user_repository=Depends(get_user_repository)) -> RegisterUserHandler: # 获取用户注册处理器实例
    '''' 获取用户注册处理器实例'''
    return RegisterUserHandler(user_repository) # 返回处理器实例
def get_login_user_handler(user_repository=Depends(get_user_repository)) -> LoginUserHandler:
    '''获取用户登录处理器实例'''
    return LoginUserHandler(user_repository)
def get_get_orders_handler(user_repository=Depends(get_user_repository)) -> GetOrdersHandler:
    '''获取获取用户订单处理器实例'''
    return GetOrdersHandler(user_repository)
