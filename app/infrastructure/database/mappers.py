'''
实体与ORM模型之间的映射器
'''
from app.infrastructure.database.orm_models import UserORM
from app.domain.user.entity import User
from app.domain.shared.vo import UserID
class UserMapper:
    @staticmethod
    def to_entity(orm_model:UserORM):
        '''
        将ORM模型转换为实体对象
        '''
        user = User(
            id=UserID(orm_model.id) if orm_model.id else None,
            username=orm_model.username,
            password=orm_model.password
        )
        return user
    @staticmethod
    def to_orm(user:User) -> UserORM:
        '''
        将实体对象转换为ORM模型
        '''
        orm_model = UserORM()
        if user.id:
            orm_model.id = user.id.value
        orm_model.username = user.username
        orm_model.password = user.password
        return orm_model