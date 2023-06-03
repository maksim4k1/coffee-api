from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from schemas.products import Product

Base = declarative_base()

class TableProduct(Base):
  __tablename__ = "products"

  id=Column("id", String, primary_key=True)
  name=Column("name", String)
  description=Column("description", String)
  price=Column("price", Integer)
  image=Column("image", String)

  def __init__(self, id, name, description, price, image):
    self.id=id
    self.name=name
    self.description=description
    self.price=price
    self.image=image

engine = create_engine("sqlite:///db/db/products.db")
Base.metadata.create_all(bind=engine)

session = sessionmaker(bind=engine)()

def convert_to_product(product: TableProduct) -> Product:
  return Product(
    id=product.id,
    name=product.name,
    description=product.description,
    price=product.price,
    image=product.image
  )

def convert_to_table_product(product: Product) -> TableProduct:
  return TableProduct(
    id=product.id,
    name=product.name,
    description=product.description,
    price=product.price,
    image=product.image
  )

def find_product(product_id: str) -> Product:
  query = session.query(TableProduct).get(product_id)
  if query == None: return None
  return convert_to_product(query)

def filter_products_by_substr(substr: str) -> list[Product]:
  query = session.query(TableProduct).filter(or_(TableProduct.name.ilike("%"+substr+"%"), TableProduct.description.ilike("%"+substr+"%")))
  users = []
  for user in query:
    if user != None: users.append(convert_to_product(user))
  return users

def get_products() -> list[Product]:
  query = session.query(TableProduct).all()
  products: list[Product] = []
  for product in query:
    if product != None: products.append(convert_to_product(product))
  return products

def add_product(product: Product) -> Product:
  session.add(convert_to_table_product(product))
  session.commit()
  return product

def change_product(product: Product) -> Product:
  query = session.query(TableProduct).get(product.id)
  if query == None: return None
  query.name = product.name
  query.description = product.description
  query.price = product.price
  query.image = product.image

  session.commit()
  return product

def delete_product(product_id: str) -> str:
  query = session.query(TableProduct).get(product_id)
  if query == None: return None
  session.delete(query)

  session.commit()
  return product_id