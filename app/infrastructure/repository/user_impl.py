from app.domain.user.repository import UserRepository
from app.infrastructure.database.mappers import UserMapper
from app.domain.user.entity import User
from app.domain.shared.vo import UserID
from app.infrastructure.database.orm_models import UserORM
from typing import Optional

class UserRepositoryImpl(UserRepository):
    '''
    用户仓库实现类
    '''
    async def save(self, user: User) -> User:
        user_orm =  UserMapper.to_orm(user)
        await user_orm.save()
        return UserMapper.to_entity(user_orm)
    async def find_by_id(self, user_id: UserID) -> User | None:
        user_orm = await UserORM.get_or_none(id=user_id.value)
        if user_orm:
            return UserMapper.to_entity(user_orm)
        return None
    async def find_by_username(self, username):
        user_orm = await UserORM.get_or_none(username=username)
        if user_orm:
            return UserMapper.to_entity(user_orm)
        return None
    async def exists_by_username(self, username: str) -> bool:
        return await UserORM.filter(username = username).exists()
    async def delete(self, user: User) -> bool:
        count = (await UserORM.filter(id=user.id.value)).delete()
        return count > 0
    async def find_all(self) -> list[User]:
        user_orms = await UserORM.all()
        return [UserMapper.to_entity(user_orm) for user_orm in user_orms]
    async def create_user(self, username: str, password: str) -> User:
        user = User(id = None,username=username, password=password)
        return user
    async def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        return raw_password == hashed_password