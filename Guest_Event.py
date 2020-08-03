from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableGuest_Event():
    print("in")
    conn.execute("CREATE TABLE IF NOT EXISTS GUEST_EVENT(G_ID NUMBER REFERENCES GUESTS(G_ID), E_ID NUMBER REFERENCES EVENTS(E_ID),CHARGE NUMBER)")
    connection.commit()
    conn.execute("INSERT INTO GUEST_EVENT VALUES(?,?,?)",(g_id.get(),e_id.get(),g_charge.get()))
    connection.commit()
    conn.execute("SELECT * FROM GUEST_EVENT")
    for row in conn.fetchall():
        print(row)
    

def Guest_EventGUI():
    global g_id,e_id,g_charge
    t=Tk()
    t.title("Guests for Event")
    t.geometry("400x250")
    t.configure(bg="black")
    l1=Label(t,text="Guests Event Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    
    #Defining Labels
    Lg_id=Label(t,text="GUEST ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Le_id=Label(t,text="EVENT ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lg_charge=Label(t,text="CHARGE REQUIRED",bg="black",foreground="snow",font="Baskerville 12 bold")


    #Defining Entry Boxes
    g_id=Entry(t)
    e_id=Entry(t)
    g_charge=Entry(t)

    #Adding Labels to window
    Lg_id.grid(row=1,column=0)
    Le_id.grid(row=2,column=0)
    Lg_charge.grid(row=3,column=0)

    #Adding Entry box to window
    g_id.grid(row=1,column=1)
    e_id.grid(row=2,column=1)
    g_charge.grid(row=3,column=1)

    lg=Label(t,text="The available guest id and guest name are:",font="Baskerville 12 bold",bg="black",foreground="snow")
    lg.grid(row=5,column=0)
    a1=Label(t,text="GUEST ID",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=6,column=0,sticky=W)
    a2=Label(t,text="GUEST NAME",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=6,column=1,sticky=W)
    conn.execute("SELECT * FROM GUESTS")
    c=7
    c1=0
    for row in conn.fetchall():
        for i in range(0,2):
            ln=Label(t,text=row[i],font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=c,column=c1,sticky=W)
            c1=c1+1
        c1=0
        c+=1

    le=Label(t,text="The available event id and event name are:",font="Baskerville 12 bold",bg="black",foreground="snow")
    le.grid(row=c,column=0)
    a11=Label(t,text="EVENT ID",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=c+1,column=0,sticky=W)
    a12=Label(t,text="EVENT NAME",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=c+1,column=1,sticky=W)
    conn.execute("SELECT * FROM EVENTS")
    k=c+3
    c1=0
    for row in conn.fetchall():
        for i in range(0,2):
            ln=Label(t,text=row[i],font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=k,column=c1,sticky=W)
            c1=c1+1
        c1=0
        k+=1

    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableGuest_Event,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=4,column=1)
    connection.commit()

