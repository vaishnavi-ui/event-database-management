from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableEvents():
    global name,topic,location,date,Type,year,website,money,budget,CID
    #Creating table if it is not present
    conn.execute("CREATE TABLE IF NOT EXISTS EVENTS(E_ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL, TOPIC TEXT,EVENT_DATE DATE, WEBSITE VARCHAR, LOCATION TEXT,CHARGE INTEGER,YEAR INTEGER, BUDGET INTEGER,TYPE TEXT,C_ID INTEGER,FOREIGN KEY (C_ID)  REFERENCES COMMITTEE(C_ID))")
    #Inserting values to table
    conn.execute("INSERT INTO EVENTS(NAME,TOPIC,EVENT_DATE,LOCATION,WEBSITE,CHARGE,YEAR,BUDGET,TYPE,C_ID) VALUES(?,?,?,?,?,?,?,?,?,?)",(name.get(),topic.get(),date.get(),location.get(),website.get(),money.get(),year.get(),budget.get(),Type.get(),CID.get()))
    #Permanently saving the data to the database 
    connection.commit()
    #Displaying the data on shell for convenince of user
    conn.execute("SELECT * FROM EVENTS")
    for row in conn.fetchall():
        print(row)

        
def EventsGUI():
    global name,topic,location,date,Type,year,website,money,budget,CID

    #Setting the window properties 
    t=Tk()
    t.title("Events")
    t.geometry("400x400")
    t.configure(bg="black")
    l1=Label(t,text="Events Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)

    #Defining LAbels
    Lname=Label(t,text="NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ltopic=Label(t,text="TOPIC",bg="black",foreground="snow",font="Baskerville 12 bold")
    Llocation=Label(t,text="LOCATION",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ldate=Label(t,text="DATE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ltype=Label(t,text="TYPE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lyear=Label(t,text="YEAR",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lwebsite=Label(t,text="WEBSITE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lmoney=Label(t,text="CHARGE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lbudget=Label(t,text="BUDGET",bg="black",foreground="snow",font="Baskerville 12 bold")
    LCID=Label(t,text="COMMITTEE ID",bg="black",foreground="snow",font="Baskerville 12 bold")
  

    #Defining Entry Boxes
    name=Entry(t)
    topic=Entry(t)
    location=Entry(t)
    date=Entry(t)
    Type=Entry(t)
    year=Entry(t)
    website=Entry(t)
    money=Entry(t)
    budget=Entry(t)
    CID=Entry(t)

    #Adding Labels to window
    Lname.grid(row=1,column=0)
    Ltopic.grid(row=2,column=0)
    Llocation.grid(row=3,column=0)
    Ldate.grid(row=4,column=0)
    Ltype.grid(row=6,column=0)
    Lyear.grid(row=7,column=0)
    Lwebsite.grid(row=8,column=0)
    Lmoney.grid(row=9,column=0)
    Lbudget.grid(row=10,column=0)
    LCID.grid(row=11,column=0)


    #Adding Entry box to window
    name.grid(row=1,column=1)
    topic.grid(row=2,column=1)
    location.grid(row=3,column=1)
    date.grid(row=4,column=1)
    Type.grid(row=6,column=1)
    year.grid(row=7,column=1)
    website.grid(row=8,column=1)
    money.grid(row=9,column=1)
    budget.grid(row=10,column=1)
    CID.grid(row=11,column=1)
    

    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",font="Times 12 bold",activebackground="red",command=creatingTableEvents)
    bSubmit.grid(row=13,column=1)



