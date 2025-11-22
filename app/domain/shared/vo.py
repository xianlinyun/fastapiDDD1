'''
共享值对象（VO）定义
'''
from dataclasses import dataclass # dataclass会自动生成初始化方法等frozen=True表示不可变

@dataclass(frozen=True)
class UserID:
    '''
    用户ID值对象
    '''
    value: int
    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("UserID must be a positive integer")