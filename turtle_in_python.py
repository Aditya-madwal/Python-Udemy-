from turtle import *

mandy = Turtle()
mandy.shape("turtle")
mandy.color("red")
# here mandy is the object
# and Turtle() is the class
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)
forward(50)

# if it is written as
# import turtle ....(module)
# Turtle()...(class)... will not be recognised by the console and will give error

my_screen = Screen()
# here my_screen is an object 
# we r basically getting the screen attributre from the turtle object

my_screen_size = my_screen.canvheight
print(my_screen_size)
# this prints the size of the screen 
# the canvheight is the sttribute here and the my_screen is the object... and we are getting the attribute from the object.

my_screen.exitonclick()
# this allows our program to remain shown up untill it is clicked on the screen 
# else the program once finished will automatically disappear
