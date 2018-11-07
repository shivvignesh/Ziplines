import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship

Base=declarative_base()

class Product(Base):
	__tablename__='Products'

	product_id=Column(Integer,primary_key=True)
	product_name=Column(String(30),nullable=False)
	seller_name=Column(String(30),nullable=False)
	product_price=Column(Integer,nullable=False)




engine = create_engine("sqlite:///ziplines.db")
Base.metadata.create_all(engine)



