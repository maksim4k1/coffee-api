from sqlalchemy import create_engine, Column, Integer, String, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from schemas.addresses import Address

Base = declarative_base()

class TableAddress(Base):
  __tablename__ = "addresses"

  id=Column("id", String, primary_key=True)
  address=Column("address", String)
  description=Column("description", String)
  image=Column("image", String)
  phone=Column("phone", String)

  def __init__(self, id, address, description, image, phone):
    self.id=id
    self.address=address
    self.description=description
    self.image=image
    self.phone=phone

engine = create_engine("sqlite:///db/db/addresses.db")
Base.metadata.create_all(bind=engine)

session = sessionmaker(bind=engine)()

def convert_to_address(address: TableAddress) -> Address:
  return Address(
    id=address.id,
    address=address.address,
    description=address.description,
    image=address.image,
    phone=address.phone
  )

def convert_to_table_address(address: Address) -> TableAddress:
  return TableAddress(
    id=address.id,
    address=address.address,
    description=address.description,
    image=address.image,
    phone=address.phone
  )

def find_address(address_id: str) -> Address:
  query = session.query(TableAddress).get(address_id)
  if query == None: return None
  return convert_to_address(query)

def get_addresses() -> list[Address]:
  query = session.query(TableAddress).all()
  addresses: list[Address] = []
  for address in query:
    if address != None: addresses.append(convert_to_address(address))
  return addresses

def add_address(address: Address) -> Address:
  session.add(convert_to_table_address(address))
  session.commit()
  return address

def change_address(address: Address) -> Address:
  query = session.query(TableAddress).get(address.id)
  if query == None: return None
  query.address = address.address
  query.description = address.description
  query.phone = address.phone
  query.image = address.image

  session.commit()
  return address

def delete_address(address_id: str) -> str:
  query = session.query(TableAddress).get(address_id)
  if query == None: return None
  session.delete(query)

  session.commit()
  return address_id