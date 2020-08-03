from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableSponsors():
    global s_name,person_contacted,_s_emailID,s_phoneNo,s_add,event_no,past_event_no
    #Creating table if it doesn't exits
    conn.execute("CREATE TABLE IF NOT EXISTS SPONSORS(S_ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,PERSON_CONTACTED TEXT,EMAIL_ID VARCHAR NOT NULL,PHONE_NO INTEGER NOT NULL,WEBSITE VARCHAR NOT NULL,TYPE TEXT)")
    connection.commit()
    #Inserting values into the table
    conn.execute("INSERT INTO SPONSORS(NAME,PERSON_CONTACTED,EMAIL_ID,PHONE_NO,WEBSITE,TYPE) VALUES(?,?,?,?,?,?)",(s_name.get(),person_contacted.get(),s_emailID.get(),s_phoneNo.get(),s_website.get(),s_type.get()))
    connection.commit()
    #Permanantly making changes to the database
    connection.commit()
    #Displaying the data for the user's convenience
    conn.execute("SELECT * FROM SPONSORS")
    for row in conn.fetchall():
        print(row)
    
def SponsorsGUI():
    global s_name,person_contacted,s_emailID,s_phoneNo,s_website,s_type
    #Setting window properties
    t=Tk()
    t.title("Sponsors")
    t.geometry("400x250")
    t.configure(bg="black")
    l1=Label(t,text="Sponsors Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    
    #Defining LAbels
    Lsname=Label(t,text="SPONSOR NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lpc=Label(t,text="PERSON CONTACTED",bg="black",foreground="snow",font="Baskerville 12 bold")
    LemailID=Label(t,text="EMAIL ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    LphoneNo=Label(t,text="PHONE NUMBER",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lweb=Label(t,text="WEBSITE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ltype=Label(t,text="SPONSOR TYPE",bg="black",foreground="snow",font="Baskerville 12 bold")

    #Defining Entry Boxes
    s_name=Entry(t)
    person_contacted=Entry(t)
    s_emailID=Entry(t)
    s_phoneNo=Entry(t)
    s_website=Entry(t)
    s_type=Entry(t)

    #Adding Labels to window
    Lsname.grid(row=2,column=0)
    Lpc.grid(row=3,column=0)
    LemailID.grid(row=4,column=0)
    LphoneNo.grid(row=5,column=0)
    Lweb.grid(row=6,column=0)
    Ltype.grid(row=7,column=0)

    #Adding Entry box to window
    s_name.grid(row=2,column=1)
    person_contacted.grid(row=3,column=1)
    s_emailID.grid(row=4,column=1)
    s_phoneNo.grid(row=5,column=1)
    s_website.grid(row=6,column=1)
    s_type.grid(row=7,column=1)


    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableSponsors,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=11,column=1)
    connection.commit()

