from tkinter import *

window = Tk()
window.title("Find the largest number")
window.geometry("400x300+20+10")

def findsmallest():
    S = []
    S.append(eval(conOfent2.get()))
    S.append(eval(conOfent3.get()))
    S.append(eval(conOfent4.get()))
    smallestNumber.set(min(S))

lbl1 = Label(window, text = "The Program that Finds the smallest Number")
lbl1.grid(row=0, column=1, columnspan=2,sticky=EW)
lbl2 = Label(window,text = "Enter the first number:")
lbl2.grid(row=1, column = 0,sticky=W)
conOfent2 = StringVar()
ent2 = Entry(window,bd=3,textvariable=conOfent2)
ent2.grid(row=1, column = 1)
lbl3 = Label(window,text = "Enter the second number:")
lbl3.grid(row=2, column=0)
conOfent3=StringVar()
ent3 = Entry(window,bd=3,textvariable=conOfent3)
ent3.grid(row=2,column=1)
lbl4 = Label(window,text="Enter the third number:")
lbl4.grid(row=3,column =0, sticky=W)
conOfent4 = StringVar()
ent4 = Entry(window,bd=3,textvariable=conOfent4)
ent4.grid(row=3, column=1)

btn1 = Button(window,text = "Find smallest Number",command=findsmallest)
btn1.grid(row=4, column = 1)
lbl5 = Label(window,text="The largest number:")
lbl5.grid(row=5,column=0,sticky=W)
smallestNumber = StringVar()
ent5 = Entry(window,bd=3,state="readonly",textvariable=smallestNumber)
ent5.grid(row=5,column=1)


mainloop()
