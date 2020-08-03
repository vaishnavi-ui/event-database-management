from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableCommittee():
    global comm_name,comm_email,comm_website,headed_by,Type,money_available
    #Creating table if it is not present
    conn.execute("CREATE TABLE IF NOT EXISTS COMMITTEE(C_ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, HEAD TEXT NOT NULL, FUNDS INTEGER, WEBSITE VARCHAR, EMAIL_ID VARCHAR, TYPE TEXT)")
    #Inserting values to table
    conn.execute("INSERT INTO COMMITTEE(NAME,HEAD,FUNDS,WEBSITE,EMAIL_ID,TYPE) VALUES(?,?,?,?,?,?)",(comm_name.get(),headed_by.get(),money_available.get(),comm_website.get(),comm_email.get(),Type.get()))
    #Permanently saving the data to the database 
    connection.commit()
    #Displaying the data on shell for convenince of user
    conn.execute("SELECT * FROM COMMITTEE")
    for row in conn.fetchall():
        print(row)
    
def CommitteeGUI():
    global comm_name,comm_email,comm_website,headed_by,Type,money_available
    #Setting properties of the window
    t=Tk()
    t.title("Committee")
    t.configure(bg="black")
    t.geometry("400x300")
    l1=Label(t,text="Committee Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)

    #Defining LAbels
    Lcomm_name=Label(t,text="NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lemail=Label(t,text="EMAIL ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lweb=Label(t,text="WEBSITE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lhead=Label(t,text="HEADED BY",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ltype=Label(t,text="TYPE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lmoney=Label(t,text="FUNDS",bg="black",foreground="snow",font="Baskerville 12 bold")

    #Defining Entry Boxes

    comm_name=Entry(t)  
    comm_email=Entry(t)
    comm_website=Entry(t)
    headed_by=Entry(t) 
    Type=Entry(t)
    money_available=Entry(t)

    #Adding Labels to window
    
    Lcomm_name.grid(row=2,column=0)    
    Lemail.grid(row=3,column=0)
    Lweb.grid(row=4,column=0)
    Lhead.grid(row=5,column=0)
    Ltype.grid(row=6,column=0)
    Lmoney.grid(row=7,column=0)

    #Adding Entry box to window
  
    comm_name.grid(row=2,column=1)    
    comm_email.grid(row=3,column=1)
    comm_website.grid(row=4,column=1)
    headed_by.grid(row=5,column=1)   
    Type.grid(row=6,column=1)
    money_available.grid(row=7,column=1)


    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableCommittee,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=11,column=1)
    connection.commit()

