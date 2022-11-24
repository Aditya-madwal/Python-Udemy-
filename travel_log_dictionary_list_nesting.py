print("nesting dictionary in list exercise")

travel_log = [
	{"country" : "country_name",
	"city" : "city_name",
	"no.of days spent" : 5,}
]
print(travel_log)

def add_new_log(country_name , city_name , days) :
	new_log = {}
	new_log["country"] = country_name
	new_log["city"] = city_name
	new_log["no.of days spent"] = days
	print(new_log)
	travel_log.append(new_log)

add_new_log("india" , "delhi" , 5)
print(travel_log) 

