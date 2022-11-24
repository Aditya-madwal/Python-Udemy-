print("slicing a tuple or a list")

alpha = "abcdefghijklmnopqrstuvwxyz"

list_alpha = list(alpha)
print(list_alpha)

print(list_alpha[2:9])
# prints from index no. 2 to 8

print(list_alpha[2:15:2])
# skips every 2nd item in the list

print(list_alpha[::2])
# the blanks represent the beginning and the ending of the list 

print(list_alpha[::-1])
# this starts the list from the back BACKWARDS 
# basically REVERSES THE LisT