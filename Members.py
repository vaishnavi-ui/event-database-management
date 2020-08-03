from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()

def creatingTableCommitteeMembers():
    global name,emailID,phoneNo,birthdate,course,branch,year,position,doj,cid
    #Creating table if it is not present
    conn.execute("CREATE TABLE IF NOT EXISTS MEMBERS(M_ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,PHONE_NO INTEGER, DOB DATE,COURSE TEXT,BRANCH TEXT,YEAR INTEGER,POSITION TEXT,DOJ DATE,C_ID INTEGER,FOREIGN KEY (C_ID)  REFERENCES COMMITTEE(C_ID))")
    #Inserting values to table
    conn.execute("INSERT INTO MEMBERS(NAME,PHONE_NO,DOB,COURSE,BRANCH,YEAR,POSITION,DOJ,C_ID) VALUES(?,?,?,?,?,?,?,?,?)",(name.get(),phoneNo.get(),birthdate.get(),course.get(),branch.get(),year.get(),position.get(),doj.get(),cid.get()))
    conn.execute("INSERT INTO COMMITTEE_MEMBERS(M_ID,C_ID) VALUES (?,?)",(conn.lastrowid,cid.get()))
    #Permanently saving the data to the database
    connection.commit()
    #Displaying the data on shell for convenince of user
    conn.execute("SELECT * FROM MEMBERS")
    for row in conn.fetchall():
        print(row)
    
def MembersGUI():
    global name,emailID,phoneNo,birthdate,course,branch,year,position,doj,cid
    #Setting window dimensions
    t=Tk()
    t.title("Committee Members")
    t.geometry("500x370")
    t.configure(bg="black")
    l1=Label(t,text="Committee Members Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    
    #Defining LAbels
    Lname=Label(t,text="NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    LemailID=Label(t,text="EMAIL ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    LphoneNo=Label(t,text="PHONE NUMBER",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lbirthdate=Label(t,text="BIRTHDATE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lcourse=Label(t,text="COURSE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lbranch=Label(t,text="BRANCH",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lyear=Label(t,text="YEAR",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lposition=Label(t,text="POSITION",bg="black",foreground="snow",font="Baskerville 12 bold")
    Ldoj=Label(t,text="DATE OF JOINING",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lcid=Label(t,text="COMMITTEE ID",bg="black",foreground="snow",font="Baskerville 12 bold")

    #Defining Entry Boxes
    name=Entry(t)
    emailID=Entry(t)
    phoneNo=Entry(t)
    birthdate=Entry(t)
    course=Entry(t)
    branch=Entry(t)
    year=Entry(t)
    position=Entry(t)
    doj=Entry(t)
    cid=Entry(t)

    #Adding Labels to window
    Lname.grid(row=1,column=0)
    LemailID.grid(row=2,column=0)
    LphoneNo.grid(row=3,column=0)
    Lbirthdate.grid(row=5,column=0)
    Lcourse.grid(row=6,column=0)
    Lbranch.grid(row=7,column=0)
    Lyear.grid(row=8,column=0)
    Lposition.grid(row=9,column=0)
    Ldoj.grid(row=10,column=0)
    Lcid.grid(row=11,column=0)

    #Adding Entry box to window
    name.grid(row=1,column=1)
    emailID.grid(row=2,column=1)
    phoneNo.grid(row=3,column=1)
    birthdate.grid(row=5,column=1)
    course.grid(row=6,column=1)
    branch.grid(row=7,column=1)
    year.grid(row=8,column=1)
    position.grid(row=9,column=1)
    doj.grid(row=10,column=1)
    cid.grid(row=11,column=1)

    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableCommitteeMembers,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=12,column=1)

