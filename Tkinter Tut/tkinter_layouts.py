print("tkinter layout managers")

from tkinter import *

window = Tk()
window.minsize(width = 500, height = 500)
# PACK()

# pack() packs up the items in a chronological order and by default the position is center alinged and at the top.
# pack(side = "left") # left, right, top, bottom

# PLACE()

# place(x=100, y=200)
# the x and y are the coordinates of the position of the item

# GRID() 
# best one so far
button_1 = Button(text = "Click Me !", font = ("arial", 10, "bold"))
button_2 = Button(text = "Click Me !", font = ("arial", 10, "bold"))
button_3 = Button(text = "Click Me !", font = ("arial", 10, "bold"))

button_1.grid(column = 0, row = 0)
button_2.grid(column = 1, row = 1)
button_3.grid(column = 2, row = 2)

# pack() and grid() cannot be used in the same code and if used it gives an error!
window.mainloop()