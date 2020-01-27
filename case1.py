#My case1 Page describes the perticular item or whole stock that a admin wanted to see
from tkinter import *
root = Tk()
root.geometry("1300x700")
root.minsize(1300,700)
root.maxsize(1300,700)

l1 = Label(root,text="!!!SHUBH LABH STOCK MANAGEMENT SYSTEM!!!",font=("Helvetica 30 bold"),bg="salmon")
l1.pack(fill=X)

l4 = Label(root,text="  CHECK OVERALL STOCK  ",font=("Helvetica 30 bold"),fg="green",bg="black")
l4.pack(padx=20,pady=20,fill=X)
l3 = Label(root,text="!!!JAY SUNDHA MATA!!!",font=("Helvetica 30 bold"),bg="salmon")
l3.pack(side=BOTTOM,fill=X)


f1 =Frame(root,borderwidth=3,relief=SUNKEN,bg="salmon")
f1.pack(side=LEFT,padx=200)


f2 =Frame(root,borderwidth=3,relief=SUNKEN,bg="salmon")
f2.pack(side=LEFT,padx=50)



Button(f1,text="  WATCH AN PERTICULAR ITEM  ").pack(padx=60,pady=60)
Button(f2,text="  SEE FULL STOCK  ").pack(padx=60,pady=60)


root.mainloop()
