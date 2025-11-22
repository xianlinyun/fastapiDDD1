from typing import Dict
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
'''
应用程序配置文件
'''
class Settings(BaseSettings):
    '''
    应用配置类
    '''
    app_name: str = "FastAPI DDD"
    app_version: str = "0.0.1"
    debug: bool = True
    secret_key: str = "your_secret_key"
    # database_url: str = "mysql://root:zhy220010@192.168.88.128:3306/fastapi"
    database_url: str = "postgres://root:zhy220010@192.168.88.129:5432/fastapi"
    model_config = ConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8")
    TORTOISE_ORM: Dict = {
    "connections": {
        # 开发环境使用 SQLite（基于文件，无需服务器）
        # "default": "sqlite://db.sqlite3",
        # 生产环境示例：PostgreSQL
        # "default": "postgres://user:password@localhost:5432/dbname",
        # 生产环境示例：MySQL
        "default":database_url,
    },
    "apps": {
        "models": {
            "models": ["app.infrastructure.database.orm_models","aerich.models"],  # 模型模块和 Aerich 迁移模型
            "default_connection": "default",
        }
    },
    # 连接池配置（推荐）
    "use_tz": False,  # 是否使用时区
    "timezone": "UTC",  # 默认时区
    "db_pool": {
        "max_size": 10,  # 最大连接数
        "min_size": 1,   # 最小连接数
        "idle_timeout": 30  # 空闲连接超时（秒）
    }
}
settings = Settings()
TORTOISE_ORM = settings.TORTOISE_ORM
if __name__ == "__main__":
    print(settings.app_name)