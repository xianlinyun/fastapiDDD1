'''
OEM 模型
'''
from typing import Dict
from tortoise import fields
from tortoise.models import Model

class UserORM(Model):
    '''
    用户模型
    '''
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"
