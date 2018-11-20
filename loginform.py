import tkinter
from tkinter import *
from tkinter import messagebox
gui = Tk()
gui.geometry("300x100")
#make sure first is capital and second is not
gui.title("Login Form")

user_label=Label(gui, text="UserName:").grid(row=0,column=0)

pwd_label=Label(gui, text="Password:").grid(row=1,column=0)

user_entry=Entry(gui)
user_entry.grid(row=0,column=1)

pwd_entry=Entry(gui,show="*")
pwd_entry.grid(row=1,column=1)

def login(event):
	import pymongo 
	client = pymongo.MongoClient("mongodb://localhost:27017/")
	db=client["Login"]
	collection=db["User"]
	uname=user_entry.get()
	pwd=pwd_entry.get()
	for r in collection.find({},{"UserName":1,"Password":1}):
		cunm=str(r["UserName"]);
		cpwd=str(r["Password"]);
		if uname==cunm and pwd==cpwd:
			messagebox.showinfo("Successful Login", "Successful Login....")
			user_entry.delete('0',END);
			pwd_entry.delete('0',END);
		else:
			messagebox.showerror("Login Failed","Invalid UserName and Password")
			user_entry.delete('0',END);
			pwd_entry.delete('0',END);
loginbtn=Button(gui,text="Login");
loginbtn.grid(row=2,column=1);
loginbtn.bind('<Button-1>',login);
gui.mainloop()