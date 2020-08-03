from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableAdmin():
    global username,password,ad_name,ad_phone,ad_email
    conn.execute("CREATE TABLE IF NOT EXISTS ADMIN(U_ID INTEGER PRIMARY KEY AUTOINCREMENT,USERNAME VARCHAR,PASSWORD VARCHAR,NAME TEXT,PHONE NUMBER,EMAIL VARCHAR)")
    conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD,NAME,PHONE,EMAIL) VALUES(?,?,?,?,?)",(username.get(),password.get(),ad_name.get(),ad_phone.get(),ad_email.get()))
    connection.commit()
    conn.execute("SELECT * FROM ADMIN")
    for row in conn.fetchall():
        print(row)
    
def AdminGUI():
    t=Tk()
    t.title("Admin")
    t.geometry("400x300")
    t.configure(bg="black")
    l1=Label(t,text="Admin Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    global username,password,ad_name,ad_phone,ad_email
    #Defining LAbels
    Luser=Label(t,text="USERNAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lpass=Label(t,text="PASSWORD",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ladname=Label(t,text="ADMIN NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ladphone=Label(t,text="ADMIN PHONE NO",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lademail=Label(t,text="ADMIN EMAIL ID",bg="black",foreground="snow",font="Baskerville 12 bold")


    #Defining Entry Boxes
    username=Entry(t)
    password=Entry(t)
    ad_name=Entry(t)
    ad_phone=Entry(t)
    ad_email=Entry(t)


    #Adding Labels to window
    Luser.grid(row=1,column=0)
    Lpass.grid(row=2,column=0)
    Ladname.grid(row=3,column=0)
    Ladphone.grid(row=4,column=0)
    Lademail.grid(row=5,column=0)

    #Adding Entry box to window
    username.grid(row=1,column=1)
    password.grid(row=2,column=1)
    ad_name.grid(row=3,column=1)
    ad_phone.grid(row=4,column=1)
    ad_email.grid(row=5,column=1)

    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableAdmin,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=11,column=1)

