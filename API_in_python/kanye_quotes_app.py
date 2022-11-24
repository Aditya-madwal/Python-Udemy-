# This program gives you random quotes by kanye 
# this program uses API "https://api.kanye.rest/"

from tkinter import *
import requests

window = Tk()

# -------MECHANISM-------

quote = ""
def generate_command() :
	response = requests.get(url = "https://api.kanye.rest/")
	quote = response.json()["quote"]
	print(quote)
	canvas.itemconfig(text , text = f'"{quote}"')

# -------UI-------
window.title("Kanye says...")
window.config(padx = 20, pady = 20)

bg_img = PhotoImage(file = "background.png")
kanye_image = PhotoImage(file = "kanye.png")

canvas = Canvas(width = 300 , height = 500)
canvas.create_image(150, 250, image = bg_img)
text = canvas.create_text(150, 250, text = f'"{quote}"', font = ("arial", 15, "bold"), width = 250)
canvas.grid(column = 0, row = 0)

generate_button = Button(image = kanye_image, highlightthickness = 0, command = generate_command)

generate_button.grid(column = 0, row = 1)


window.mainloop()