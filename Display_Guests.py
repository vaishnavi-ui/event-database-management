from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor = connection.cursor()
def disp():
    global e1,e2,t,rowCount
    c=0
    f1=("SELECT E_ID from events where name=? and year=?")
    cursor.execute(f1,[(e1.get()),(e2.get())])
    val1=cursor.fetchone()
    if val1==None:
        noData=Label(t,text="There is no such event! Please try some other event!",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
        rowCount+=1
    else:
        f2=("select name,profession from guests where g_id in (select g_id from GUEST_EVENT where e_id=(SELECT E_ID from events where name=? and year=?))")
        cursor.execute(f2,[(e1.get()),(e2.get())])
        for t in cursor.fetchall():
            c+=1
        if c==0:
            noData=Label(t,text="No Guests are performing at this event!",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
            rowCount+=1
        else:
            name=Label(t,text="Name",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
            prof=Label(t,text="Profession",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=1)
            rowCount+=1
            f3=("select name,profession from guests where g_id in (select g_id from GUEST_EVENT where e_id=(SELECT E_ID from events where name=? and year=?))")
            cursor.execute(f3,[(e1.get()),(e2.get())])
            for row in cursor.fetchall():
                for i in range(0,2):
                    l=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=i)
                rowCount+=1
def DisplayGuestsGUI():
    global e1,e2,t,rowCount
    t=Tk()
    rowCount=0
    t.configure(bg="black")
    l1=Label(t,text="Hi user, here you can see the guests who will be performing at an event!",font="Times 15 bold underline",bg="black",foreground="snow").grid(row=rowCount,column=0)
    rowCount+=1
    l2=Label(t,text="Enter event name",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    e1=Entry(t)
    e1.grid(row=rowCount,column=0)
    rowCount+=1
    l3=Label(t,text="Enter the year of the event",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    e2=Entry(t)
    e2.grid(row=rowCount,column=0)
    rowCount+=1
    b1=Button(t,text="Submit",command=disp,font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
    rowCount+=1

             
