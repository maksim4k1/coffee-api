from fastapi import APIRouter

from schemas.addresses import Address, CreateAddress, ChangeAddress, DeleteAddress

from services.addresses import addresses_service

router = APIRouter()

# GET
# get_address
@router.get(
  "/api/addresses/address/{id}",
  status_code=200,
  response_model=Address
)
def get_address(id: str):
  return addresses_service.get_address(id)

# get_addresses
@router.get(
  "/api/addresses/",
  status_code=200,
  response_model=list[Address]
)
def get_addresses():
  return addresses_service.get_addresses()

# POST
# create_address
@router.post(
  "/api/addresses/create",
  status_code=200,
  response_model=str
)
def create_address(data: CreateAddress) -> str:
  return addresses_service.create_address(data)

# PUT
# change_address
@router.put(
  "/api/addresses/change",
  status_code=200,
  response_model=str
)
def change_address(data: ChangeAddress) -> str:
  return addresses_service.change_address(data)

# DELETE
# delete_address
@router.delete(
  "/api/addresses/delete",
  status_code=200,
  response_model=str
)
def delete_address(data: DeleteAddress) -> str:
  return addresses_service.delete_address(data)