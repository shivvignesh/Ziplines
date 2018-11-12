from tkinter import *
from tkinter.ttk import *
from app import *
LARGE_FONT=("Verdana",20)


class Ziplines(Tk):

	def __init__(self,*args,**kwargs):

		Tk.__init__(self,*args,**kwargs)

		container=Frame(self)
		container.grid()
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.geometry("800x600")
		self.frames={}
		#initialization of frames in the dictionary with key as the frame name and object returned as the value
		for F in (Home,Products,Employees,Add_Orders,Customers,Add_Products,Add_Customers,Add_Employees,Employee_detail,Delete_employees,Seller_info,display_products):
			frame=F(parent=container,controller=self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		
		self.show_frame(Home)
		#code to display the frame required 
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()

class Home(Frame):

	def __init__(self,parent,controller):

		Frame.__init__(self,parent)
		self.controller=controller
		label = Label(self, text="Home", font=LARGE_FONT)
		label.grid(row=2, column=2, padx=10,pady=10)
		button1=Button(self,text="Products",command=lambda:controller.show_frame(Products))
		button2=Button(self,text="Employees",command=lambda:controller.show_frame(Employees))
		button3=Button(self,text="Add_Orders",command=lambda:controller.show_frame(Add_Orders))
		button4=Button(self,text="Customers",command=lambda:controller.show_frame(Customers))		
		button5=Button(self,text="Track_Orders",command=lambda:controller.show_frame(View_Participants))
		button6=Button(self,text="Seller info",command=lambda:controller.show_frame(Seller_info))
		

		button1.grid(row =4, column = 0, padx=20, pady =20)
		button2.grid(row = 4, column = 3, padx=20, pady =20)
		button3.grid(row = 8,column =1,padx=20, pady =20 )
		button4.grid(row = 8,column =3,padx=20, pady =20 )
		button5.grid(row = 8,column =5,padx=20, pady =20 )
		button6.grid(row=8,column=7,padx=10,pady=10)


class Products(Frame):

	def __init__(self,parent,controller):
		'''

		'''

		Frame.__init__(self,parent)
		self.controller  = controller
		button1=Button(self,text="Add Product",command=lambda:controller.show_frame(Add_Products))
		button2=Button(self,text="Delete Product",command=lambda:controller.show_frame(View_Participants))
		button3=Button(self,text="display",command=lambda:controller.show_frame(display_products))
		button4=Button(self,text="seller info",command=lambda:controller.show_frame(View_Participants))
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=2,column=3,padx=20,pady=20)
		
		button1.grid(row = 1,column =5,padx=20, pady =20 )
		button2.grid(row = 2,column =5,padx=20, pady =20 )
		button3.grid(row = 3,column =5,padx=20, pady =20 )
		button4.grid(row = 4,column =5,padx=20, pady =20 )

class Employees(Frame):

	def __init__(self,parent,controller):
		'''

		'''

		Frame.__init__(self,parent)
		self.controller  = controller
		button1=Button(self,text="Add Employees",command=lambda:controller.show_frame(Add_Employees))
		button2=Button(self,text="Delete Employees",command=lambda:controller.show_frame(Delete_employees))
		button3=Button(self,text="Employee Details",command=lambda:controller.show_frame(Employee_detail))
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=2,column=3,padx=20,pady=20)
		
		button1.grid(row = 1,column =5,padx=20, pady =20 )
		button2.grid(row = 2,column =5,padx=20, pady =20 )
		button3.grid(row = 3,column =5,padx=20, pady =20 )
		
class Add_Orders(Frame):

	def __init__(self,parent,controller):
		'''

		'''

		Frame.__init__(self,parent)
		self.controller  = controller
		self.name_label=Label(self,text="Name of Product")
		self.price_label=Label(self,text="Price of Product")
		self.customer_name_label=Label(self,text="Name of customer")
		self.seller_name_label=Label(self,text="Name of seller")
		self.payment_method_label=Label(self,text="payment method")
		

		self.order_name=Text(self,height=2,width=30)
		self.order_price=Text(self,height=2,width=30)
		self.customer_name=Text(self,height=2,width=30)
		self.seller_name=Text(self,height=2,width=30)
		self.payment_method=Text(self,height=2,width=30)

		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=10,column=3,padx=20,pady=20)
		
		self.name_label.grid(row=1,column=0,padx=10,pady=10)
		self.order_name.grid(row=1,column=1,padx=10,pady=10)

		self.price_label.grid(row=2,column=0,padx=10,pady=10)
		self.order_price.grid(row=2,column=1,padx=10,pady=10)

		self.customer_name_label.grid(row=3,column=0,padx=10,pady=10)
		self.customer_name.grid(row=3,column=1,padx=10,pady=10)

		self.seller_name_label.grid(row=4,column=0,padx=10,pady=10)
		self.seller_name.grid(row=4,column=1,padx=10,pady=10)

		self.payment_method_label.grid(row=5,column=0,padx=10,pady=10)
		self.payment_method.grid(row=5,column=1,padx=10,pady=10)


