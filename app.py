from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Product,Base


engine=create_engine("sqlite:///ziplines.db")
Base.metadata.bind=engine

Session=sessionmaker(bind=engine)

session=Session()

def create_product(name,price,seller_name):

	product=Product(product_name=name,product_price=price,seller_name=seller_name)

	session.add(product)
	session.commit()

