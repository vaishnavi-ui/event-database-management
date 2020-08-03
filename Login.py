from tkinter import *
from DatabaseAddPage import *
import sqlite3
connection=sqlite3.connect("Event_Management.DB")
cursor=connection.cursor()
def close():
    t.destroy()
#check if input matches info existing in database   
def check():
    global u,p
    find_user=("SELECT * FROM ADMIN WHERE USERNAME =? AND PASSWORD= ?")
    cursor.execute(find_user,[(u.get()),(p.get())])
    if cursor.fetchone() is not None:
        DatabaseAddPage.DatabaseAddPageGUI()
    else:
        incorrect=Tk()
        incorrect.configure(bg="black")
        incorrect.title("Wrong Data")
        l1=Label(incorrect,text="Incorrect username or password",bg="black",foreground="snow",font="Baskerville 12 bold")
        l1.pack()
        desButton=Button(incorrect,text="Try Again",font="Times 12 bold",activebackground="red",command=incorrect.destroy)
        desButton.pack()               


def LoginGUI():
    global u,p,t
    t=Tk()
    t.configure(bg="black")
    t.title("LOGIN PAGE")

    #string variables used
    u=StringVar()
    p=StringVar()

    l1=Label(t,text="ENTER THE LOGIN DETAILS",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)

    #creating labels
    l2=Label(t,text="Username",bg="black",foreground="snow",font="Baskerville 12 bold")
    l2.grid(row=1,column=0)
    L3=Label(t,text="Password",bg="black",foreground="snow",font="Baskerville 12 bold")
    L3.grid(row=2,column=0)


    #taking inputs
    u=Entry(t)
    u.grid(row=1,column=1)
    p=Entry(t)
    p.grid(row=2,column=1)

    #submit button
    s=Button(t,text="Submit",command=check,font="Times 12 bold",activebackground="red")
    s.grid(row=3,column=0)
    q=Button(t,text="Quit",command=close,font="Times 12 bold",activebackground="red")
    q.grid(row=3,column=1)
    t.mainloop()

