from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableResources():
    global r_name,r_price,provider_name,provider_phone,provider_add
    #Creating table if it doesn't exits
    conn.execute("CREATE TABLE IF NOT EXISTS RESOURCES(R_ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,PRICE NUMBER,PROVIDER_NAME VARCHAR,PROVIDER_PHONE_NO INTEGER,PROVIDER_ADDRESS VARCHAR)")
    connection.commit()
    #Inserting values into the table
    conn.execute("INSERT INTO RESOURCES(NAME,PRICE,PROVIDER_NAME,PROVIDER_PHONE_NO,PROVIDER_ADDRESS) VALUES(?,?,?,?,?)",(r_name.get(),r_price.get(),provider_name.get(),provider_phone.get(),provider_add.get()))
    connection.commit()
    #Permanantly making changes to the database
    conn.execute("SELECT * FROM RESOURCES")
    #Displaying the data for the user's convenience
    for row in conn.fetchall():
        print(row)
    
def ResourceGUI():
    global r_name,r_price,provider_name,provider_phone,provider_add
    #Setting window properties
    t=Tk()
    t.title("Resources")
    t.geometry("400x300")
    t.configure(bg="black")
    l1=Label(t,text="Resources Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    #Defining Labels
    Lname=Label(t,text="NAME OF RESOURCE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lprice=Label(t,text="PRICE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lpname=Label(t,text="PROVIDER NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lpphno=Label(t,text="PROVIDER PHONE NO",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lpadd=Label(t,text="PROVIDER ADDRESS",bg="black",foreground="snow",font="Baskerville 12 bold")

    #Defining Entry Boxes
    r_name=Entry(t)
    r_price=Entry(t)
    provider_name=Entry(t)
    provider_phone=Entry(t)
    provider_add=Entry(t)

    #Adding Labels to window
    Lname.grid(row=1,column=0)
    Lprice.grid(row=3,column=0)
    Lpname.grid(row=5,column=0)
    Lpphno.grid(row=6,column=0)
    Lpadd.grid(row=7,column=0)


    #Adding Entry box to window
    r_name.grid(row=1,column=1)
    r_price.grid(row=3,column=1)
    provider_name.grid(row=5,column=1)
    provider_phone.grid(row=6,column=1)
    provider_add.grid(row=7,column=1)


    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableResources,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=11,column=1)
    connection.commit()
