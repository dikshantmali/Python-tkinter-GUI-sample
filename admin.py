#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:28:08 2019

@author: dikshant
"""

#ADMIN PAGE FOR LOGIN
from tkinter import *
root =Tk()
root.geometry("1300x700")
root.minsize(1300,700)
root.maxsize(1300,700)


f1 =Frame(root,borderwidth=3,relief=SUNKEN,bg="salmon")
f1.pack(side=TOP,fill="x")

l1 = Label(f1,text="!!!SHUBH LABH STOCK MANAGEMENT SYSTEM!!!",font=("Helvetica 30 bold"))
l1.pack()


l3 = Label(root,text="!!!JAY SUNDHA MATA!!!",font=("Helvetica 30 bold"),bg="salmon")
l3.pack(side=BOTTOM,fill=X)


f2 = Frame(root)
f2.pack(fill=X,pady=40)


photo = PhotoImage(file="abc.png")
y = Label(f2,image=photo)
y.pack(side=LEFT)

f3 = Frame(f2,borderwidth=3,relief=SUNKEN)
f3.pack(side=LEFT,padx= 40)

l2 = Label(f3,text="ADMIN-LOGIN",font=("Helvetica 30 bold"))
user = Label(f3,text="admin name : ",font=("Helvetica 20 bold"))
password = Label(f3,text = "password : ",font=("Helvetica 20 bold"))
l2.grid(row=0,column=1,pady=20)
user.grid(row=1,padx=20,pady=20)
password.grid(row=2,padx=20,pady=20)


uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(f3,textvariable= uservalue,font=("Helvetica 20 bold"))
passentry = Entry(f3,textvariable= passvalue,font=("Helvetica 20 bold"))
userentry.grid(row=1,column=1,padx=15,pady=20)
passentry.grid(row=2,column=1,padx=15,pady=20)


Button(f3,text="LOGIN").grid(row=4,column=1,pady=20)
root.mainloop()
