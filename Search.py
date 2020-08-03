from tkinter import *
from tkinter.ttk import * 
from time import strftime

import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor= connection.cursor()

#free of charge events
def free():
    global t
    cursor.execute("CREATE TEMP VIEW SEARCH AS SELECT E_ID,NAME,TOPIC,EVENT_DATE,WEBSITE,CHARGE,TYPE FROM EVENTS")
    find=("SELECT * FROM SEARCH WHERE CHARGE=0")
    cursor.execute(find)
    a1=Label(t,text="EVENT ID",font="Baskerville 12 bold").grid(row=3,column=0,sticky=W)
    a2=Label(t,text="EVENT NAME",font="Baskerville 12 bold").grid(row=3,column=1,sticky=W)
    a3=Label(t,text="EVENT TOPIC",font="Baskerville 12 bold").grid(row=3,column=2,sticky=W)
    a4=Label(t,text="EVENT DATE",font="Baskerville 12 bold").grid(row=3,column=3,sticky=W)
    a5=Label(t,text="WEBSITE",font="Baskerville 12 bold").grid(row=3,column=4,sticky=W)
    a6=Label(t,text="CHARGE  ",font="Baskerville 12 bold").grid(row=3,column=5,sticky=W)
    a7=Label(t,text="TYPE",font="Baskerville 12 bold").grid(row=3,column=6,sticky=W)
    a=4
    c1=0
    for row in cursor.fetchall():
        for i in range(0,7):
            l4=Label(t,text=row[i],background="black",foreground="snow",font="Baskerville 12 bold")
            l4.grid(row=a,column=c1,sticky=W)
            c1=c1+1
        c1=0
        a+=1

#price mentioned
def charge_price():
    global t
    global e1
    cursor.execute("CREATE TEMP VIEW SEARCH1 AS SELECT E_ID,C_ID,NAME,TOPIC,EVENT_DATE,WEBSITE,CHARGE,TYPE FROM EVENTS")
    find=("SELECT * FROM SEARCH1 WHERE CHARGE=?")
    cursor.execute(find,[(e1.get())])

    if cursor.fetchone() is not None:
        a1=Label(t,text="EVENT ID",font="Baskerville 12 bold").grid(row=3,column=0,sticky=W)
        a2=Label(t,text="COMMITTEE ID ",font="Baskerville 12 bold").grid(row=3,column=1,sticky=W)
        a3=Label(t,text="EVENT NAME",font="Baskerville 12 bold").grid(row=3,column=2,sticky=W)
        a4=Label(t,text="EVENT TOPIC",font="Baskerville 12 bold").grid(row=3,column=3,sticky=W)
        a5=Label(t,text="EVENT DATE",font="Baskerville 12 bold").grid(row=3,column=4,sticky=W)
        a6=Label(t,text="WEBSITE",font="Baskerville 12 bold").grid(row=3,column=5,sticky=W)
        a7=Label(t,text="CHARGE",font="Baskerville 12 bold").grid(row=3,column=6,sticky=W)
        a8=Label(t,text="TYPE",font="Baskerville 12 bold").grid(row=3,column=7,sticky=W)
        cursor.execute(find,[(e1.get())])
        c=4
        c1=0
        for row in cursor.fetchall():
            for i in range(0,8):
                l3=Label(t,text=row[i],background="black",foreground="snow",font="Baskerville 12 bold")
                l3.grid(row=c,column=c1,sticky=W)
                c1=c1+1
            c1=0
            c+=1
    else :
        ll=Label(t,text="No such price exists for the events!",font="Baskerville 12 bold").grid(row=3,column=1)


#entering price desired
def enter():
    global t
    l2=Label(t,text="Enter price of event to be searched",font="Times 15 bold",background="black",foreground="snow")
    l2.grid(row=2,column=0)
    global e1
    e1=Entry(t)
    e1.grid(row=2,column=1)
    b=Button(t,text="Submit",command=charge_price)
    b.grid(row=3,column=0,sticky=W)

