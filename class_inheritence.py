print("class inheritence in python")


# class SampleInheritedClass(SuperClass):
# 	def __init__(self):
# 		super().__init__() 
# this super() refers to the SuperClass

# for eg - 

class Animal :
	def __init__(self):
		self.num_of_eyes = 2

	def breathe(self):
		print("inhale, exhale")

class Fish(Animal) :
	def __init__(self):
		super().__init__()
		# this allows to inherit all the methods and attributes from the parent class here its Animal class
	def swim():
		print("swimming")

	def breathe(self):
		super().breathe()
		print("this is a modified method from the Animal class")
		# this is how we can modify a method from the parent class in the inherited class

nemo = Fish()
# nemo is the object

nemo.breathe() # method in the Animal is accessible by the Fish
# prints "inhale, exhale"

print(nemo.num_of_eyes) # attribute from Animal is accessible by the Fish

tiger = Animal() # parent class
tiger.breathe() # this prints "inhale , exhale" i.e the unmodified method command.