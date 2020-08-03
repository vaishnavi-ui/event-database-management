from tkinter import *
from tkinter import messagebox
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()


def creatingTableCollege_Audience():
    global a_id,a_name,college_id,a_email,a_phone,a_branch,a_course,a_year
    #Creating table if it doesn't exits
    conn.execute("CREATE TABLE IF NOT EXISTS COLLEGE_AUDIENCE(A_ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,COLLEGE_ID INTEGER NOT NULL,EMAIL VARCHAR NOT NULL,PHONE_NUMBER NOT NULL,BRANCH TEXT,COURSE TEXT,YEAR NUMBER)")
    connection.commit()
    #Inserting values into the table
    conn.execute("INSERT INTO COLLEGE_AUDIENCE(NAME,COLLEGE_ID,EMAIL,PHONE_NUMBER,BRANCH,COURSE,YEAR) VALUES(?,?,?,?,?,?,?)",(a_name.get(),college_id.get(),a_email.get(),a_phone.get(),a_branch.get(),a_course.get(),a_year.get()))
    connection.commit()
    #Permanantly making changes to the database
    conn.execute("SELECT * FROM COLLEGE_AUDIENCE")
    #Displaying the data for the user's convenience
    for row in conn.fetchall():
        print(row)
    conn.execute("SELECT MAX(A_ID) FROM COLLEGE_AUDIENCE")
    val=conn.fetchone()
    str1="Registered! Your ID is: "+str(val[0])
    messagebox.showinfo("ID",str1) 
    
def College_AudienceGUI():
    global a_id,a_name,college_id,a_email,a_phone,a_branch,a_course,a_year
    #Setting window properties
    t=Tk()
    t.title("College Audience")
    t.geometry("500x350")
    t.configure(bg="black")
    l1=Label(t,text="College Audience Details",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    #Defining Labels
    Lname=Label(t,text="NAME OF AUDIENCE",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lcollege_id=Label(t,text="COLLEGE ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lemail=Label(t,text="EMAIL ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lphone=Label(t,text="PHONE NO",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lbranch=Label(t,text="BRANCH NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lcourse=Label(t,text="COURSE NAME",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lyear=Label(t,text="YEAR",bg="black",foreground="snow",font="Baskerville 12 bold")
    
    

    #Defining Entry Boxes
    a_name=Entry(t)
    college_id=Entry(t)
    a_email=Entry(t)
    a_phone=Entry(t)
    a_branch=Entry(t)
    a_course=Entry(t)
    a_year=Entry(t)
    money_paid=Entry(t)
    e_id=Entry(t)
    e_name=Entry(t)

    #Adding Labels to window

    Lname.grid(row=2,column=0)
    Lcollege_id.grid(row=3,column=0)
    Lemail.grid(row=4,column=0)
    Lphone.grid(row=5,column=0)
    Lbranch.grid(row=8,column=0)
    Lcourse.grid(row=9,column=0)
    Lyear.grid(row=10,column=0)
    

    #Adding Entry box to window
   
    a_name.grid(row=2,column=1)
    college_id.grid(row=3,column=1)
    a_email.grid(row=4,column=1)
    a_phone.grid(row=5,column=1)
    a_branch.grid(row=8,column=1)
    a_course.grid(row=9,column=1)
    a_year.grid(row=10,column=1)
   

    #Recieving and passing all the values
    bSubmit=Button(t,text="Submit",command=creatingTableCollege_Audience,font="Times 12 bold",activebackground="red")
    bSubmit.grid(row=14,column=1)
    connection.commit()



