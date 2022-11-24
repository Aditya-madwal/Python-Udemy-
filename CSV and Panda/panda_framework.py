import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

# print(" ")

# print(data['day'])
 	
# print(" ")

# data_dict = data.to_dict()
# # this converts the whole data frame into a dictionary with {day,{index:day123}} format
# print(data_dict)

# print(" ")

# temp_dict = data['temp'].to_dict()
# # this converts the temp data into a dictionary with {index : item} format
# # this "temp" is called a series 
# print(temp_dict)

# print(" ")

# temp_list = data["temp"].to_list()
# # this prints the whole series(temp) into a list 
# # this also automatically excludes the label "temp"
# print(temp_list)
# # now this list can be modified just as a regular list.

# print(" ")

# # avg temp check

# average_temp = round(sum(temp_list)/len(temp_list) , 2)
# # round(number , decimal_places) 
# # this helps to limit a float value to a certain decimal places
# print(f"the average temp is : {average_temp}")

# print(max(temp_list)) 
# print(min(temp_list))

# # get the data in a row
# # eg - get the data of monday

about_monday = data[data.day == 'Monday']
print(about_monday)
# this returns the particular row of MONDAY 
# it is necessary that the data is not converted into dict or list for pulling out a partivular row.

# printing the row which has the maximum temperaturre

day_with_max_temp = data[data.temp == data.temp.max()]
print(day_with_max_temp)