class Customers(Frame):

	def __init__(self,parent,controller):
		'''

		'''

		Frame.__init__(self,parent)
		self.controller  = controller
		button1=Button(self,text="Add Customers",command=lambda:controller.show_frame(Add_Customers))
		button2=Button(self,text="Delete Customers",command=lambda:controller.show_frame(View_Participants))
		button3=Button(self,text="Customers Info",command=lambda:controller.show_frame(View_Participants))
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=2,column=3,padx=20,pady=20)
		
		button1.grid(row = 1,column =5,padx=20, pady =20 )
		button2.grid(row = 2,column =5,padx=20, pady =20 )
		button3.grid(row = 3,column =5,padx=20, pady =20 )
		
class Add_Products(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.name_label=Label(self,text="Name of Product")
		self.price_label=Label(self,text="Price of Product")
		self.seller_name_label=Label(self,text="Name of seller")
		
		self.product_name=Text(self,height=2,width=30)
		self.product_price=Text(self,height=2,width=30)
		# self.seller_name=tk.Text(self,height=2,width=30)

		option=[]
		seller=get_seller()

		for r in seller:
			option.append(r)

		options = list(set(option))		#to obtain only unique events 
		variable = StringVar(self)
		variable.set(options[0])		#Setting the default event
		self.select = OptionMenu(self, variable,*options).grid(row =2,column =1,padx=10,pady=10)
		self.seller_name = variable.get()
	
		
		self.name_label.grid(row=3,column=1,padx=10,pady=10)
		self.price_label.grid(row=4,column=1,padx=10,pady=10)
		self.seller_name_label.grid(row=5,column=1,padx=10,pady=10)

		self.product_name.grid(row=3,column=2,padx=10,pady=10)
		self.product_price.grid(row=4,column=2,padx=10,pady=10)
		# self.seller_name.grid(row=5,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Products))
		self.back_button.grid(row=2,column=3,padx=20,pady=20)

		self.submit_button=Button(self,text="Submit",command=self.add_product)
		self.submit_button.grid(row=3,column=3,padx=20,pady=20)

	def add_product(self):
		self.pname=self.product_name.get("1.0","end-1c")
		self.pprice=self.product_price.get("1.0","end-1c")
		# self.sname=self.seller_name.get("1.0","end-1c")

		self.product_name.delete("1.0","end")
		self.product_price.delete("1.0","end")
		# self.seller_name.delete("1.0","end")

		create_product(self.pname,self.pprice,self.seller_name)



class Add_Customers(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.cust_name_label=Label(self,text="Name of customer")
		self.cust_phno_label=Label(self,text="Phone Number")
		self.cust_address_label=Label(self,text="Address")
		
		self.cust_name=Text(self,height=2,width=30)
		self.cust_phno=Text(self,height=2,width=30)
		self.cust_address=Text(self,height=10,width=30)
		
		self.cust_name_label.grid(row=3,column=1,padx=10,pady=10)
		self.cust_phno_label.grid(row=4,column=1,padx=10,pady=10)
		self.cust_address_label.grid(row=5,column=1,padx=10,pady=10)

		self.cust_name.grid(row=3,column=2,padx=10,pady=10)
		self.cust_phno.grid(row=4,column=2,padx=10,pady=10)
		self.cust_address.grid(row=5,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Customers))
		self.back_button.grid(row=2,column=3,padx=20,pady=20) 	

		self.submit_button=Button(self,text="Submit",command=self.add_customer)
		self.submit_button.grid(row=3,column=3,padx=20,pady=20)
	

	def add_customer(self):


		self.cname = self.cust_name.get("1.0","end-1c")
		self.cphno = self.cust_phno.get("1.0","end-1c")
		self.caddress = self.cust_address.get("1.0","end-1c")
		self.cust_name.delete("1.0","end")
		self.cust_phno.delete("1.0","end")
		self.cust_address.delete("1.0","end")

		create_customer(self.cname,self.cphno,self.caddress)


class Add_Employees(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.emp_name_label=Label(self,text="Name of Employee")
		self.emp_salary_label=Label(self,text="Employee salary")
		self.emp_dob_label=Label(self,text="Employee Date of Birth")
		self.emp_gender_label=Label(self,text="Gender")
		self.emp_phno_label=Label(self,text="Phone Number")
		
		self.emp_name=Text(self,height=2,width=30)
		self.emp_salary=Text(self,height=2,width=30)
		self.emp_dob=Text(self,height=2,width=30)
		self.emp_gender=Text(self,height=2,width=30)
		self.emp_phno=Text(self,height=2,width=30)
		
		self.emp_name_label.grid(row=3,column=1,padx=10,pady=10)
		self.emp_salary_label.grid(row=4,column=1,padx=10,pady=10)
		self.emp_dob_label.grid(row=5,column=1,padx=10,pady=10)
		self.emp_gender_label.grid(row=6,column=1,padx=10,pady=10)
		self.emp_phno_label.grid(row=7,column=1,padx=10,pady=10)

		self.emp_name.grid(row=3,column=2,padx=10,pady=10)
		self.emp_salary.grid(row=4,column=2,padx=10,pady=10)
		self.emp_dob.grid(row=5,column=2,padx=10,pady=10)
		self.emp_gender.grid(row=6,column=2,padx=10,pady=10)
		self.emp_phno.grid(row=7,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Employees))
		self.back_button.grid(row=2,column=3,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.add_employee)
		self.submit_button.grid(row=3,column=3,padx=20,pady=20)


	def add_employee(self):
			
		self.ename=self.emp_name.get("1.0","end-1c")
		self.egender=self.emp_gender.get("1.0","end-1c")
		self.edob=self.emp_dob.get("1.0","end-1c")
		self.esalary=self.emp_salary.get("1.0","end-1c")
		self.ephno=self.emp_phno.get("1.0","end-1c")

		self.emp_name.delete("1.0","end")
		self.emp_gender.delete("1.0","end")
		self.emp_dob.delete("1.0","end")
		self.emp_salary.delete("1.0","end")
		self.emp_phno.delete("1.0","end")

		create_employee(self.ename,self.egender,self.edob,self.esalary,self.ephno)

class Employee_detail(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.display_button=Button(self,text="display",command=self.emp_details)
		self.display_button.grid(row=3,column=3,padx=20,pady=20)


		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Employees))
		self.back_button.grid(row=2,column=3,padx=20,pady=20)

	def emp_details(self):

		self.lb=Listbox()

		employees=get_employees()

		for r in employees:
			i=1
			self.lb.insert(i,r)
			++i

		self.lb.grid(row=3,column=3,padx=10,pady=10)	

