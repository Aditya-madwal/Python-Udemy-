#for loop 
fruits = ['apple','mango','cherry','banana','peach']
print("apple" in fruits)  # prints TRUE
print("pear" in fruits) #prints FALSE

for i in fruits:  # here i stands for the items in list ... x can be used to 
	print(i)     # this prints the items in the list one by one
	print(i + " is a fruit")
	# print(i + "is at index no.")

#forloop
print("hello")
my_list = ['aditya','ayu','golu','riya','shubham']
#to print the items one by one .. the manual option is 
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

# but with for loop
for i in my_list :
    	print(i)

# similarly tuple can also be for looped and printed one by one 

my_tuple = ('madwal','paddey','sanaa','karls')
for friends in my_tuple :
    	print(friends)

# for loop on list of list

my_scores = [['eng',89],['maths',78],['sst',34]]
for subjmarks in my_scores :
    	print(subjmarks)     # this prints the lists one by one 

for subj , marks in my_scores :	
    	print(subj ,"and", marks) # this prints the subj along side the marks 


#---------------------------ASSIGNMENT QUESTION---------------------------
# make a list and detect if it is a no. or not and if its a num then print if greater than 6

items = [int ,float, "aditya" , "ayush",34,56,1,2,3]

for item in items :
	if str(item).isnumeric() and item>6 : 
		#first the item has bee STRINGIFIED so that datatype like int and float can be turned into strig and then verified as numeric
		print(item)

# alternative method 

for i in items :
	if type(i) == int and i > 6:
		print(i)


#---------------------RANGE FUCTION-----------------
# for number in range (a,b,c) :       # a represents initial , b represents final , c represents STEP GAP 
# 	print(number)

for num in range (1,10) : #numbers between 1 and 10 not including 10 but including 1
	print(num)

for number in range (1 , 20 , 2) : # 1,3,5,7,9....19
    	print(number)

#-------------------------------QUESTION------------------------------
# sum up all the no. btw 1 to 100 and print ... using for loop and range function

total = 0
for numbers in range(1,101) :
	# print(numbers) #prints 1 to 100 (excluding 101)
	# total = total+numbers
	total += numbers 

print(total)

#------------------------------QUESTION----------------------
# 2+4+6+.........+100 = ?

even_total = 0
for x in range(0 , 101 , 2):
	print(x)
	even_total = even_total + x
print(even_total)

# alternate way 
# even_total_alternate = 0
# for y in range(2 , 101) :
#     if y%2 ==0 :
# 		even_total_alternate += y
# print(even_total_alternate)