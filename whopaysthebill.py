import random

names = input("gemme the names(seprated by comma) : ")
names_list = names.split(",")    # seperates the names with commas in a list 
print(names_list)

print(len(names_list))

one_who_pays_the_bill = names_list[random.randint(0,len(names_list)-1)]
print(one_who_pays_the_bill , "is gonna pay the bill.")

# this could also be done by the CHOICE functiom

naam = ['adi','ayu','golu','riya']
print(naam)
 
for i in range(1) : # -1 to stabilise the index and len 
	print(random.choice(naam))

# this picks up a random choice and prints .. no. of choices is range(no. of choices)


