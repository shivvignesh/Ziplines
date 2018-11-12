from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Product,Customer,Employee,Seller,Base


engine=create_engine("sqlite:///ziplines.db")
Base.metadata.bind=engine

Session=sessionmaker(bind=engine)

session=Session()

def create_product(name,price,seller_name):

	product=Product(product_name=name,product_price=price,seller_name=seller_name)

	session.add(product)
	session.commit()

def create_employee(ename,egender,edob,esalary,ephno):
	
	employee = Employee(employee_name=ename,employee_gender=egender,employee_dob=edob,employee_salary=esalary,employee_phno=ephno)

	session.add(employee)
	session.commit()

def create_customer(cname,cphno,caddress):

	customer = Customer(customer_name=cname,customer_phno=cphno,customer_address=caddress)

	session.add(customer)
	session.commit

def get_employees():

	employees=session.query(Employee.employee_name,Employee.employee_gender)
	return employees

def delete_employees(ename):

	session.query(Employee).filter(Employee.employee_name==ename).delete()
	session.commit()

def create_seller(sname):

	seller=Seller(seller_name=sname)
	session.add(seller)
	session.commit()

def get_seller():

	sellers=session.query(Seller.seller_name)
	return sellers

def get_products():
	products=session.query(Product.product_name,Product.product_price,Product.seller_name)
	return products	