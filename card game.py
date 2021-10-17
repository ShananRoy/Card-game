from tkinter import *
import random
from PIL import ImageTk, Image

root=Tk()
root.title("Card Game")
root.geometry("500x500")
root.configure(background="yellow")

img=ImageTk.PhotoImage(Image.open("Pikachu.jpg"))
player1=Label(root,text="player1",bg="blue",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,text="player2",bg="blue",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1score=Label(root,bg="blue",fg="white")
player1score.place(relx=0.1,rely=0.4,anchor=CENTER)

player2score=Label(root,bg="blue",fg="white")
player2score.place(relx=0.9,rely=0.4,anchor=CENTER)

randomdice=Label(root,bg="brown",fg="white")
randomdice.place(relx=0.5,rely=0.5,anchor=CENTER)

player1scorevalue=0
def player1():
    global player1scorevalue
    randomnumber=random.randint(1, 6)
    randomdice["text"]="player1 dice random CARD:"+str(randomCARD)
    player1scorevalue=player1scorevalue+randomnumber
    player1score["text"] = str( player1scorevalue)
     
player2scorevalue=0
def player2():
    global player2scorevalue
    randomnumber2=random.randint(1, 6)
    randomdice["text"]="player2 dice random CARD:"+str(randomCARD)
    player2scorevalue=player2scorevalue+randomnumber2
    player2score["text"] = str( player2scorevalue) 
    
player_1_btn=Button(root, image = img, command=player1)
player_1_btn.place(relx= 0.1,rely = 0.6, anchor = CENTER)
    
player_2_btn=Button(root, image = img, command=player2)
player_2_btn.place(relx= 0.9,rely = 0.6, anchor = CENTER)
    
root.mainloop()