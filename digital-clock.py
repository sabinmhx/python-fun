from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S")
    label.config(text = string)
    label.after(1000, time)
    
label = Label(root, font = ("", 80), background = "black", foreground = "aqua")
label.pack(anchor = "center")

time()
root.mainloop()
