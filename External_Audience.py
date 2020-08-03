from tkinter import *
from tkinter import messagebox
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableExternal_Audience():
    global ea_id,ea_name,college_name,ea_email,ea_phone
    #Creating table if it doesn't exits
    conn.execute("CREATE TABLE IF NOT EXISTS EXTERNAL_AUDIENCE(EA_ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,COLLEGE_NAME TEXT NOT NULL,EMAIL VARCHAR NOT NULL,PHONE NUMBER NOT NULL)")
    connection.commit()
    #Inserting values into the table
    conn.execute("INSERT INTO EXTERNAL_AUDIENCE(NAME,COLLEGE_NAME,EMAIL,PHONE) VALUES(?,?,?,?)",(ea_name.get(),college_name.get(),ea_email.get(),ea_phone.get()))
    connection.commit()
    #Permanantly making changes to the database
    conn.execute("SELECT * FROM EXTERNAL_AUDIENCE")
    #Displaying the data for the user's convenience
    for row in conn.fetchall():
        print(row)
    conn.execute("SELECT MAX(EA_ID) FROM EXTERNAL_AUDIENCE")
    val=conn.fetchone()
    str1="Registered! Your ID is: "+str(val[0])
    messagebox.showinfo("ID",str1)  
    
def External_AudienceGUI():
    global ea_id,ea_name,college_name,ea_email,ea_phone
    #Setting window properties
    t=Tk()
    t.title("External Audience")
    t.geometry("500x300")
    t.configure(bg="black")
    l1=Label(t,text="External Audience Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    #Defining Labels
    Lname=Label(t,text="NAME OF AUDIENCE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lcollege_name=Label(t,text="COLLEGE NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lemail=Label(t,text="EMAIL ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lphone=Label(t,text="PHONE NO",bg="black",foreground="snow",font="Baskerville 12 bold")
    
    

    #Defining Entry Boxes
    ea_name=Entry(t)
    college_name=Entry(t)
    ea_email=Entry(t)
    ea_phone=Entry(t)
    

    #Adding Labels to window
    Lname.grid(row=2,column=0)
    Lcollege_name.grid(row=3,column=0)
    Lemail.grid(row=4,column=0)
    Lphone.grid(row=5,column=0)
    

    #Adding Entry box to window
    ea_name.grid(row=2,column=1)
    college_name.grid(row=3,column=1)
    ea_email.grid(row=4,column=1)
    ea_phone.grid(row=5,column=1)
   

    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableExternal_Audience,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=10,column=1)
    connection.commit()



