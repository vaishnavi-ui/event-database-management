from tkinter import *
from Total_Cost import *
from Members import *
from Remove_Member import *
from Resource_Event import *
from Guest_Event import *
from Sponsor_Event import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor = connection.cursor()
def DisplayMenu():
    global y
    y.destroy()
    t=Tk()
    t.title("Committee Page")
    t.configure(bg="black")
    t.geometry("600x400")
    l1=Label(t,text="WELCOME TO COMMITTEE PAGE",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    l2=Label(t,text="Hi, Welcome. Please select your choice!Click on the button!",bg="black",foreground="snow",font="Baskerville 12 bold")
    l2.grid(row=1,column=0)

    #Creating  Labels
    Lcost=Label(t,text="Calculate Cost of Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ladd=Label(t,text="Add Member to Committee",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lremove=Label(t,text="Remove Member",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lspon=Label(t,text="Add Sponsors to Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lresource=Label(t,text="Add Resources to Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lguest=Label(t,text="Add Guests to Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    

    #Adding Labels
    Lcost.grid(row=2,column=0)
    Ladd.grid(row=3,column=0)
    Lremove.grid(row=4,column=0)
    Lspon.grid(row=5,column=0)
    Lresource.grid(row=6,column=0)
    Lguest.grid(row=7,column=0)


    #Creating Buttons
    cost=Button(t,text="Click here!",font="Times 12 bold",activebackground="red",command=lambda: destructTotalCost(t))
    add=Button(t,text="Click here!",font="Times 12 bold",activebackground="red",command=MembersGUI)
    remove=Button(t,text="Click here!",font="Times 12 bold",activebackground="red",command=RemoveMemberGUI)
    spon=Button(t,text="Click here!",font="Times 12 bold",activebackground="red",command=Sponsor_EventGUI)
    resource=Button(t,text="Click here!",font="Times 12 bold",activebackground="red",command=Resource_EventGUI)
    guest=Button(t,text="Click here!",font="Times 12 bold",activebackground="red",command=Guest_EventGUI)


    #Adding Buttons
    cost.grid(row=2,column=1)
    add.grid(row=3,column=1)
    remove.grid(row=4,column=1)
    spon.grid(row=5,column=1)
    resource.grid(row=6,column=1)
    guest.grid(row=7,column=1)
    
def Pass():
    global e
    find_comm=("SELECT C_ID FROM COMMITTEE WHERE NAME=?")
    cursor.execute(find_comm,[(e.get())])
    if cursor.fetchone() is not None:
        cursor.execute(find_comm,[(e.get())])
        store=cursor.fetchone()
        getId(store)
        getID(store)
        l=Label(y,text="Correct Committee ID! You can proceed!",bg="black",foreground="snow",font="Baskerville 12 bold")
        l.grid(row=2,column=0)
        b2=Button(y,text="Proceed",command=DisplayMenu,font="Times 12 bold",activebackground="red")
        b2.grid(row=3,column=0)
    else:
        incorrect=Tk()
        incorrect.configure(bg="black")
        incorrect.title("Wrong Data")
        l1=Label(incorrect,text="Incorrect committee name!!",bg="black",foreground="snow",font="Baskerville 12 bold")
        l1.pack()
        desButton=Button(incorrect,text="Try Again",font="Times 12 bold",activebackground="red",command=incorrect.destroy)
        desButton.pack() 
    
def CommitteeMainPageGUI():
    global e,y
    y=Tk()
    y.title("Check ID")
    y.configure(bg="black")
    l=Label(y,text="Enter your committee name:",bg="black",foreground="snow",font="Baskerville 12 bold")
    e=Entry(y)
    l.grid(row=0,column=0)
    e.grid(row=0,column=1)
    b1=Button(y,text="Proceed",command=Pass,font="Times 12 bold",activebackground="red")
    b1.grid(row=1,column=0)
    


