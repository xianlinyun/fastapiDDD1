'''
用户仓库模块
'''
from abc import ABC, abstractmethod
from .entity import User
from ..shared.vo import UserID
from typing import Optional
class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> User:
        '''保存用户实体'''
        pass
    @abstractmethod
    async def find_by_id(self, user_id: UserID) -> Optional[User]:
        '''根据用户ID查找用户实体'''
        pass
    @abstractmethod
    async def find_by_username(self, username: str) -> Optional[User]:
        '''根据用户名查找用户实体'''
        pass
    @abstractmethod
    async def exists_by_username(self, username: str) -> bool:
        '''检查用户名是否存在'''
        pass
    @abstractmethod
    async def delete(self, user: User) -> bool:
        '''删除用户实体'''
        pass
    @abstractmethod
    async def find_all(self) -> None:
        '''查找所有用户实体'''
        pass
    @abstractmethod
    async def create_user(self, username: str, password: str) -> User:
        '''创建新用户实体'''
        pass
    @abstractmethod
    async def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        '''验证密码是否匹配'''
        pass