#any price
def any():
    global t
    cursor.execute("CREATE TEMP VIEW SEARCH2 AS SELECT E_ID,C_ID,NAME,TOPIC,EVENT_DATE,WEBSITE,CHARGE,TYPE FROM EVENTS")
    find=("SELECT * FROM SEARCH2 ORDER BY CHARGE ASC")
    cursor.execute(find)
    a1=Label(t,text="EVENT ID",font="Baskerville 12 bold").grid(row=4,column=0,sticky=W)
    a2=Label(t,text="COMMITTEE ID ",font="Baskerville 12 bold").grid(row=4,column=1,sticky=W)
    a3=Label(t,text="EVENT NAME",font="Baskerville 12 bold").grid(row=4,column=2,sticky=W)
    a4=Label(t,text="EVENT TOPIC",font="Baskerville 12 bold").grid(row=4,column=3,sticky=W)
    a5=Label(t,text="EVENT DATE",font="Baskerville 12 bold").grid(row=4,column=4,sticky=W)
    a6=Label(t,text="WEBSITE",font="Baskerville 12 bold").grid(row=4,column=5,sticky=W)
    a7=Label(t,text="CHARGE",font="Baskerville 12 bold").grid(row=4,column=6,sticky=W)
    a8=Label(t,text="TYPE",font="Baskerville 12 bold").grid(row=4,column=7,sticky=W)
    y=5
    c1=0
    for row in cursor.fetchall():
        for i in range(0,8):
            l5=Label(t,text=row[i],background="black",foreground="snow",font="Baskerville 12 bold")
            l5.grid(row=y,column=c1,sticky=W)
            c1=c1+1
        c1=0
        y+=1

def com_wise():
    global t
    global e2
    cursor.execute("CREATE TEMP VIEW SEARCH3 AS SELECT E_ID,C_ID,NAME,TOPIC,EVENT_DATE,WEBSITE,CHARGE,TYPE FROM EVENTS")
    find1=("SELECT * FROM SEARCH3 WHERE C_ID == ?")
    cursor.execute(find1,[(e2.get())])
    '''
    if cursor.fetchone() is None :
         ll=Label(t,text="No such committee id exists for the events!",font="Baskerville 12 bold").grid(row=3,column=1)

    else :
    '''
    a1=Label(t,text="EVENT ID",font="Baskerville 12 bold").grid(row=3,column=0,sticky=W)
    a2=Label(t,text="COMMITTEE ID ",font="Baskerville 12 bold").grid(row=3,column=1,sticky=W)
    a3=Label(t,text="EVENT NAME",font="Baskerville 12 bold").grid(row=3,column=2,sticky=W)
    a4=Label(t,text="EVENT TOPIC",font="Baskerville 12 bold").grid(row=3,column=3,sticky=W)
    a5=Label(t,text="EVENT DATE",font="Baskerville 12 bold").grid(row=3,column=4,sticky=W)
    a6=Label(t,text="WEBSITE",font="Baskerville 12 bold").grid(row=3,column=5,sticky=W)
    a7=Label(t,text="CHARGE",font="Baskerville 12 bold").grid(row=3,column=6,sticky=W)
    a8=Label(t,text="TYPE",font="Baskerville 12 bold").grid(row=3,column=7,sticky=W)
    b=4
    c1=0
    for row in cursor.fetchall():
        for i in range(0,8):
            l7=Label(t,text=row[i],background="black",foreground="snow",font="Baskerville 12 bold")
            l7.grid(row=b,column=c1,sticky=W)
            c1=c1+1
        c1=0
        b+=1
                
#committeee wise search for events
def enter2():
    global t
    l6=Label(t,text="Enter Committee id to be searched",font="Times 15 bold",background="black",foreground="snow")
    l6.grid(row=2,column=0)
    global e2
    e2=Entry(t)
    e2.grid(row=2,column=1)
    b=Button(t,text="Submit",command=com_wise)
    b.grid(row=3,column=0,sticky=W)
    
def searchGUI():
    global t
    t=Tk()
    t.title("Search")
    t.configure(bg="black")
    t.geometry("400x100")
    l1=Label(t,text="Welcome to our Search Station",font="Times 20 bold underline",background="black",foreground="snow")
    l1.grid(row=0,column=0)

    menubar=Menu(t)
    #adding price range
    price=Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Charges of event',menu=price)
    price.add_command(label='Free of cost',command=free)
    price.add_separator()
    price.add_command(label='Specific Price',command=enter)
    price.add_separator()
    price.add_command(label='Any price',command=any)

    #adding committee wise search
    com=Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Committee Events',menu=com)
    com.add_command(label='Search Committee',command=enter2)
    com.add_separator()

    t.config(menu= menubar)
    t.mainloop()
