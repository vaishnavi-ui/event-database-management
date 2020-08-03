from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor= connection.cursor()
def destructTotalCost(window):
    window.destroy()
    TotalCostGUI()
    
def getID(val):
    global Id
    rem=val
    Id=val[0]
    
def calculate():
    global t,e1,rowCount
    spent=0
    rec=0

    #Price of the event
    f9="SELECT CHARGE FROM EVENTS WHERE E_ID=?"
    cursor.execute(f9,[(e1.get())])
    val13=cursor.fetchone()
    price=val13[0]
    print("Price: ",price)

    #Charges for guests
    f1=("SELECT SUM(CHARGE) FROM GUEST_EVENT WHERE E_ID=?")
    cursor.execute(f1,[(e1.get())])
    val=cursor.fetchone()    
    val1=val[0]
    spent=spent+val1

    #Charges for resources
    f2=("SELECT R_ID,QUANTITY FROM RESOURCE_EVENT WHERE E_ID=?")
    cursor.execute(f2,[(e1.get())])
    val2=cursor.fetchall()             
    for row in val2:
        f3=("SELECT PRICE FROM RESOURCES WHERE R_ID=?")
        cursor.execute(f3,[(row[0])])
        val3=cursor.fetchone()
        val4=val3[0]
        spent=spent+(val4*row[1])

    #Money recieved from college audience
    f4=("SELECT COUNT(A_ID) FROM CAUDIENCE_EVENT WHERE E_ID=?")
    cursor.execute(f4,[(e1.get())])
    val5=cursor.fetchone()
    val6=val5[0]
    val14=price*val6
    print("college: ",val14)
    rec=rec+val14

    #Money recieved from external audience
    f5=("SELECT COUNT(EA_ID) FROM EAUDIENCE_EVENT WHERE E_ID=?")
    cursor.execute(f5,[(e1.get())])
    val7=cursor.fetchone()
    val8=val7[0]
    val15=val8*price
    rec=rec+val15
    print("external: ",val15)
    totalspent=spent-rec
    f6=("SELECT BUDGET FROM EVENTS WHERE E_ID=?")
    cursor.execute(f6,[(e1.get())])
    val9=cursor.fetchone()
    val10=val9[0]
    f9=("SELECT C_ID FROM EVENTS WHERE E_ID=?")
    cursor.execute(f9,[(e1.get())])
    val13=cursor.fetchone()
    cid=val13[0]
    f7=("SELECT FUNDS FROM COMMITTEE WHERE C_ID=?")
    cursor.execute(f7,[(cid)])
    val11=cursor.fetchone()
    val12=val11[0]
    saved=val10-totalspent
    finBudget=val12+saved
    f8=("UPDATE COMMITTEE SET FUNDS=? WHERE C_ID=?")
    cursor.execute(f8,[(finBudget),(cid)])
    str1="THE TOTAL MONEY SPENT FOR THIS EVENT(RESOURCE + GUEST CHARGERS) IS: RS. "+str(spent)
    str2="THE TOTAL MONEY RECIEVED FROM AUDIENCE: RS. "+str(rec)
    str3="MONEY REMAINING IN EVENT BUDGET: RS. "+str(saved)
    str5="THE UPDATED FUNDS OF THE COMMITTEE IS NOW : RS. "+str(finBudget)
    str4="CURRENT ORIGINAL FUNDS OF THE COMMITTEE: RS. "+str(val12)
    rowCount=rowCount+1
    l2=Label(t,text=str1,font="Times 12 bold",bg="black",foreground="snow").grid(row=rowCount,column=0)
    rowCount=rowCount+1
    l3=Label(t,text=str2,font="Times 12 bold",bg="black",foreground="snow").grid(row=rowCount,column=0)
    rowCount=rowCount+1
    l4=Label(t,text=str3,font="Times 12 bold",bg="black",foreground="snow").grid(row=rowCount,column=0)
    rowCount=rowCount+1
    l5=Label(t,text=str4,font="Times 12 bold",bg="black",foreground="snow").grid(row=rowCount,column=0)
    rowCount=rowCount+1
    l6=Label(t,text=str5,font="Times 12 bold",bg="black",foreground="snow").grid(row=rowCount,column=0)
    rowCount=rowCount+1

def TotalCostGUI():
    global e1,t,Id,rowCount
    t=Tk()
    rowCount=4
    t.configure(bg="black")
    t.title("Calculating Total Cost")
    l=Label(t,text="HERE YOU CAN DO THE COST EVALUATION OF THE EVENT!",font="Times 16 bold",bg="black",foreground="snow")
    l.grid(row=0,column=0)
    la=Label(t,text="The event available for your committee are: ",font="Times 12 italic",bg="black",foreground="snow").grid(row=1,column=0)
    lid=Label(t,text="ID",font="Times 12 italic",bg="black",foreground="snow").grid(row=2,column=0)
    lname=Label(t,text="Name",font="Times 12 italic",bg="black",foreground="snow").grid(row=2,column=1)
    lyear=Label(t,text="Year",font="Times 12 italic",bg="black",foreground="snow").grid(row=2,column=2)
    f=("SELECT E_ID,NAME,YEAR FROM EVENTS WHERE C_ID=?")
    cursor.execute(f,[(Id)])
    for row in cursor.fetchall():
        for i in range(0,3):
            lt=Label(t,text=row[i],font="Times 12 bold",bg="black",foreground="snow").grid(row=rowCount,column=i)
        rowCount=rowCount+1
    rowCount=rowCount+1    
    l1=Label(t,text="Enter the event id whose cost is to be calculated: ",font="Times 15 italic",bg="black",foreground="snow").grid(row=rowCount,column=0)
    rowCount=rowCount+1
    e1=Entry(t)
    e1.grid(row=rowCount,column=0)
    rowCount=rowCount+1
    b1=Button(t,text="Submit",font="Times 10",activebackground="red",command=calculate).grid(row=rowCount,column=0)
    rowCount=rowCount+1

    

    
