from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor= connection.cursor()
import datetime as dt

e1=StringVar
def ue():
    global t
    global e1
    date=dt.datetime.now()
    l2=Label(t,text=f"{dt.datetime.now():%a,%b %d %Y}",fg="snow",bg="black")
    l2.grid(row=1,column=0)
    x=f"{dt.datetime.now():%d/%m/%Y}"
    y=f"{dt.datetime.now():%Y}"
    cursor.execute("CREATE TEMP VIEW UPCOMING AS SELECT E_ID,C_ID,NAME,TOPIC,EVENT_DATE,WEBSITE,CHARGE,TYPE,YEAR FROM EVENTS")
    find1=("SELECT * FROM UPCOMING WHERE EVENT_DATE > ? AND YEAR > ? ORDER BY YEAR ASC")
    cursor.execute(find1,[(x),(y)])
    a1=Label(t,text="EVENT ID",font="Baskerville 12 bold").grid(row=3,column=0,sticky=W)
    a2=Label(t,text="COMMITTEE ID ",font="Baskerville 12 bold").grid(row=3,column=1,sticky=W)
    a3=Label(t,text="EVENT NAME",font="Baskerville 12 bold").grid(row=3,column=2,sticky=W)
    a4=Label(t,text="EVENT TOPIC",font="Baskerville 12 bold").grid(row=3,column=3,sticky=W)
    a5=Label(t,text="EVENT DATE",font="Baskerville 12 bold").grid(row=3,column=4,sticky=W)
    a6=Label(t,text="WEBSITE",font="Baskerville 12 bold").grid(row=3,column=5,sticky=W)
    a7=Label(t,text="CHARGE",font="Baskerville 12 bold").grid(row=3,column=6,sticky=W)
    a8=Label(t,text="TYPE",font="Baskerville 12 bold").grid(row=3,column=7,sticky=W)
    a9=Label(t,text="YEAR",font="Baskerville 12 bold").grid(row=3,column=8,sticky=W)
    c=4
    c1=0
    for row in cursor.fetchall():
        for i in range(0,9):
            l3=Label(t,text=row[i],font="Baskerville 12 bold",bg="black",foreground="snow")
            l3.grid(row=c,column=c1,sticky=W)
            c1=c1+1
        c1=0
        c+=1

def upcomingGUI():
    global t
    global e1
    t=Tk()
    t.title("Upcoming events")
    t.geometry("600x500")
    t.configure(bg="black")
    l1=Label(t,text="Upcoming Events!",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    b1=Button(t,text=" Enter ",command=ue,font="Times 10 bold",activebackground="red")
    b1.grid(row=2,column=0)
    t.mainloop()


