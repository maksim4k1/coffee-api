from fastapi import HTTPException
from uuid import uuid4

from schemas.products import Product, CreateProduct, ChangeProduct, DeleteProduct
from schemas.users import User, TokenAuth

from db.products import find_product, filter_products_by_substr, get_products, add_product, change_product, delete_product

from services.users import users_service

class ProductsService:
  def get_product(self, id: str) -> Product:
    product: Product = find_product(id)
    if product == None:
      raise HTTPException(status_code=404, detail="Такого продукта не было найдено")
    return product

  def get_products(self) -> list[Product]:
    products: list[Product] = get_products()
    return products

  def filter_products_by_substr(self, substr: str) -> list[Product]:
    products: list[Product] = filter_products_by_substr(substr)
    return products

  def create_product(self, data: CreateProduct) -> str:
    user: User = users_service._token_auth(TokenAuth(token=data.admin.token))
    if user == None: raise HTTPException(status_code=404, detail="Пользователь не найден")
    if users_service._check_admin(user) == False: raise HTTPException(status_code=403, detail="Вы не можете выполнить это действие")

    new_product: Product = Product(
      id=str(uuid4()),
      name=data.name,
      description=data.description,
      price=data.price,
      image=data.image
    )

    add_product(new_product)
    return new_product.id

  def change_product(self, data: ChangeProduct) -> str:
    user: User = users_service._token_auth(TokenAuth(token=data.admin.token))
    if user == None: raise HTTPException(status_code=404, detail="Пользователь не найден")
    if users_service._check_admin(user) == False: raise HTTPException(status_code=403, detail="Вы не можете выполнить это действие")

    product: Product = find_product(data.id)
    if product == None: raise HTTPException(status_code=404, detail="Продукт не найден")

    product.name = data.name
    product.description = data.description
    product.price = data.price
    product.image = data.image

    change_product(product)
    return data.id

  def delete_product(self, data: DeleteProduct) -> str:
    user: User = users_service._token_auth(TokenAuth(token=data.admin.token))
    if user == None: raise HTTPException(status_code=404, detail="Пользователь не найден")
    if users_service._check_admin(user) == False: raise HTTPException(status_code=403, detail="Вы не можете выполнить это действие")

    product: Product = find_product(data.id)
    if product == None: raise HTTPException(status_code=404, detail="Продукт не найден")

    delete_product(data.id)
    return data.id

products_service: ProductsService = ProductsService()