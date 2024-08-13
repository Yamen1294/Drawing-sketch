import tkinter as tk
from tkinter import *


current_color = "black"
def select_color(color):
    global current_color
    current_color = color

def paint(event):
    x,y = event.x , event.y
    canvas.create_oval(x-2,y-2,x+2,y+2,
                        fill = current_color,
                        outline= current_color)

def clear():
    canvas.delete("all")

root = tk.Tk()
root.title("Painting")
root.geometry("1200x600")
root.resizable(False,False)

canvas= tk.Canvas(
    root,
    bg="white",
    width= 1000,
    height= 550
)
canvas.pack()

colors = ['black','red','blue','green','yellow']

for c in colors:
    button = tk.Button(
        root,
        bg=c,
        width=3,
        height=1,
        command= lambda color = c : select_color(color)
    )
    button.pack(side= tk.LEFT)

clear_button= tk.Button(
    root,
    text="Clear",
    command = clear
)
clear_button.pack(side=RIGHT)
canvas.bind('<B1-Motion>',paint)
root.mainloop()