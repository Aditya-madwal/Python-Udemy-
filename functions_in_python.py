print("functions in python")

def myfunc() :
	print("hello")
	print("world")
	print("hello\nworld")

myfunc() # calls out the functions and does as defined 

# functions with inputs 

def greet() :
	print("hello")
	print("good morning")
greet()

def greet_with_name() :
	name = input("enter your name : ")
	print(f"hello {name}")
	print("good morning")

greet_with_name()

def new_greet(your_name) :
	print("hello " + your_name)

new_greet("ayush")

def new_greet_multiple(your_name , anime_name , age) :
	print("her name is " + your_name)
	print("her fav anime movie is " + anime_name)
	print("her age is " + age)

new_greet_multiple("chetna" , "your name" , "17")

#-----------------question------------------
print("------------------------------")

num_of_apples = int(input("how many apples : "))
num_of_people = int(input("how many people : "))

def apple_per_each(apple = num_of_apples , people = num_of_people) :
	apple_per_each = apple/people
	print(f"each person will get {str(apple_per_each)} apples ")

apple_per_each()

