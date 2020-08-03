from tkinter import *
from Login import *
from CommitteeMainPage import *
from ExternalMainPage import *

def MainPageGUI():
    mainPage=Tk()
    mainPage.title("Main Page")
    mainPage.configure(bg="black")
    l1=Label(mainPage,text="WELCOME TO EVENT MANAGEMENT SYSTEM",font="Times 20 bold underline",bg="black",foreground="yellow")
    l1.place(x=380,y=20)
    img=PhotoImage(file="events.png")
    lg=Label(mainPage,image=img)
    lg.place(x=300,y=100)
    l2=Label(mainPage,text="Hi, Welcome. Please select what type of user you are. Click on the button!", font="Times 15 bold",bg="black",foreground="snow")
    l2.place(x=380,y=610)
    LExternalUser=Label(mainPage,text="External User (Registering for any event)",font="Times 15 bold",bg="black",foreground="snow")
    LExternalUser.place(x=380,y=640)
    ExternalUser=Button(mainPage,text="Click Here",font="Times 12 bold italic",activebackground="red",command=ExternalMainPageGUI)
    ExternalUser.place(x=800,y=640)
    LCommitteeMember=Label(mainPage,text="Committee Member",font="Times 15 bold",bg="black",foreground="snow")
    LCommitteeMember.place(x=380,y=700)
    CommitteeMember=Button(mainPage,text="Click Here",font="Times 12 bold italic",activebackground="red",command=CommitteeMainPageGUI)
    CommitteeMember.place(x=800,y=700)
    LAdmin=Label(mainPage,text="Admin",font="Times 15",bg="black",foreground="snow")
    LAdmin.place(x=380,y=750)
    Admin=Button(mainPage,text="Click Here",font="Times 12 bold italic",activebackground="red",command=LoginGUI)
    Admin.place(x=800,y=750)
    Names=Label(mainPage,text="Made by : Vaishnavi Rathod and Riya Tendulkar",font="Verdana 10 bold italic",foreground="yellow",bg="black")
    Names.place(x=850,y=820)
    mainPage.mainloop()
MainPageGUI()
