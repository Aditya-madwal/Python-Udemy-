import random
# import string_utils

print("password generator")

letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(letters_lower)
list_lower = list(letters_lower)

letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(list(letters_upper))
list_upper = list(letters_upper)

list_numbers = list('1234567890')
print(list_numbers)

list_symbols = list('!@#$%^&*-+')
print(list_symbols)

print(len(list_lower)+len(list_numbers)+len(letters_upper)+len(list_symbols))

# inputs from the user 

num_letters_upper = int(input("how many upper case : "))
num_letters_lower = int(input("how many  case lower: "))
num_numbers = int(input("how many numbers : "))
num_symbols = int(input("how many symbols : "))

password = ""  # empty string

for lower in range(1, num_letters_lower+1) :
    random_lower= random.choice(list(list_lower))
    password = password + random_lower
    # print(password)

for numbers in range(1, num_numbers+1) :
    random_numbers = random.choice(list(list_numbers))
    password = password + random_numbers
    # print(password)

for symbols in range(1, num_symbols+1) :
    random_symbols = random.choice(list(list_symbols))
    password = password + random_symbols
    # print(password)

for upper in range(1, num_letters_upper+1) :
    random_upper = random.choice(list(list_upper))
    password = password + random_upper
    # print(password)

print("YOUR THE MOST SECURED PASSWORD IS :",password)
# random.shuffle(password)
# print(password)
# print string_utils.shuffle(password)

# NOW SHUFFLING THE PASSWORD :-

list_password = list(password)
print(list_password)
random.shuffle(list_password)
print(list_password)

shuffled_password = ""  #empty string

for i in list_password:
    shuffled_password = shuffled_password + i
print(shuffled_password)

# DONE !
