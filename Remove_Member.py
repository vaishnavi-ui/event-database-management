from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor = connection.cursor()

def getId(val):
    global Id
    rem=val
    Id=val[0]
    
def Del():
    global e2,t,rowCount
    rem1=("DELETE FROM COMMITTEE_MEMBERS WHERE M_ID=?")
    cursor.execute(rem1,[(e2.get())])
    remov=("DELETE FROM MEMBERS WHERE M_ID=?")
    cursor.execute(remov,[(e2.get())])
    connection.commit()
    l8=Label(t,text="Member deleted from the committee",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    bproceed=Button(t,text="Exit",font="Times 12 bold",activebackground="red",bg="black",foreground="snow",command=lambda: t.destroy()).grid(row=rowCount,column=0)


def dispYear():
    global vari,e2,Id,t,rowCount,e4
    countYear=0
    rowCount+=1
    lid=Label(t,text="ID",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    lname=Label(t,text="Name",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=1)
    lid=Label(t,text="Position",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=2)
    lid=Label(t,text="Date of joining",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=3)
    rowCount+=1
    d=("SELECT M_ID,NAME,POSITION,DOJ FROM MEMBERS WHERE YEAR=? AND C_ID=?")
    cursor.execute(d,[(e4.get()),(Id)])
    for row in cursor.fetchall():
        for i in range(0,4):
            l9=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=i)
        rowCount+=1
        countYear+=1
    rowCount+=1
    if countYear==0:
        lnodata=Label(t,text="No Member available for the year!",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    else:
        l7=Label(t,text="Enter the M_ID of the employee who you want to remove from the committee:",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
        rowCount+=1
        e2=Entry(t)
        e2.grid(row=rowCount,column=0)
        rowCount+=1
        b13=Button(t,text="Delete",command=Del,font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
        rowCount+=1
    
def disp():
    global e1,e2,Id,t,rowCount
    lid=Label(t,text="ID",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    lname=Label(t,text="Name",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=1)
    lid=Label(t,text="Position",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=2)
    lid=Label(t,text="Date of joining",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=3)
    rowCount+=1
    sel=("SELECT M_ID,NAME,POSITION,DOJ FROM MEMBERS WHERE POSITION=? AND C_ID=?")
    cursor.execute(sel,[e1.get(),Id])
    for row in cursor.fetchall():
        for i in range(0,4):
            l6=Label(t,text=row[i],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=i)
        rowCount+=1
        print(row)
    l7=Label(t,text="Enter the M_ID of the employee who you want to remove from the committee:",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    e2=Entry(t)
    e2.grid(row=rowCount,column=0)
    rowCount+=1    
    b6=Button(t,text="Delete",command=Del).grid(row=rowCount,column=0)
    rowCount+=1

    
def deletePosition():
    global Id,t,e1,rowCount
    cnt=0
    l3=Label(t,text="Following positions are availabe for deleting:",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    find=("SELECT DISTINCT(POSITION) FROM MEMBERS WHERE C_ID=?")
    cursor.execute(find,[(Id)])
    for row in cursor.fetchall():
        l4=Label(t,text=row[0],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
        rowCount+=1
    l5=Label(t,text="Please enter any one of the positions:",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    e1=Entry(t)
    e1.grid(row=rowCount,column=0)
    rowCount+=1
    b5=Button(t,text="Proceed",command=disp,font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
    rowCount+=1    

        
def deleteYear():
    global e4,t,rowCount
    vari=IntVar()
    l9=Label(t,text="Enter the year from which you want to remove the employee from:",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    find=("SELECT DISTINCT(YEAR) FROM MEMBERS WHERE C_ID=?")
    cursor.execute(find,[(Id)])
    for row in cursor.fetchall():
        l4=Label(t,text=row[0],bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
        rowCount+=1
    l5=Label(t,text="Please enter any one of the year:",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=rowCount,column=0)
    rowCount+=1
    e4=Entry(t)
    e4.grid(row=rowCount,column=0)
    rowCount+=1
    b5=Button(t,text="Proceed",command=dispYear,font="Times 12 bold",activebackground="red").grid(row=rowCount,column=0)
    rowCount+=1    



def RemoveMemberGUI():
    global t,var,rowCount
    rowCount=5
    t=Tk()
    t.configure(bg="black")
    t.title("Remove Member")
    l1=Label(t,text="REMOVE COMMITTEE MEMBERS",bg="black",foreground="snow",font="Baskerville 12 bold underline").grid(row=0,column=0)
    l2=Label(t,text="Select the parameter:",bg="black",foreground="snow",font="Baskerville 12 bold").grid(row=1,column=0)     
    b1=Button(t,text="Position",command=deletePosition,font="Times 12 bold",activebackground="red",bg="black",foreground="snow").grid(row=2,column=0)
    b2=Button(t,text="Year",command=deleteYear,font="Times 12 bold",activebackground="red",bg="black",foreground="snow").grid(row=3,column=0)

