from dataclasses import dataclass # dataclass会自动生成初始化方法等frozen=True表示不可变
from typing import Optional
from app.domain.shared.vo import UserID

@dataclass
class User:
    '''
    用户实体类
    '''
    id: Optional[UserID]
    username: str
    password: str

    def __post_init__(self):
        if not self.username:
            raise ValueError("Username cannot be empty")
        if not self.password:
            raise ValueError("Password cannot be empty")
    def verify_password(self, password: str) -> bool:
        '''
        验证用户密码
        '''
        return self.password == password
    def change_password(self, new_password: str):
        '''
        修改用户密码
        '''
        if not new_password:
            raise ValueError("New password cannot be empty")
    