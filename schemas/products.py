from pydantic import BaseModel

from schemas.users import TokenAuth

class Product(BaseModel):
  id: str
  name: str
  description: str
  price: int
  image: str

class CreateProduct(BaseModel):
  name: str
  description: str
  price: int
  image: str
  admin: TokenAuth

class ChangeProduct(BaseModel):
  id: str
  name: str
  description: str
  price: int
  image: str
  admin: TokenAuth

class DeleteProduct(BaseModel):
  id: str
  admin: TokenAuth