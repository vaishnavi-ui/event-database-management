from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableSponsor_Event():
    print("in")
    conn.execute("CREATE TABLE IF NOT EXISTS SPONSOR_EVENT(S_ID NUMBER REFERENCES SPONSORS(S_ID), E_ID NUMBER REFERENCES EVENTS(E_ID))")
    connection.commit()
    conn.execute("INSERT INTO SPONSOR_EVENT VALUES(?,?)",(s_id.get(),e_id.get()))
    connection.commit()
    conn.execute("SELECT * FROM SPONSOR_EVENT")
    for row in conn.fetchall():
        print(row)
    

def Sponsor_EventGUI():
    global s_id,e_id
    t=Tk()
    t.title("Sponsors for Event")
    t.geometry("450x160")
    t.configure(bg="black")
    l1=Label(t,text="Sponsors Event Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    
    #Defining Labels
    Ls_id=Label(t,text="SPONSOR ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Le_id=Label(t,text="EVENT ID",bg="black",foreground="snow",font="Baskerville 12 bold")
   
    #Defining Entry Boxes
    s_id=Entry(t)
    e_id=Entry(t)

    #Adding Labels to window
    Ls_id.grid(row=1,column=0)
    Le_id.grid(row=2,column=0)

    #Adding Entry box to window
    s_id.grid(row=1,column=1)
    e_id.grid(row=2,column=1)

    lss=Label(t,text="The available sponsor id and sponsor name are:",font="Baskerville 12 bold",bg="black",foreground="snow")
    lss.grid(row=4,column=0)
    a1=Label(t,text="SPONSOR ID",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=5,column=0)
    a2=Label(t,text="SPONSOR NAME",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=5,column=1)
    find2=("SELECT S_ID,NAME FROM SPONSORS")
    conn.execute(find2)
    c=6
    c1=0
    for row in conn.fetchall():
        for i in range(0,2):
             L1=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold")
             L1.grid(row=c,column=c1,sticky=W)
             c1=c1+1
        c1=0
        c+=1
    ls=Label(t,text="The available event id and event name are:",font="Baskerville 12 bold",bg="black",foreground="snow")
    ls.grid(row=c,column=0)
    a1=Label(t,text="EVENT ID",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=c+1,column=0)
    a2=Label(t,text="EVENT NAME",font="Baskerville 12 bold",bg="black",foreground="snow").grid(row=c+1,column=1)
    find3=("SELECT E_ID,NAME FROM EVENTS")
    conn.execute(find3)
    k=c+3
    c1=0
    for row in conn.fetchall():
        for i in range(0,2):
            L1=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold")
            L1.grid(row=k,column=c1,sticky=W)
            c1=c1+1
        c1=0
        k+=1
    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableSponsor_Event,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=3,column=1)
    connection.commit()

