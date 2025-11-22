'''
fastapi DDD 应用入口
'''
from fastapi import FastAPI
from app.interface.api.v1.auth_router import router as auth_router
from app.interface.api.v1.order_router import router as order_router
from config.setting import settings
from tortoise import Tortoise
from contextlib import asynccontextmanager
async def init_database():
    '''
    初始化数据库连接
    '''
    await Tortoise.init(
        db_url=settings.database_url,
        modules={'models': ['app.infrastructure.database.orm_models']}
    )
    await Tortoise.generate_schemas()
async def close_database():
    '''
    关闭数据库连接
    '''
    await Tortoise.close_connections()
@asynccontextmanager
async def lifespan(app: FastAPI):
    '''
    应用生命周期管理
    '''
    await init_database()
    yield
    await close_database()

def create_app() -> FastAPI:
    '''
    创建 FastAPI 应用实例
    '''
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
        lifespan=lifespan
    )

    app.include_router(auth_router)
    app.include_router(order_router)
    return app

app = create_app()
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI DDD Application","version": settings.app_version}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=settings.debug)