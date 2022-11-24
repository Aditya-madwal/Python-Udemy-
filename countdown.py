print("countdown")

from tkinter import *
import math

window = Tk()
total_count = 250
window.minsize(width = 200 , height = 100)
window.config(padx = 20, pady = 20)

time = Label(font = ("arial",20,"bold"))
time.pack()

def countdown(count) :
    count_min = math.floor(count/60)
    count_sec = count % 60
    window.after(1000, countdown, count-1)
    time_display = f"{count_min}:{count_sec}"
    time.config(text = f"{count_min}:{count_sec}")

countdown(250)


window.mainloop()