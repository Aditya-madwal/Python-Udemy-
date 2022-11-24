print("msg encryptor by CAESER CIPHER")

string_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string_alpha.lower()
print(string_alpha.lower())

list_alpha = list(string_alpha.lower())
print(list_alpha)

msg = input("enter your msg here : \n").lower()
shifts = int(input("enter the no. of shifts : \n"))

encrypted_msg = ""

def encrypt(plain_text , num_of_shifts) :
	
	encrypted_msg = ""
	
	if num_of_shifts > 26 :
		for letter in plain_text :
			original_index = list_alpha.index(letter)
			shifted_index = original_index + num_of_shifts - 26
			new_letter = list_alpha[shifted_index]
			encrypted_msg += new_letter
	else :
		for letter in plain_text :
			original_index = list_alpha.index(letter)
			shifted_index = original_index + num_of_shifts
			new_letter = list_alpha[shifted_index]		
			encrypted_msg += new_letter

	print(f"the encoded msg is {encrypted_msg}")

encrypt(plain_text = msg , num_of_shifts = shifts)

