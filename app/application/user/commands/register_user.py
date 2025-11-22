from dataclasses import dataclass
from typing import Optional

from app.application.common.exception import ValidationException,DuplicateResourceException
from app.domain.user.repository import UserRepository

@dataclass
class RegisterUserCommand:
    '''
    注册用户命令
    '''
    username: str
    password: str
@dataclass
class RegisterUserResult:
    '''
    注册用户结果
    '''
    user_id: Optional[int]
    username : str
class RegisterUserHandler:
    """
    注册用户命令处理器
    """
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository 
    async def handle(self, command: RegisterUserCommand) -> RegisterUserResult:
        '''
        处理注册用户命令
        '''
        if not command.username  or not command.username.strip():
            raise ValidationException("用户名不能为空")
        if not command.password or not command.password.strip():
            raise ValidationException("密码不能为空")
        # 检查用户名是否已存在
        if await self.user_repository.exists_by_username(command.username):
            raise DuplicateResourceException("用户名已存在")
        # 创建用户实体
        user = await self.user_repository.create_user(command.username, command.password)
        # 保存用户实体
        saved_user = await self.user_repository.save(user)
        return RegisterUserResult(user_id=saved_user.id.value if saved_user.id else None,
                                  username=saved_user.username)
         