from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor= connection.cursor()

def enter1():
    global t
    global e1
    lab=Label(t,text="Enter which year's past events you wish to look into:",bg="black",foreground="snow",font="Baskerville 12 bold")
    lab.grid(row=1,column=0)
    e1=Entry(t)
    e1.grid(row=1,column=1)
    b=Button(t,text="Submit",font="Times 10 bold",activebackground="red",command=past)
    b.grid(row=1,column=2)

def enter2():
    global t
    global e1
    lab=Label(t,text="Enter which year's future events you wish to look into:",bg="black",foreground="snow",font="Baskerville 12 bold")
    lab.grid(row=1,column=0)
    e1=Entry(t)
    e1.grid(row=1,column=1)
    b=Button(t,text="Submit",font="Times 10 bold",activebackground="red",command=future)
    b.grid(row=1,column=2)

#past events
def past():
    global t
    global e1
    cursor.execute("CREATE TEMP VIEW SORT AS SELECT E_ID,NAME,TOPIC,EVENT_DATE,WEBSITE,CHARGE,TYPE,YEAR FROM EVENTS")
    find=("SELECT * FROM SORT WHERE YEAR < ? ORDER BY YEAR DESC")
    cursor.execute(find,[(e1.get())])
    a1=Label(t,text="EVENT ID",font="Baskerville 12 bold").grid(row=3,column=0,sticky=W)
    a2=Label(t,text="EVENT NAME",font="Baskerville 12 bold").grid(row=3,column=1,sticky=W)
    a3=Label(t,text="EVENT TOPIC",font="Baskerville 12 bold").grid(row=3,column=2,sticky=W)
    a4=Label(t,text="EVENT DATE",font="Baskerville 12 bold").grid(row=3,column=3,sticky=W)
    a5=Label(t,text="WEBSITE",font="Baskerville 12 bold").grid(row=3,column=4,sticky=W)
    a6=Label(t,text="CHARGE",font="Baskerville 12 bold").grid(row=3,column=5,sticky=W)
    a7=Label(t,text="TYPE",font="Baskerville 12 bold").grid(row=3,column=6,sticky=W)
    a8=Label(t,text="YEAR",font="Baskerville 12 bold").grid(row=3,column=7,sticky=W)
    a=4
    c1=0
    for row in cursor.fetchall():
        for i in range(0,8):
            l5=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=a,column=c1,sticky=W)
            c1=c1+1
        c1=0
        a+=1

#upcoming events
def future():
    global t
    global e1
    cursor.execute("CREATE TEMP VIEW SORT1 AS SELECT E_ID,NAME,TOPIC,EVENT_DATE,WEBSITE,CHARGE,TYPE,YEAR FROM EVENTS")
    find=("SELECT * FROM SORT1 WHERE YEAR > ? ORDER BY YEAR ASC")
    cursor.execute(find,[(e1.get())])
    a1=Label(t,text="EVENT ID",font="Baskerville 12 bold").grid(row=3,column=0,sticky=W)
    a2=Label(t,text="EVENT NAME",font="Baskerville 12 bold").grid(row=3,column=1,sticky=W)
    a3=Label(t,text="EVENT TOPIC",font="Baskerville 12 bold").grid(row=3,column=2,sticky=W)
    a4=Label(t,text="EVENT DATE",font="Baskerville 12 bold").grid(row=3,column=3,sticky=W)
    a5=Label(t,text="WEBSITE",font="Baskerville 12 bold").grid(row=3,column=4,sticky=W)
    a6=Label(t,text="CHARGE",font="Baskerville 12 bold").grid(row=3,column=5,sticky=W)
    a7=Label(t,text="TYPE",font="Baskerville 12 bold").grid(row=3,column=6,sticky=W)
    a8=Label(t,text="YEAR",font="Baskerville 12 bold").grid(row=3,column=7,sticky=W)
    a=4
    c1=0
    for row in cursor.fetchall():
        for i in range(0,8):
            l6=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=a,column=c1,sticky=W)
            c1=c1+1
        c1=0
        a+=1
def sortGUI():
    global t
    t=Tk()
    t.title("Sort")
    t.geometry("500x100")
    t.configure(bg="black")
    l1=Label(t,text="Welcome to our Sort Station",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)

    menubar=Menu(t)  
    #adding event of which committee
    sort_event=Menu(menubar)
    menubar.add_cascade(label='Sort Events',menu=sort_event)
    sort_event.add_command(label='Past Events',command=enter1)
    sort_event.add_separator()
    sort_event.add_command(label='Future Events',command=enter2)
    t.config(menu=menubar)
    t.mainloop()

