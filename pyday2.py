#-------------STRING MANIPULATION--------------
print(len("aditya is a good boy")) #prints the no. of characters in the given STRING

#data types
#---1) STRINGs
string0 = "aditya is a boy"[1] # prints the character at index 1 of the string i.e. d (here)
string1 = "aditya madwal is a boy"
print(string0)
print(string1)
#string indexing starts from 0 to infinity
string2 = "123442" #this is not a no. but a string

print(string1+string2) #prints "aditya madwal is a boy123442" because they are STRINGs


#------------DATATYPES------------
num1 = float(123.5) # t\prits the no. along with the decimal etc
print(num1)
num2 = int(123.4) # prints only 123 and not decimal no.s 
print(num2)
sen1 = str("aity") #its a string
print(sen1)
 
print(str(20) + str(123)) # just prints the two strings together
print(219+344) # prints the sum
print(12 + 34.4) # prints 46.4 the whole sum with decimal
print(12 + int(34.4)) #prints 46 only because the int func turns float no. to integer data types

# TYPE FUNCTION-- prints the data type of the function 

print(type(num1))
print(type(sen1))


#--------------MATHEMATICAL OPERATIONS-----------------
print(2*3)
print(2/3)
print(2+3)
print(2-3)
print(2**3) #exponent

# THE BODMAS OF PYTHON :-
# PEMDAS
# ()
# **
# *
# /
# +
# -

#----------NUMBER MANUPULATION---------
print(round(10/3)) # prints the round off of the result
print(round(10/3 , 2)) # here 2 is the no. of places to be rounded off

#adding in a different way

score = 0
score += 1
score += 2 
print(score)

# similarly substraction
 
marks = 23
marks -= 3
print(marks)

#similarly /= and *=

#-------------------F-STRING-------------------

print(f"your marks are {marks}") #no need to match the data types of the string

