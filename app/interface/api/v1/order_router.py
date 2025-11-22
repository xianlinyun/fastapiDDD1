from app.application.common.exception import DomainException
from pydantic import BaseModel
from fastapi import APIRouter,Depends, Query,status,HTTPException
from app.interface.api.dependency import get_get_orders_handler
from app.application.user.queries.get_orders import GetOrdersQuery
from app.application.user.queries.get_orders import GetOrdersHandler
router = APIRouter(
    prefix="/orders",tags=["订单管理"])
class OrderResponse(BaseModel):
    '''订单响应模型'''
    id: int
    order_number: str
    total_amount: float
    created_at: str
    updated_at: str
class GetOrdersResponse(BaseModel):
    '''获取用户订单响应模型'''
    orders: list[OrderResponse]
    total: int
    limit: int
    offset: int
@router.get("/",response_model=GetOrdersResponse,status_code=status.HTTP_200_OK)
async def get_orders(
    user_id:int = Query(..., description="用户ID"),
    limit:int = Query(10, description="返回订单数量限制", le=100,ge=1),
    offset:int = Query(0, description="返回订单的偏移量", ge=0),
    handler: GetOrdersHandler = Depends(get_get_orders_handler)
    ):
    '''获取用户订单的接口'''
    try:
        query = GetOrdersQuery(
            user_id=user_id,
            limit=limit,
            offset=offset
        )
        result = await handler.handle(query)
        orders_response = [
            OrderResponse(
                id=order.id,
                order_number=order.order_number,
                total_amount=order.total_amount,
                created_at=order.created_at,
                updated_at=order.updated_at
            ) for order in result.orders
        ]
        return GetOrdersResponse(
            orders=orders_response,
            total=result.total,
            limit=limit or 10,
            offset=offset or 0
        )
    except DomainException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))