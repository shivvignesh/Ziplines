import tkinter as tk

LARGE_FONT=("Verdana",20)


class Ziplines(tk.Tk):

	def __init__(self,*args,**kwargs):

		tk.Tk.__init__(self,*args,**kwargs)

		container=tk.Frame(self)
		container.grid()
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.geometry("800x600")
		self.frames={}
		#initialization of frames in the dictionary with key as the frame name and object returned as the value
		for F in (Home,Products,Employees,Add_Orders,Customers):
			frame=F(parent=container,controller=self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		
		self.show_frame(Home)
		#code to display the frame required 
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()

class Home(tk.Frame):

	def __init__(self,parent,controller):

		tk.Frame.__init__(self,parent)
		self.controller=controller
		label = tk.Label(self, text="Home", font=LARGE_FONT)
		label.grid(row=2, column=2, padx=10,pady=10)
		button1=tk.Button(self,text="Products",command=lambda:controller.show_frame(Products))
		button2=tk.Button(self,text="Employees",command=lambda:controller.show_frame(Employees))
		button3=tk.Button(self,text="Add_Orders",command=lambda:controller.show_frame(Add_Orders))
		button4=tk.Button(self,text="Customers",command=lambda:controller.show_frame(Customers))
		button5=tk.Button(self,text="Track_Orders",command=lambda:controller.show_frame(View_Participants))
		

		button1.grid(row =4, column = 0, padx=20, pady =20)
		button2.grid(row = 4, column = 3, padx=20, pady =20)
		button3.grid(row = 8,column =1,padx=20, pady =20 )
		button4.grid(row = 8,column =3,padx=20, pady =20 )
		button5.grid(row = 8,column =5,padx=20, pady =20 )


class Products(tk.Frame):

	def __init__(self,parent,controller):
		'''

		'''

		tk.Frame.__init__(self,parent)
		self.controller  = controller
		button1=tk.Button(self,text="Add Product",command=lambda:controller.show_frame(View_Participants))
		button2=tk.Button(self,text="Delete Product",command=lambda:controller.show_frame(View_Participants))
		button3=tk.Button(self,text="display",command=lambda:controller.show_frame(View_Participants))
		button4=tk.Button(self,text="seller info",command=lambda:controller.show_frame(View_Participants))
		
		self.back_button=tk.Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=2,column=3,padx=20,pady=20)
		
		button1.grid(row = 1,column =5,padx=20, pady =20 )
		button2.grid(row = 2,column =5,padx=20, pady =20 )
		button3.grid(row = 3,column =5,padx=20, pady =20 )
		button4.grid(row = 4,column =5,padx=20, pady =20 )

class Employees(tk.Frame):

	def __init__(self,parent,controller):
		'''

		'''

		tk.Frame.__init__(self,parent)
		self.controller  = controller
		button1=tk.Button(self,text="Add Employees",command=lambda:controller.show_frame(View_Participants))
		button2=tk.Button(self,text="Delete Employees",command=lambda:controller.show_frame(View_Participants))
		button3=tk.Button(self,text="Employee Details",command=lambda:controller.show_frame(View_Participants))
		
		self.back_button=tk.Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=2,column=3,padx=20,pady=20)
		
		button1.grid(row = 1,column =5,padx=20, pady =20 )
		button2.grid(row = 2,column =5,padx=20, pady =20 )
		button3.grid(row = 3,column =5,padx=20, pady =20 )
		
class Add_Orders(tk.Frame):

	def __init__(self,parent,controller):
		'''

		'''

		tk.Frame.__init__(self,parent)
		self.controller  = controller
		self.name_label=tk.Label(self,text="Name of Product")
		self.price_label=tk.Label(self,text="Price of Product")
		self.customer_name_label=tk.Label(self,text="Name of customer")
		self.seller_name_label=tk.Label(self,text="Name of seller")
		self.payment_method_label=tk.Label(self,text="payment method")
		

		self.order_name=tk.Text(self,height=2,width=30)
		self.order_price=tk.Text(self,height=2,width=30)
		self.customer_name=tk.Text(self,height=2,width=30)
		self.seller_name=tk.Text(self,height=2,width=30)
		self.payment_method=tk.Text(self,height=2,width=30)

		self.back_button=tk.Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
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


class Customers(tk.Frame):

	def __init__(self,parent,controller):
		'''

		'''

		tk.Frame.__init__(self,parent)
		self.controller  = controller
		button1=tk.Button(self,text="Add Customers",command=lambda:controller.show_frame(View_Participants))
		button2=tk.Button(self,text="Delete Customers",command=lambda:controller.show_frame(View_Participants))
		button3=tk.Button(self,text="Customers Info",command=lambda:controller.show_frame(View_Participants))
		
		self.back_button=tk.Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=2,column=3,padx=20,pady=20)
		
		button1.grid(row = 1,column =5,padx=20, pady =20 )
		button2.grid(row = 2,column =5,padx=20, pady =20 )
		button3.grid(row = 3,column =5,padx=20, pady =20 )
		



app=Ziplines()
app.mainloop()