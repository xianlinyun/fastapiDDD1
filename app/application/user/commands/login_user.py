from dataclasses import dataclass
from typing import Optional
from app.application.common.exception import ValidationException, AuthenticationException
from app.domain.user.repository import UserRepository

@dataclass
class LoginUserCommand:
    '''
    注册用户命令
    '''
    username: str
    password: str
@dataclass
class LoginUserResult:
    '''
    注册用户结果
    '''
    user_id: Optional[int]
    username : str
class LoginUserHandler:
    """
    注册用户命令处理器
    """
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    async def handle(self, command: LoginUserCommand) -> LoginUserResult:
        '''
        处理注册用户命令
        '''
        if not command.username  or not command.username.strip():
            raise ValidationException("用户名不能为空")
        if not command.password or not command.password.strip():
            raise ValidationException("密码不能为空")
        user = await self.user_repository.find_by_username(command.username)
        if not user:
            raise AuthenticationException("用户名或密码错误")
        # if not await user.verify_password(command.password, user.password):
        #     raise ValueError("用户名或密码错误")
        if not await self.user_repository.verify_password(command.password, user.password):
            raise AuthenticationException("用户名或密码错误")
        return LoginUserResult(user_id=user.id.value if user.id else None,
                               username=user.username)
        
    