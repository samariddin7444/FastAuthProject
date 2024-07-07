from fastapi import APIRouter

order_routes = APIRouter(
    prefix="/order",
)


@order_routes.get("/")
async def get_order():
    return {"message": "order"}
