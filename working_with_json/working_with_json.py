print("working with JSON!")

from tkinter import *
import json


# MECHANISM :

def add_to_json() :
	name_value = name_Entry.get()
	class_value = class_Entry.get()
	roll_value = rollno_Entry.get()

	student_data = {
		name_value : {
			"class : " : class_value,
			"roll no. : " : roll_value
		}
	}
	
	# Writing to JSON 

	with open( "data_file.json" , mode = "r" ) as data_file :
	    #Reading old data
	    data = json.load(data_file)
	    #Updating old data with new data
	    data.update(student_data)
	with open( "data_file.json" , mode ="w" ) as data_file :
	    #Saving updated data
	    json.dump( data , data_file , indent = 4 )

	website_entry.delete( 0 , END )
	password_entry.delete( 0 , END )

	print(student_data)

# UI : 

window = Tk()
window.title("working with json")
window.config(padx = 20, pady = 20)

name_label = Label(text = "enter your name : ",font = ("arial",12,"bold"))
class_label = Label(text = "enter your class : ",font = ("arial",12,"bold"))
rollno_label = Label(text = "enter your roll no. : ",font = ("arial",12,"bold"))
name_label.grid(column = 0 , row = 0)
class_label.grid(column = 0 , row = 1)
rollno_label.grid(column = 0 , row = 2)


name_Entry = Entry(font = ("arial",12,"bold"))
class_Entry = Entry(font = ("arial",12,"bold"))
rollno_Entry= Entry(font = ("arial",12,"bold"))
name_Entry.grid(column = 1 , row = 0)
class_Entry.grid(column = 1 , row = 1)
rollno_Entry.grid(column = 1 , row = 2)

add_button = Button(text = "Add to JSON", font = ("arial",12,"bold"), width = 20, command = add_to_json)
add_button.grid(column = 0, row = 3, columnspan = 2)






window.mainloop()