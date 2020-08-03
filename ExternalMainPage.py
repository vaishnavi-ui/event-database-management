from tkinter import *
from Audience import *
from Popularity_Page import *
from Search import *
from Sort import *
from Upcoming import *
from Display_Guests import *
from Sponsor_Count import *
def ExternalMainPageGUI():
    t=Tk()
    t.configure(bg="black")
    l1=Label(t,text="Welcome Audience!",font="Times 20 bold underline",bg="black",foreground="snow")
    l1.grid(row=0,column=0)
    l2=Label(t,text="Select what you would like to do next!",bg="black",foreground="snow",font="Baskerville 12 bold")
    l2.grid(row=1,column=0)

    #Creating Label
    LseeEvent=Label(t,text="See Upcoming Events",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lsort=Label(t,text="Sort Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lsearch=Label(t,text="Search Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lpop=Label(t,text="See Popularity of Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lguest=Label(t,text="See Guests of Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lspon=Label(t,text="See Sponsors for Event",bg="black",foreground="snow",font="Baskerville 12 bold")
    Lregister=Label(t,text="Register for Event",bg="black",foreground="snow",font="Baskerville 12 bold")

    #Adding Events
    LseeEvent.grid(row=4,column=0)
    Lsort.grid(row=5,column=0)
    Lsearch.grid(row=6,column=0)
    Lpop.grid(row=7,column=0)
    Lguest.grid(row=8,column=0)
    Lspon.grid(row=9,column=0)
    Lregister.grid(row=10,column=0)

    #Adding Buttons
    seeEvent=Button(t,text="Click Here",command=upcomingGUI,font="Times 12 bold",activebackground="red")
    sort=Button(t,text="Click Here",command=sortGUI,font="Times 12 bold",activebackground="red")
    search=Button(t,text="Click Here",command=searchGUI,font="Times 12 bold",activebackground="red")
    pop=Button(t,text="Click Here",command=PopularityGUI,font="Times 12 bold",activebackground="red")
    guest=Button(t,text="Click Here",command=DisplayGuestsGUI,font="Times 12 bold",activebackground="red")
    spon=Button(t,text="Click Here",command=SponsorCountGUI,font="Times 12 bold",activebackground="red")
    register=Button(t,text="Click Here",command=AudienceGUI,font="Times 12 bold",activebackground="red")

    #Adding Buttons
    seeEvent.grid(row=4,column=1)
    sort.grid(row=5,column=1)
    search.grid(row=6,column=1)
    pop.grid(row=7,column=1)
    guest.grid(row=8,column=1)
    spon.grid(row=9,column=1)
    register.grid(row=10,column=1)
    t.mainloop()

