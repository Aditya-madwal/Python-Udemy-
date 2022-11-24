from tkinter import *
from math import *

window = Tk()
window.minsize(width = 500, height = 500)
window.config(padx = 20 , pady = 20)


#-------------Functions Mechanism-------------

def countdown(minutes , seconds):
    count = minutes*60 + seconds
    
    if count > 0 :
        print(f"{count_min}:{count_sec}")   
        window.after(1000, countdown, count-1)


def start_timer():
    countdown(minutes , seconds)
    # window.after(1000, countdown , thing)
    print("timer started")




#-------------UI designing-------------


title = Label(text = "Timer", font = ("arial",20,"bold"))
title.grid(column = 1 , row = 0)

# inputs :
ask_min = Label(text = "Enter the no. of minutes : ", font = ("arial",12,"bold"))
ask_sec = Label(text = "Enter the no. of seconds : ", font = ("arial",12,"bold"))
ask_min.grid(column = 0 , row = 1)
ask_sec.grid(column = 0 , row = 2)

entry_min = Entry(font = ("arial",12,"bold"))
entry_sec = Entry(font = ("arial",12,"bold"))
entry_min.grid(column = 1, row = 1)
entry_sec.grid(column = 1, row = 2)
minutes = entry_min.get()
seconds = entry_sec.get()
# buttons :

start = Button(text = "Start Timer", font = ("arial",10,"bold"), command = start_timer)
start.grid(column = 1 , row = 3)

timer_text = Label(text = "00:00", font = ("arial",10,"bold"))
timer_text.grid(column = 1 , row = 4)
#-------------End-------------
window.mainloop()