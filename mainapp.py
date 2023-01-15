from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time

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
screen_height = root.winfo_screenheight()
window_height = root.winfo_height()
root.geometry("500x170+0+850")
root.overrideredirect(1)

root.config(bg='white')
i = 0
direction = 15
label = Label(root, bg='white')
label.place(x=0, y=0)
root.wm_attributes("-transparentcolor", "white")
label.bind('<Button-1>', hey)
walk()
root.mainloop()
