# apni lkaksha lecture on python programming basics :-

# to run python file in cmd :-
#terminal/cmd > cd {code file} > cd {python file} > python hello.world
print("hello world!")

name = "mandy"
another_name = "aditya pitamber dutt madwal"

#strings management

print(name.find('d'))  # gives the index no. of the 'd' in the name entered

print(name.replace(name, "aditya madwal"))  #replaces

print(another_name.replace("dutt madwal", "madwal"))

print("ad" in name)  # tells true or false for 'ad' being in name

#arithmetic oprations

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 % 2)  #remainder operator

print(3 > 13)  #says true or false
print(23 == 34)  # also says true and false
print(34 != 55)  # not equals to

# LOGICAL OPERATORS :-

#or
print(22 > 33 or 44 < 55)  # f or t says true

#and
print(22 > 33 and 33 < 55)  # f and t syas false

#not
print(33 > 44)  #says false
print(not 33 > 44)  #says true (not false)

# if else statements :-

sun = "on"

if sun == "on":
    print("its mornning")
else:
    print("its night")

#mini project : simple calculator

print("simple calculator ")

num1 = int(input("enter 1st no. : "))
operation = input("*,/,+,- : ")
num2 = int(input("enter 2nd no. : "))

if operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)

#range
numbers = range(7)
print(numbers)  #prints range(0,7)

# loops

#while loop (jab tak tab tak)

num = 1
while num <= 10:  # jab tak num 10 se chota ya equal hai
    print(num)
    num = num + 2  # tab tak num mein +2 krke print krte raho

numm = 1
while numm <= 5:  # jab tak num 5 se chota hai
    print(numm * "*")
    numm = numm + 1  # tab tak ****.. likhte raho

for item in range(10):
    print(item + 2)  # 2,3,5....

# LIST MANIPULATION :

animals = ["tiger", "lion", "dog"]
mixed = ["aditya", 34]
print(animals)
print(mixed)

print(animals[1])  #prints item of index 1 in animals
print(mixed[-1])  #prints last item of mixed

# index to index printing
print(animals[0:2])  #btw 0 to 2 index i.e tiger and lion

#printing in sequece 1 by 1 :-
for names in animals:  #names can be any variable
    print(names)

animals.append("zebra")  # adds zebra in the list
print(animals)

animals.insert(1, "cheetah")  #inserts cheetah at index no. 1
print(animals)

#to check something being in the list
print("cheetah" in animals)  # says true

#length of the list
print(len(animals))

i = 0
while i < len(animals):
    print(animals[i])
    i = i + 1

animals.clear()
print(animals)

# break and continue

students = ["chatti", "tushar", "karls", "chetna", "sanya", "paddey"]

for student in students:
    if student == "chetna":
        break
        # breaks the loop when list reaches chetna
    print(student)

for student in students:
    if student == 'karls':
        continue  #leaves karls and continues to print
    print(student)

# tuple :-
# unmodifiable lists

friends = ("bhavik", "govind", "piyush", "yash", "govind")

print(friends.index("govind"))  # prints the index of govind coming first time

# sets in python
# in sets index doesnt exists
# every term should be unique

sample_set = {"aditya", "ayush", "rahul",
              "riya"}  # if rahul is repeated then also set will print it once

for cousins in sample_set:
    print(cousins)  # unordered printing

# sets can be used as dictionaries too

marks = {"english": 98, "chemistry": 97, "maths": 95, "physics": 99}
print(marks["physics"])  # prints the data stored under physics i.e. 99
print(marks)  # prints the whole set

print("*****************done*******************")
