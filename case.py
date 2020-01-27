#My case Page Where I describe The Facility That My Software Provide
from tkinter import *
root = Tk()
root.geometry("1300x700")
root.minsize(1300,700)
root.maxsize(1300,700)

l1 = Label(root,text="!!!SHUBH LABH STOCK MANAGEMENT SYSTEM!!!",font=("Helvetica 30 bold"),bg="salmon")
l1.pack(fill=X)

l4 = Label(root,text="  AVAILABLE FECILITIES  ",font=("Helvetica 30 bold"),fg="green",bg="black")
l4.pack(padx=20,pady=20,fill=X)

l3 = Label(root,text="!!!JAY SUNDHA MATA!!!",font=("Helvetica 30 bold"),bg="salmon")
l3.pack(side=BOTTOM,fill=X)


f1 =Frame(root,borderwidth=3,relief=SUNKEN,bg="salmon")
f1.pack(side=LEFT,padx=85)


f2 =Frame(root,borderwidth=3,relief=SUNKEN,bg="salmon")
f2.pack(side=LEFT,padx=85)


f3 =Frame(root,borderwidth=3,relief=SUNKEN,bg="salmon")
f3.pack(side=LEFT,padx=85)

Button(f1,text="  CHECK OVERALL STOCK  ").pack(padx=60,pady=60)
Button(f2,text="  ADD AN ITEM  ").pack(padx=60,pady=60)
Button(f3,text="  REMOVE AN ITEM  ").pack(padx=60,pady=60)

root.mainloop()
