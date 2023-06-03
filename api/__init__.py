from fastapi import APIRouter

from api.users import router as users_router
from api.products import router as products_router
from api.addresses import router as addresses_router

router = APIRouter()
router.include_router(users_router)
router.include_router(products_router)
router.include_router(addresses_router)