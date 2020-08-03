from tkinter import *
from DatabaseAddPage import *
from College_Audience import *
from External_Audience import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
conn= connection.cursor()
def enterExternalAudience():
    conn.execute("INSERT INTO EAUDIENCE_EVENT VALUES(?,?)",(s,e))
    connection.commit()

def enterCollegeEvent(s,e):
    conn.execute("INSERT INTO CAUDIENCE_EVENT VALUES(?,?)",(s,e))
    connection.commit()
def external():
    global t
    t.destroy()
    col=Tk()
    col.title("External Audience for Event")
    col.geometry("450x160")
    col.configure(bg="black")
    l1=Label(col,text="External Audience for Event",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    
    #Defining Labels
    Ls_id=Label(col,text="AUDIENCE ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Le_id=Label(col,text="EVENT ID",bg="black",foreground="snow",font="Baskerville 12 bold")
   
    #Defining Entry Boxes
    s_id=Entry(col)
    e_id=Entry(col)

    #Adding Labels to window
    Ls_id.grid(row=1,column=0)
    Le_id.grid(row=2,column=0)

    #Adding Entry box to window
    s_id.grid(row=1,column=1)
    e_id.grid(row=2,column=1)
    b1=Button(col,text="Submit",font="Times 12 bold",activebackground="red",command=lambda: enterExternalEvent(s_id.get(),e_id.get())).grid(row=3,column=0)    
def college():
    global t
    t.destroy()
    col=Tk()
    col.title("College Audience for Event")
    col.geometry("450x160")
    col.configure(bg="black")
    l1=Label(col,text="College Audience for Event",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    
    #Defining Labels
    Ls_id=Label(col,text="AUDIENCE ID",bg="black",foreground="snow",font="Baskerville 12 bold")
    Le_id=Label(col,text="EVENT ID",bg="black",foreground="snow",font="Baskerville 12 bold")
   
    #Defining Entry Boxes
    s_id=Entry(col)
    e_id=Entry(col)

    #Adding Labels to window
    Ls_id.grid(row=1,column=0)

    Le_id.grid(row=2,column=0)


    #Adding Entry box to window
    s_id.grid(row=1,column=1)

    e_id.grid(row=2,column=1)

    b1=Button(col,text="Submit",font="Times 12 bold",activebackground="red",command=lambda: enterCollegeEvent(s_id.get(),e_id.get())).grid(row=4,column=0)
def registerForEvent():
    global t,rowCount
    lcollege=Label(t,text="College Student",bg="black",foreground="snow",font="Baskerville 12 bold")
    lexternal=Label(t,text="Outside College Student",bg="black",foreground="snow",font="Baskerville 12 bold")

    #Adding Label
    c1=rowCount
    lcollege.grid(row=rowCount,column=0)
    rowCount+=1
    c2=rowCount
    lexternal.grid(row=rowCount,column=0)
    rowCount+=1

    #Creating Buttons
    College=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=college)
    External=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=external)

    #Adding Pages
    College.grid(row=c1,column=1)

    External.grid(row=c2,column=1)

    

def register():
    global t,rowCount
    #Setting Label
    Lcollege=Label(t,text="College Student",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lexternal=Label(t,text="Outside College Student",bg="black",foreground="snow",font="Baskerville 12 bold")

    #Adding Label
    c1=rowCount
    Lcollege.grid(row=rowCount,column=0)
    rowCount+=1
    c2=rowCount
    Lexternal.grid(row=rowCount,column=0)
    rowCount+=1
    #Creating Buttons
    college=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=College_AudienceGUI)
    external=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=External_AudienceGUI)

    #Adding Pages
    college.grid(row=c1,column=1)
    external.grid(row=c2,column=1)
 
    
def AudienceGUI():
    global t,rowCount
    t=Tk()
    t.geometry("500x250")
    t.title("Audience Page")
    t.configure(bg="black")
    rowCount=5
    l1=Label(t,text="ADD DETAILS FOR AUDIENCE",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    l2=Label(t,text="Select what type of audience you are",font="Times 15",bg="black",foreground="snow")
    l2.grid(row=2,column=0)
    b1=Button(t,text="Register for event",font="Times 12 bold",activebackground="red",command=registerForEvent).grid(row=3,column=0)
    b2=Button(t,text="Register",font="Times 12 bold",activebackground="red",command=register).grid(row=4,column=0)

    