class Delete_employees(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller
		
		self.emp_name=Text(self,height=2,width=30)
		
		self.emp_name.grid(row=3,column=2,padx=10,pady=10)
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Employees))
		self.back_button.grid(row=2,column=3,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.delete_employee)
		self.submit_button.grid(row=3,column=3,padx=20,pady=20)

	def delete_employee(self):
		self.ename=self.emp_name.get("1.0","end-1c")
		self.emp_name.delete("1.0","end")

		delete_employees(self.ename)
		
class Seller_info(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.seller_name=Text(self,height=2,width=30)
		
		self.seller_name.grid(row=3,column=2,padx=10,pady=10)
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=2,column=3,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.add_seller)
		self.submit_button.grid(row=3,column=3,padx=20,pady=20)
	
	def add_seller(self):

		self.sname=self.seller_name.get("1.0","end-1c")
		self.seller_name.delete("1.0","end")

		create_seller(self.sname)

class display_products(Frame):


	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.tree=Treeview( self, columns=('Name','Price', 'Seller Name'))
		self.tree.heading('#0',text='Item')
		self.tree.heading('#1',text='Price')
		self.tree.heading('#2',text='Seller Name')
		self.tree.column('#1',stretch=YES)
		self.tree.column('#2', stretch=YES)
		self.tree.column('#0', stretch=YES)
		self.tree.grid(row=4, column=4 ,padx=10,pady=10,columnspan=4, sticky='nsew')
		self.treeview = self.tree
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Products))
		self.back_button.grid(row=2,column=3,padx=20,pady=20)
		# Initialize the counter
		
		products=get_products()

		for i in products:
			self.tree.insert("",END,values=i)

	


app=Ziplines()
app.mainloop()