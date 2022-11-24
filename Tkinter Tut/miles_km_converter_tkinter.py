from tkinter import *

window = Tk()
window.config(padx = 30, pady = 30)
window.minsize(width = 700, height = 500)

title_label = Label(text = "Miles to Kms Converter :", font = ("arial", 25, "bold"))
title_label.grid(column = 0 , row = 0)

# enteries :

miles_label = Label(text = "enter the value (miles) : ", font = ("arial", 15, "bold"))
miles_label.grid(column = 0 , row = 1)

miles_input = Entry(font = ("arial", 15, "bold"))
miles_input.grid(column = 1, row = 1)

# miles = miles_input.get()
# result :

# result = Label(text = f"{miles} miles is equal to {eu} kilometers.")

def miles_to_kms():
    miles = int(miles_input.get())
    kms = round(miles * 1.60934 , 2)
    print(kms)
    result = Label(text = f"{miles} miles is equal to {kms} kilometers.", font = ("arial", 15,"bold") , fg = "grey")
    result.grid(column = 0, row = 3)


result_button = Button(text = "Convert" , font = ("arial", 12, "bold"), command = miles_to_kms)
result_button.grid(column = 1 , row = 2)
# result_button.config(padx = 20, pady = 20)

window.mainloop()