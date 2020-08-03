from tkinter import *
from Admin import *
from Events import *
from Committee import *
from Members import *
from Guests import *
from Audience import *
from Sponsors import *
from Resource import *
class DatabaseAddPage:
    def DatabaseAddPageGUI():
        t=Tk()
        t.title("Main Menu")
        t.geometry("500x500")
        t.configure(bg="black")
        l1=Label(t,text="ADD DETAILS",font="Times 20 bold underline",bg="black",foreground="snow")
        l1.grid(row=0,column=0)
        l2=Label(t,text="On this page you can add details in the database here",font="Times 15",bg="black",foreground="snow")
        l2.grid(row=1,column=0)
        l3=Label(t,text="Click on the button to add the details!",font="Times 15",bg="black",foreground="snow")
        l3.grid(row=2,column=0)

        #Creating LAbels labels 
        Levent=Label(t,text="Event",bg="black",foreground="snow",font="Baskerville 12 bold")
        Lcommittee=Label(t,text="Committee",bg="black",foreground="snow",font="Baskerville 12 bold")
        Lmembers=Label(t,text="Committee Members",bg="black",foreground="snow",font="Baskerville 12 bold")
        Lguest=Label(t,text="Guests",bg="black",foreground="snow",font="Baskerville 12 bold")
        Laudience=Label(t,text="Audience",bg="black",foreground="snow",font="Baskerville 12 bold")
        Lsponsors=Label(t,text="Sponsors",bg="black",foreground="snow",font="Baskerville 12 bold")
        Lresources=Label(t,text="Resources",bg="black",foreground="snow",font="Baskerville 12 bold")
        Ladmin=Label(t,text="Admin",bg="black",foreground="snow",font="Baskerville 12 bold")

        #Adding LAbels
        Levent.grid(row=3,column=0)
        Lcommittee.grid(row=4,column=0)
        Lmembers.grid(row=5,column=0)
        Lguest.grid(row=6,column=0)
        Laudience.grid(row=7,column=0)
        Lsponsors.grid(row=8,column=0)
        Lresources.grid(row=9,column=0)
        Ladmin.grid(row=10,column=0)

        #Creating Buttons
        event=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=EventsGUI)
        committee=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=CommitteeGUI)
        members=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=MembersGUI)
        guest=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=GuestsGUI)
        audience=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=AudienceGUI)
        sponsors=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=SponsorsGUI)
        resources=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=ResourceGUI)
        admin=Button(t,text="Click Here",font="Times 12 bold",activebackground="red",command=AdminGUI)

        #Adding Buttons
        event.grid(row=3,column=1)
        committee.grid(row=4,column=1)
        members.grid(row=5,column=1)
        guest.grid(row=6,column=1)
        audience.grid(row=7,column=1)
        sponsors.grid(row=8,column=1)
        resources.grid(row=9,column=1)
        admin.grid(row=10,column=1)
        t.mainloop()
        
