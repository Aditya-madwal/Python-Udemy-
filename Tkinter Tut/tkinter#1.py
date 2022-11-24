from tkinter import *
 
window = Tk()

window.title("my first tkinter program")
window.config(padx = 20 , pady = 20) 
# adds up margin on the whole tkinter window 

window.minsize(width = 500 , height = 300)

my_label = Label(text = "I love you shaxpeur", font =("arial",25,"bold"))
my_label.pack() 
# this defaults to side "top" and "center"

# my_label.pack(side = "left")
# {left , right , bottom , top}

my_label.pack()
# this centralises the text at the exact center and mid.

# editing my label 
# the label is a dictionary of {key : value} where key is the text, format , color etc and value is the value

my_label["text"] = "this is the modified text."
# modifies the text and automatically packs 

my_label.config(fg = "red", bg = "yellow", text = "again modified")
# also text can be changed through this 

# BUTTONS :-

button_1 = Button(text = "this is button 1", font = ("arial",10,"bold"))
button_1.pack()

# alloing a command to the button :-

def button_1_click():
    print("you just clicked the button 1.")

button_1.config(command = button_1_click)

# commanding a button to config some tkinter things :-

button_2 = Button(text = "this is button 2", font = ("arial",10,"bold"))
button_2.pack()

def button_2_click() :
    print("you just clicked the button 2.")
    button_2.config(bg = "yellow")

button_2.config(command = button_2_click)

# taking inputs in tkinter window 

name = Entry()
name.pack()

# question :-

title_label = Label(text = "what do you think should be the title of this program ?", font = ("arial",10,"bold"))
title_label.pack()

title_input = Entry(font = ("arial",10,"bold"))
title_input.pack()

def title_func():
    print(title_input.get())
    my_label.config(text = title_input.get())
    
title_button = Button(text = "ENTER", font = ("arial",10,"bold"), command = title_func)
title_button.pack()

# hiding and showing a widget :-
def toggle_hide_show():
    hide_or_show = hide_show_button.cget('text')
    if hide_or_show == "hide" :
        hide_show_button.config(text = "show")
        text.pack_forget()
    elif hide_or_show == "show" :
        text.pack()
        hide_show_button.config(text = "hide")

text = Label(text = "hello ji !", font = ("arial",15,"bold"))
text.pack()
hide_show_button = Button(text = "hide", font = ("arial",10,"bold"), command = toggle_hide_show)
hide_show_button.pack()




window.mainloop()