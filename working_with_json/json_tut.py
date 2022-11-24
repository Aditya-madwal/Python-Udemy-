import json

name = input("enter your name : ")
classs = input("enter your class : ")
roll_no = input("enter your class : ")

# name = "aditya"
# classs = 12
# roll_no = 3

print(name)
print(classs)
print(roll_no)

data = {
    name : {
        "class" : classs,
        "roll no." : roll_no,
    }
}

# with open('json_tut_file.json', mode = 'w') as json_file :
#     json.dump(data, json_file, indent = 4)

with open('json_tut_file.json', mode = 'r') as json_file :
    load_data = json.load(json_file)
    load_data.update(data)

with open('json_tut_file.json', mode = 'w') as json_file :
	json.dump(load_data, json_file, indent = 4)


