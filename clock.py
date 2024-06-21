from tkinter import Tk 
from tkinter import Label

import time
import sys

root = Tk()
root.title("Digital Clock")

def present_time():
    current_time = time.strftime("%I:%M:%S %p")
    dig_clock.config(text = current_time)
    dig_clock.after(200,present_time)

dig_clock = Label(root ,font=("arial",100),bg= "blue",fg="yellow")
dig_clock.pack()

present_time()
root.mainloop()