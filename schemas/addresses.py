from pydantic import BaseModel

from schemas.users import TokenAuth

class WorkTime(BaseModel):
  start: int
  end: int

class Address(BaseModel):
  id: str
  address: str
  description: str
  image: str
  phone: str

class CreateAddress(BaseModel):
  address: str
  description: str
  image: str
  phone: str
  admin: TokenAuth

class ChangeAddress(BaseModel):
  id: str
  address: str
  description: str
  image: str
  phone: str
  admin: TokenAuth

class DeleteAddress(BaseModel):
  id: str
  admin: TokenAuth