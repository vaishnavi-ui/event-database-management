from tkinter import *
from SnakeGame import *

from PIL import Image,ImageTk,ImageOps

def SnakeGameGUI(ID):
    sn=Toplevel()
    #sn=Tk()
    sn.title("Snake Game")
    sn.configure(bg="black")
    sn.geometry("700x700")
    l=Label(sn,text="SNAKE GAME",bg="aqua",font=("Fantasy",30,"bold italic"),width=22)
    l.pack()
    l1=Label(sn,text="Welcome to the snake game",bg="paleturquoise",font=("Fantasy",30,"bold italic"),width=22)
    l1.pack()
    l2=Label(sn,text="The snake of the game is hungry and wants food.",bg="paleturquoise",font=("Fantasy",15,"bold italic"),width=44).pack()
    l3=Label(sn,text="It is your responsibility to feed him the food!",bg="paleturquoise",font=("Fantasy",15,"bold italic"),width=44).pack()
    l3=Label(sn,text="Use your  arrow keys to navigate the snake to the food!",bg="paleturquoise",font=("Fantasy",15,"bold italic"),width=44).pack()
    l4=Label(sn,text="BUT BEWARE!",bg="paleturquoise",font=("Fantasy",15,"bold italic"),fg="red",width=44).pack()
    l5=Label(sn,text="Your snake can die if you are not careful!",bg="paleturquoise",font=("Fantasy",15,"bold italic"),width=44).pack()
    l6=Label(sn,text="Make sure the snake does not hit itself,",bg="paleturquoise",font=("Fantasy",15,"bold italic"),width=44).pack()
    l9=Label(sn,text="or the screen borders or it will die!",bg="paleturquoise",font=("Fantasy",15,"bold italic"),width=44).pack()
    l7=Label(sn,text="Everytime the snake gets some food,",bg="paleturquoise",font=("Fantasy",15,"bold italic"),width=44).pack()
    l8=Label(sn,text="it will get energy & speed up and you will get 10 points!",bg="paleturquoise",font=("Fantasy",15,"bold italic"),width=44).pack()
    i3=ImageTk.PhotoImage(Image.open("Snake.png"))
    l3=Label(sn,image=i3,bg="paleturquoise",width=530).pack()
    b1=Button(sn,text="Play",bg="aqua",font=("Fantasy",15,"bold italic"),width=44,command=lambda: destructMain(sn,ID)).pack()
    #b2=Button(sn,text="Go back",bg="aqua",font=("Fantasy",15,"bold italic"),width=44,command=lambda: d(sn,ID)).pack()
    sn.mainloop()

