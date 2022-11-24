print('dictionaries in python')

# the general syntax is :
# dictionary = {key : value , key2 = value2 , ... }

sample_dict = { 
	"code" : "programming instructions",
	"monitor" : "display device",
	"instagram" : "social meda platform",
	7124 : "this is a number"
}

# printing a dictionary

print(sample_dict["monitor"])
#this prints the value of the key "monitor"
print(sample_dict[7124])

# adding new item to the dict
sample_dict["new item"] = "this item has been added to the dictionary"
print(sample_dict)

# edit an item in a dict

sample_dict["monitor"] = "it is a device"
print(sample_dict)

# empting a dictionary 
# sample_dict = {}
# print(sample_dict)

# empty dict
empty_dict = {}

# loop through a dictionary

for item in sample_dict :
	print(item)
	# this prints the keys one by one only and not the value
	print(sample_dict[item])
	# this prints the value only
	print(item , ":" , sample_dict[item])
	# smart way to print the dictionary in key:value format

