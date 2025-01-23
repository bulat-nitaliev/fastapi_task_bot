from fastapi import APIRouter
from .products.views import router as product_router
from .subscribe.views import router as subscribe_router

router = APIRouter()
router.include_router(router=product_router, prefix='/product')
router.include_router(router=subscribe_router, prefix='/subscribe')
