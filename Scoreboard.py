#print details / score board
from tkinter import *
from PIL import Image,ImageTk
from Homepage import *
import sqlite3

connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()
def destructScore(window,val):
    window.destroy()
    ScoreboardGUI(val)
def ScoreboardGUI(e1):
    global sc
    sc=Toplevel()
    #t=Tk()
    #t.title("Scores")
    sc.title("Scoreboard")
    img=ImageTk.PhotoImage(Image.open("bg1.png"))
    lg=Label(sc,image=img).place(x=0,y=0)
    l=Label(sc,text="SCOREBOARD",font="Verdana 30 bold",bg="black",fg="white")
    l.grid(row=0,column=0,sticky=W)
    find1=("SELECT * FROM SCORE WHERE ID=?")
    cursor.execute(find1,[(e1)])
    l0=Label(sc,text="User ID :",font="Verdana 15",bg="black",fg="white").grid(row=1,column=1,sticky=W)
    l1=Label(sc,text="Guess the Logo :",font="Verdana 15",bg="black",fg="white").grid(row=1,column=2,sticky=W)
    l2=Label(sc,text="Tic Tac Toe :",font="Verdana 15",bg="black",fg="white").grid(row=1,column=3,sticky=W)
    l3=Label(sc,text="Snake Game :",font="Verdana 15",bg="black",fg="white").grid(row=1,column=4,sticky=W)
    l4=Label(sc,text="Hangman Game :",font="Verdana 15",bg="black",fg="white").grid(row=1,column=5,sticky=W)
    l5=Label(sc,text="Colour Game :",font="Verdana 15",bg="black",fg="white").grid(row=1,column=6,sticky=W)
    c1=1
    c=2
    for row in cursor.fetchall():
        for i in range(0,6):
            
            l1=Label(sc,text=row[i],bg="black",fg="snow")
            l1.grid(row=c,column=c1)
            c1=c1+1
        c1=1
        c+=1
    b1=Button(sc,text="Play",font="Verdana 20",command=lambda: destructHomepage(sc,e1))
    b1.grid(row=c,column=3)
    sc.mainloop()
    
