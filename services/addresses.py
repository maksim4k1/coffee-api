from fastapi import HTTPException
from uuid import uuid4

from schemas.addresses import Address, CreateAddress, ChangeAddress, DeleteAddress
from schemas.users import User, TokenAuth

from db.addresses import find_address, get_addresses, add_address, change_address, delete_address

from services.users import users_service

class AddresssService:
  def get_address(self, id: str) -> Address:
    address: Address = find_address(id)
    if address == None:
      raise HTTPException(status_code=404, detail="Адрес не найден")
    return address

  def get_addresses(self) -> list[Address]:
    addresses: list[Address] = get_addresses()
    return addresses

  def create_address(self, data: CreateAddress) -> str:
    user: User = users_service._token_auth(TokenAuth(token=data.admin.token))
    if user == None: raise HTTPException(status_code=404, detail="Пользователь не найден")
    if users_service._check_admin(user) == False: raise HTTPException(status_code=403, detail="Вы не можете выполнить это действие")

    new_address: Address = Address(
      id=str(uuid4()),
      address=data.address,
      description=data.description,
      phone=data.phone,
      image=data.image
    )

    add_address(new_address)
    return new_address.id

  def change_address(self, data: ChangeAddress) -> str:
    user: User = users_service._token_auth(TokenAuth(token=data.admin.token))
    if user == None: raise HTTPException(status_code=404, detail="Пользователь не найден")
    if users_service._check_admin(user) == False: raise HTTPException(status_code=403, detail="Вы не можете выполнить это действие")

    address: Address = find_address(data.id)
    if address == None: raise HTTPException(status_code=404, detail="Адрес не найден")

    address.address = data.address
    address.description = data.description
    address.phone = data.phone
    address.image = data.image

    change_address(address)
    return data.id

  def delete_address(self, data: DeleteAddress) -> str:
    user: User = users_service._token_auth(TokenAuth(token=data.admin.token))
    if user == None: raise HTTPException(status_code=404, detail="Пользователь не найден")
    if users_service._check_admin(user) == False: raise HTTPException(status_code=403, detail="Вы не можете выполнить это действие")

    address: Address = find_address(data.id)
    if address == None: raise HTTPException(status_code=404, detail="Адрес не найден")

    delete_address(data.id)
    return data.id

addresses_service: AddresssService = AddresssService()