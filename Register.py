from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from Homepage import *
import sqlite3

connection=sqlite3.connect("Gaming Arkade.DB")
cursor=connection.cursor()

def destroyRegister(window):
    window.destroy()
    RegisterGUI()
    
def validatePassword(password):
    global r,e1,e2,e3
    if len(e1.get())>0 and len(e2.get())>0 and len(e3.get())>0:
        for ch in e1.get():
            if ch.isdigit():
                messagebox.showerror("Error","Name cannot have digits!")
                break
        sql1="SELECT COUNT(ID) FROM USERS WHERE USERNAME=?"
        cursor.execute(sql1,[(e2.get())])
        val=cursor.fetchone()
        val1=val[0]
        if val1==0: 
            store=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&]).{5,}$")     
            if  re.search(store, password): 
                l1=Label(r,text="Password is valid.",font="Verdana 26",bg="black",fg="white")
                l1.grid(row=13,column=0)
                b2=Button(r,text="Register",command=enter,font="Verdana 20")
                b2.grid(row=14,column=0)
                
            else:
                messagebox.showerror("Error","Password is invalid! Please try another!")

        else:
            messagebox.showerror("Error","This Username already exists! Please try another!")
            
    else:
        messagebox.showerror("Error","Please fill all fields!")
    
def enter():
    global r
    global e1,e2,e3
    find1=("INSERT INTO USERS(NAME,USERNAME,PASSWORD) VALUES(?,?,?)")
    cursor.execute(find1,[(e1.get()),(e2.get()),(e3.get())])
    connection.commit()
    lsuccess=Label(r,text="You have been sucessfully registered! Click to play Games!",font="Verdana 26",bg="black",fg="white")
    lsuccess.grid(row=16,column=0)
    cursor.execute("SELECT MAX(ID) FROM USERS")
    val=cursor.fetchone()
    ID=val[0]
    bplay=Button(r,text="Play",font="Verdana 20",command=lambda: destructHomepage(r,ID))
    bplay.grid(row=17,column=0)

def RegisterGUI():
    global r,e1,e2,e3
    #t=Tk()
    r=Toplevel()
    r.title("Register Page")
    img=ImageTk.PhotoImage(Image.open("bg1.png"))
    lg=Label(r,image=img).place(x=0,y=0)
    #t.configure(bg="black")
    l=Label(r,text="Welcome to Register!",font="Verdana 30 bold italic",bg="black",fg="white")
    l.grid(row=0,column=0)
    l1=Label(r,text="To register,please enter the following details",font="Verdana 26",bg="black",fg="white")
    l1.grid(row=1,column=0)
    
    l2=Label(r,text="NAME",font="Verdana 18",bg="black",fg="white")
    l2.grid(row=2,column=0,sticky=E)
    
    l3=Label(r,text="USERNAME",font="Verdana 18",bg="black",fg="white")
    l3.grid(row=3,column=0,sticky=E)
    
    l4=Label(r,text="PASSWORD",font="Verdana 18",bg="black",fg="white")
    l4.grid(row=4,column=0,sticky=E)
    
    l5=Label(r,text="Please enter a password with following parameters: ",font="Verdana 15",bg="light blue")
    l5.grid(row=5,column=0,sticky=W)
    
    l6=Label(r,text="1. Should have at least one number.",font="Verdana 15",bg="light blue")
    l6.grid(row=6,column=0,sticky=W)
    
    l7=Label(r,text="2. Should have at least one uppercase and one lowercase character.",font="Verdana 15",bg="light blue")
    l7.grid(row=7,column=0,sticky=W)
    
    l8=Label(r,text="3. Should have at least one special symbol.",font="Verdana 15",bg="light blue")
    l8.grid(row=8,column=0,sticky=W)
    
    l9=Label(r,text="4. Should have more than 6 characters.",font="Verdana 15",bg="light blue")
    l9.grid(row=9,column=0,sticky=W)
    
    e1=Entry(r)
    e1.grid(row=2,column=1)
    
    e2=Entry(r)
    e2.grid(row=3,column=1)
    
    e3=Entry(r)
    e3.grid(row=4,column=1)

    b1=Button(r,text=" Check Password ",width=14,height=2,font="Verdana 18",command=lambda: validatePassword(e3.get()))
    b1.grid(row=10,column=0)
    r.mainloop()
   
