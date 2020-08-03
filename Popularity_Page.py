from tkinter import *
import sqlite3
connection = sqlite3.connect("Event_Management.db")
cursor = connection.cursor()

def run():
    global t,ent,ent2
    count=0
    find=("SELECT COUNT(A_ID) FROM COLLEGE_AUDIENCE GROUP BY COLLEGE_AUDIENCE.A_ID HAVING (COLLEGE_AUDIENCE.A_ID=(SELECT E_ID FROM EVENTS WHERE NAME=? AND YEAR=?))")
    cursor.execute(find,[(ent.get()),(ent2.get())])
    val1=cursor.fetchone()
    if val1==None:
        val2=0
    else:
        val2=val1[0]
    count=count+val2
    find1=("SELECT COUNT(EA_ID) FROM EXTERNAL_AUDIENCE GROUP BY EXTERNAL_AUDIENCE.EA_ID HAVING (EXTERNAL_AUDIENCE.EA_ID=(SELECT E_ID FROM EVENTS WHERE NAME=? AND YEAR=?))")
    cursor.execute(find1,[(ent.get()),(ent2.get())])
    val3=cursor.fetchone()
    if val3==None:
        val4=0
    else:
        val4=val3[0]
    count=count+val4
    l5=Label(t,text="THE NUMBER OF PEOPLE WHO ATTENDED THE EVENT ARE:",font="Times 15 bold",bg="black",foreground="snow")
    l5.pack()
    l6=Label(t,text=count,font="Times 15 bold",bg="black",foreground="snow")
    l6.pack()
def PopularityGUI():
    global t,ent,ent2
    t=Tk()
    t.configure(bg="black")
    t.title("Event Popularity")
    l1=Label(t,text="EVENT POPULARITY",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.pack()
    l2=Label(t,text="Here you can choose an event and see how many people registered for that event!",bg="black",foreground="snow",font="Baskerville 12 bold")
    l2.pack()
    l3=Label(t,text="Enter the name of the event",bg="black",foreground="snow",font="Baskerville 12 bold")
    l3.pack()
    ent=Entry(t)
    ent.pack()
    l4=Label(t,text="Select the year in which the event took place",bg="black",foreground="snow",font="Baskerville 12 bold")
    l4.pack()
    ent2=Entry(t)
    ent2.pack()
    b1=Button(t,text="Find",command=run,font="Times 12 bold",activebackground="red")
    b1.pack()


