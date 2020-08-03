from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableResource_Event():
    global t
    conn.execute("CREATE TABLE IF NOT EXISTS RESOURCE_EVENT(R_ID NUMBER REFERENCES RESOURCES(R_ID), E_ID NUMBER REFERENCES EVENTS(E_ID),QUANTITY NUMBER)")
    connection.commit()
    conn.execute("INSERT INTO RESOURCE_EVENT VALUES(?,?,?)",(r_id.get(),e_id.get(),quantity.get()))
    connection.commit()
    conn.execute("SELECT * FROM RESOURCE_EVENT")
    for row in conn.fetchall():
        print(row)
       
def Resource_EventGUI():
    global r_id,e_id,quantity
    global t
    t=Tk()
    t.title("Resources for Event")
    t.geometry("500x200")
    t.configure(bg="black")
    l1=Label(t,text="Resources Event Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    
    #Defining Labels
    Lr_id=Label(t,text="RESOURCE ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Le_id=Label(t,text="EVENT ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lquantity=Label(t,text="QUANTITY REQUIRED",bg="black",foreground="snow",font="Baskerville 12 bold")


    #Defining Entry Boxes
    r_id=Entry(t)
    e_id=Entry(t)
    quantity=Entry(t)

    #Adding Labels to window
    Lr_id.grid(row=1,column=0)
    Le_id.grid(row=2,column=0)
    Lquantity.grid(row=3,column=0)

    #Adding Entry box to window
    r_id.grid(row=1,column=1)
    e_id.grid(row=2,column=1)
    quantity.grid(row=3,column=1)

    lr=Label(t,text="The available details for resources:",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=5,column=0)
    conn.execute("SELECT R_ID,NAME FROM RESOURCES")
    a1=Label(t,text="RESOURCE ID",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=6,column=0)
    a2=Label(t,text="RESOURCE NAME",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=6,column=1)
    c1=0
    c=7
    for row in conn.fetchall():
        for i in range(0,2):
            l1=Label(t,text=row[i],font="Baskerville 12 bold",bg="black",foreground="snow")
            l1.grid(row=c,column=c1,sticky=W)
            c1=c1+1
        c1=0
        c+=1
    lr=Label(t,text="The available details for events:",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=c,column=0)
    a1=Label(t,text="EVENT ID",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=c+1,column=0)
    a2=Label(t,text="EVENT NAME",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=c+2,column=1)
    conn.execute("SELECT E_ID,NAME FROM EVENTS")
    c1=0
    k=c+3
    for row in conn.fetchall():
        for i in range(0,2):
            l1=Label(t,text=row[i],font="Baskerville 12 bold",bg="black",foreground="snow")
            l1.grid(row=k,column=c1,sticky=W)
            c1=c1+1
        c1=0
        k+=1
    
    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableResource_Event,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=4,column=1)
    connection.commit()

