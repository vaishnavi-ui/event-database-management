from tkinter import *
from Login import *
from CommitteeMainPage import *
from ExternalMainPage import *
def MainPageGUI():
    mainPage=Tk()
    mainPage.title("Main Page")
    mainPage.geometry("640x350")
    mainPage.configure(bg="black")
    l1=Label(mainPage,text="WELCOME TO EVENT MANAGEMENT SYSTEM",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    l2=Label(mainPage,text="Hi, Welcome. Please select what type of user you are. Click on the button!", font="Times 15 bold",bg="black",foreground="snow")
    l2.grid(row=1,column=0)
    LExternalUser=Label(mainPage,text="External User (Registering for any event)",font="Times 15",bg="black",foreground="snow")
    LExternalUser.grid(row=2,column=0)
    ExternalUser=Button(mainPage,text="Click Here",font="Times 10",activebackground="red",command=ExternalMainPageGUI)
    ExternalUser.grid(row=3,column=0)
    LCommitteeMember=Label(mainPage,text="Committee Member",font="Times 15",bg="black",foreground="snow")
    LCommitteeMember.grid(row=4,column=0)
    CommitteeMember=Button(mainPage,text="Click Here",font="Times 10",activebackground="red",command=CommitteeMainPageGUI)
    CommitteeMember.grid(row=5,column=0)
    LAdmin=Label(mainPage,text="Admin",font="Times 15",bg="black",foreground="snow")
    LAdmin.grid(row=6,column=0)
    Admin=Button(mainPage,text="Click Here",font="Times 10",activebackground="red",command=LoginGUI)
    Admin.grid(row=7,column=0)
MainPageGUI()
