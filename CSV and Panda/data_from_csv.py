print("reading data from csv file")

# with open("weather_data.csv",mode = 'r') as data_file :
# 	data = data_file.readlines()
# 	print(data)

# easy method (recommended):

import csv

with open("weather_data.csv" , mode = "r") as data_file :
	data = csv.reader(data_file)
	# this reads the data and outputs it
	# this creates a csv reader object
	print(data) # returns the csv reader object
	temperature = []
	for row in data :
		# print(row)
		# this prints the data line by line as a list of [day,temp,condition]
		days = row[0]
		# print(days)
		# this only prints the day as the index (0) of the row(list) is day!

		# to make a list of all temperatures :
		temperatures = row[1]
		# temperature.append(temperatures)
		# print(temperature)
		# but this also prints the "temp" label 
		# to exclude it :
		if row[1] != "temp" :
			temperature.append(int(temperatures) # converts thetempertaures written as string into integer 
				
	print(temperature)

