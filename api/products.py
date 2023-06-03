from fastapi import APIRouter

from schemas.products import Product, CreateProduct, ChangeProduct, DeleteProduct

from services.products import products_service

router = APIRouter()

# GET
# get_product
@router.get(
  "/api/products/product/{id}",
  status_code=200,
  response_model=Product
)
def get_product(id: str):
  return products_service.get_product(id)

# get_products
@router.get(
  "/api/products/",
  status_code=200,
  response_model=list[Product]
)
def get_products():
  return products_service.get_products()

# filter_products_by_substr
@router.get(
  "/api/products/filter_products_by_substr/{substr}",
  status_code=200,
  response_model=list[Product]
)
def filter_products_by_substr(substr: str):
  return products_service.filter_products_by_substr(substr)

# POST
# create_product
@router.post(
  "/api/products/create",
  status_code=200,
  response_model=str
)
def create_product(data: CreateProduct) -> str:
  return products_service.create_product(data)

# PUT
# change_product
@router.put(
  "/api/products/change",
  status_code=200,
  response_model=str
)
def change_product(data: ChangeProduct) -> str:
  return products_service.change_product(data)

# DELETE
# delete_product
@router.delete(
  "/api/products/delete",
  status_code=200,
  response_model=str
)
def delete_product(data: DeleteProduct) -> str:
  return products_service.delete_product(data)