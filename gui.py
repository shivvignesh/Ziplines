from tkinter import *
from tkinter.ttk import *

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
		for F in (Home,Products,Employees):
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
		button3=Button(self,text="display",command=lambda:controller.show_frame(View_Participants))
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


app=Ziplines()
app.mainloop()