from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor = connection.cursor()
def disp():
    global eType,t,rowCount
    c=0
    f2=("SELECT S_ID,NAME FROM SPONSORS WHERE TYPE=?")
    cursor.execute(f2,[(eType.get())])
    for m in cursor.fetchall():
        c+=1
    if c==0:
        lab2=Label(t,text="No Sponsor for this type!",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
        rowCount+=1
    else:
        f3=("SELECT S_ID,NAME FROM SPONSORS WHERE TYPE=?")
        cursor.execute(f3,[(eType.get())])
        for row in cursor.fetchall():
            print(row)
            for i in range(0,2):
                lab10=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=i)
            rowCount+=1
            
        l5=Label(t,text="Enter the id of the sponsor whose event sponsored you want: ",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
        rowCount+=1
        e5=Entry(t)
        e5.grid(row=rowCount,column=0)
        rowCount+=1
        b1=Button(t,text="Display",command=lambda:dispEvent(e5.get()),font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
        rowCount+=1
def dispEvent(ID):
    global rowCount,e1
    counter=0
    a1=Label(t,text="EVENTS SPONSORED BY THIS SPONSOR ARE: ").grid(row=rowCount,column=0)
    rowCount+=1
    f2=("SELECT NAME,TOPIC,YEAR,TYPE FROM EVENTS WHERE E_ID=(SELECT E_ID FROM SPONSOR_EVENT WHERE S_ID=?)")
    cursor.execute(f2,[ID])
    for m in cursor.fetchall():
        counter+=1
    if counter==0:
        l5=Label(t,text="This Sponsor has not sponsored any event till now!",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
        rowCount+=1
    else:
        a2=Label(t,text="Name",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
        a3=Label(t,text="Topic",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=1)
        a4=Label(t,text="Year",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=2)
        a5=Label(t,text="Type",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=3)
        rowCount+=1
        f1=("SELECT NAME,TOPIC,YEAR,TYPE FROM EVENTS WHERE E_ID IN (SELECT E_ID FROM SPONSOR_EVENT WHERE S_ID=?)")
        cursor.execute(f1,[ID])
        for row in cursor.fetchall():
            for i in range(0,4):
                l5=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=i)
            rowCount=+1
def name():
    global t,rowCount,e1
    l3=Label(t,text="Following are the sponsor names, please select a sponsor: ",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    
    rowCount+=1
    lid=Label(t,text="Id",bg="black",foreground="snow").grid(row=rowCount,column=0)
    lid=Label(t,text="Name",bg="black",foreground="snow").grid(row=rowCount,column=1)
    rowCount+=1
    cursor.execute("SELECT S_ID,NAME FROM SPONSORS WHERE S_ID IN (SELECT S_ID FROM SPONSOR_EVENT)")
    for row in cursor.fetchall():
        for i in range(0,2):
            l4=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=i)
        rowCount+=1
    l5=Label(t,text="Enter the id of the sponsor whose event sponsored you want: ",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    e1=Entry(t)
    e1.grid(row=rowCount,column=0)
    rowCount+=1
    b1=Button(t,text="Display",command=lambda: dispEvent(e1.get()),font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
    rowCount+=1
        
def type():
    global t,rowCount,eType
    l3=Label(t,text="Following are the sponsor types, please select a sponsor: ",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    cursor.execute("SELECT DISTINCT(TYPE) FROM SPONSORS WHERE S_ID IN (SELECT S_ID FROM SPONSOR_EVENT)")
    for row in cursor.fetchall():
        for i in range(0,1):
            l4=Label(t,text=row,bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=i)
        rowCount+=1
    lab1=Label(t,text="Enter the type of the sponsor you want to explore: ",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    eType=Entry(t)
    eType.grid(row=rowCount,column=0)
    rowCount+=1
    button=Button(t,text="See Sponsors",command=disp,font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
    rowCount+=1   

    
def SponsorCountGUI():
    global t,rowCount
    rowCount=0
    t=Tk()
    t.title("Sponsor Details")
    t.configure(bg="black")
    l1=Label(t,text="This page will show you a sponsor has sponsored how many events till now!",font="Times 20 bold underline",bg="black",foreground="snow").grid(row=rowCount,column=0)
    rowCount+=1
    l2=Label(t,text="Please select the basis on which you want to find your sponsor:",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    b1=Button(t,text="Sponsor Name",command=name,font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
    rowCount+=1
    b2=Button(t,text="Sponsor Type",command=type,font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
    rowCount+=1
