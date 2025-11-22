from dataclasses import dataclass
from typing import Optional, List
from app.domain.user.repository import UserRepository

@dataclass
class GetOrdersQuery:
    '''
    获取用户订单查询
    '''
    user_id: int
    limit: Optional[int] = 10
    offset: Optional[int] = 0
@dataclass
class OrderDTO:
    '''
    订单数据传输对象
    '''
    id: int
    order_number: str
    total_amount: float
    created_at: str
    updated_at: str
@dataclass
class GetOrdersResult:
    '''
    获取用户订单结果
    '''
    orders: List[OrderDTO]
    total : int
class GetOrdersHandler:
    '''
    获取用户订单查询处理器
    '''
    def __init__(self, user_repository: UserRepository):# 从领域层注入用户仓库,需要在基础设施层实现该接口
        # self.user_repository = user_repository
        pass
    async def handle(self, query: GetOrdersQuery) -> GetOrdersResult:
        '''
        处理获取用户订单查询
        '''
        if query.user_id <= 0:
            raise ValueError("无效的用户ID")
        if query.limit>100 or  query.limit <= 0:
            raise ValueError("无效的限制参数")
        if query.offset < 0:
            raise ValueError("无效的偏移参数")
        # 这里假设有一个方法可以获取订单数据，实际实现中需要调用相应的仓库方法
        # 由于订单相关的实现不在当前上下文中，这里仅做示例
        orders = [
            OrderDTO(id=1, order_number="ORD123", total_amount=100.0, created_at="2024-01-01", updated_at="2024-01-02"),
            OrderDTO(id=2, order_number="ORD124", total_amount=150.0, created_at="2024-01-03", updated_at="2024-01-04"),
        ]
        # 应用分页
        orders = orders[query.offset or 0:query.offset + query.limit or 2]
        return GetOrdersResult(orders=orders, total=len(orders))