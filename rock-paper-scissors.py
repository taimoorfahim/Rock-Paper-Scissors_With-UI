#import library
from tkinter import *
import random


#initialize window
root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title('Rock,Paper,Scissors')
root.config(bg ='lightskyblue')

#heading
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 30 bold', bg = 'white').pack()

##user choice
user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 19 bold', bg = 'white').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=140 , y = 130)


#computer choice
c_pick = random.randint(1,3)
if c_pick == 1:
    c_pick = 'rock'
elif c_pick ==2:
    c_pick = 'paper'
else:
    c_pick = 'scissors'
    

#play
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == c_pick:
        Result.set('Tie,both are same')
    elif user_pick == 'rock' and c_pick == 'paper':
        Result.set('You loose,computer selected paper')
    elif user_pick == 'rock' and c_pick == 'scissors':
        Result.set('You win,computer selected scissors')
    elif user_pick == 'paper' and c_pick == 'scissors':
        Result.set('You loose,computer selected scissors')
    elif user_pick == 'paper' and c_pick == 'rock':
        Result.set('You win,computer selected rock')
    elif user_pick == 'scissors' and c_pick == 'rock':
        Result.set('You loose,computer selected rock')
    elif user_pick == 'scissors' and c_pick == 'paper':
        Result.set('You win ,computer selected paper')
    else:
        Result.set('invalid, Try again')
    
         
#reset
def Reset():
    Result.set("") 
    user_take.set("")

##exit
def Exit():
    root.destroy()


#button
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 64,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =6,bg ='seashell4' ,command = play).place(x=213,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =6,bg ='seashell4' ,command = Reset).place(x=110,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =6,bg ='seashell4' ,command = Exit).place(x=310,y=310)

root.mainloop()
