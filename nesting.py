print("nesting lists and dictionaries")

'''{
	key : [list],
	key2 : {dict}
}

'''

# nesting a list in a dictionary
travel_log = {
	'India' : ['delhi' , 'agra' , 'himachal' , 'goa'],
	'france' : ['paris' , 'lille' , 'dijon'],
}
print(travel_log)

# nesting a dictionary in a dictionary
travel_days_log = {
	'usa' : {
	'new york' : 2,
	'sanfransisco' : 3
	},

	'nepal' : {
	'kathmandu' : 2,
	'kamar taj' : 4
	},
}
print(travel_days_log)

#  nesting a dictionary in a list
listed_travel_log = [
	{"country":"india","city":"delhi","no. of days":4},
	{"country":"france","city":"paris","no. of days":3},
]
print(listed_travel_log)
