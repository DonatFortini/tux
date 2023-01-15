from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import platform
import os

def walk():
    global i, direction
    img = Image.open("image/tuxwalk.gif")
    for frame in ImageSequence.Iterator(img):
        img = ImageTk.PhotoImage(frame)
        label.config(image=img)
        if i >= 375:
            direction = -15
        elif i <= 15:
            direction = 15
        i += direction
        label.place_configure(x=i, y=0)
        time.sleep(0.15)
        root.update()
        
    root.after(1, walk)

def hey(event):
    img = Image.open("image/tux02.gif")
    for frame in ImageSequence.Iterator(img):
        img = ImageTk.PhotoImage(frame)
        label.config(image=img)
        time.sleep(0.2)
        root.update()

root = Tk()
root.overrideredirect(1)
if platform.system() != 'Linux':
    root.config(bg='white')
    label = Label(root, bg='white')
    root.wm_attributes("-transparentcolor", "white")
else:
    label = Label(root)
    root.attributes("-alpha",0.0)

root.geometry("500x170+0+850")


i = 0
direction = 15
label.place(x=0, y=0)
label.bind('<Button-1>', hey)
walk()
root.mainloop()
