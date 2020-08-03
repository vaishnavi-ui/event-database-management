from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableGuests():
    global g_id,g_name,g_profession,event_no,event_name,g_email,g_phone
    #Creating table if it is not present
    conn.execute("CREATE TABLE IF NOT EXISTS GUESTS(G_ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,PROFESSION TEXT,EMAIL VARCHAR,PHONE_NO INTEGER)")
    #Inserting values to table
    conn.execute("INSERT INTO GUESTS(NAME,PROFESSION,EMAIL,PHONE_NO) VALUES(?,?,?,?)",(g_name.get(),g_profession.get(),g_email.get(),g_phone.get()))
    #Permanently saving the data to the database
    conn.execute("SELECT * FROM GUESTS")
    #Displaying the data on shell for convenince of user
    for row in conn.fetchall():
        print(row)
    
def GuestsGUI():
    global g_id,g_name,g_profession,g_email,g_phone
    #Setting window dimensions
    t=Tk()
    t.title("Guests")
    t.geometry("400x250")
    t.configure(bg="black")
    l1=Label(t,text="Guests Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    #Defining Labels
    Lg_name=Label(t,text="NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lg_profession=Label(t,text="PROFESSION",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lg_email=Label(t,text="EMAIL ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lg_phone=Label(t,text="PHONE NO",bg="black",foreground="snow",font="Baskerville 12 bold")


    #Defining Entry Boxes
    g_name=Entry(t)
    g_profession=Entry(t)
    g_email=Entry(t)
    g_phone=Entry(t)

    #Adding Labels to window
    Lg_name.grid(row=2,column=0)
    Lg_profession.grid(row=3,column=0)
    Lg_email.grid(row=6,column=0)
    Lg_phone.grid(row=7,column=0)


    #Adding Entry box to window
    g_name.grid(row=2,column=1)
    g_profession.grid(row=3,column=1)
    g_email.grid(row=6,column=1)
    g_phone.grid(row=7,column=1)


    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableGuests,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=11,column=1)
    connection.commit()
