print("this is a blind auction")

from replit import clear

bids_dictionary = {}
bidding_finished = False


while not bidding_finished :
	name = input('what is your name sir/madam : \n')
	price = input('what is your bid : \n $')
	bids_dictionary[name] = price
	continue_or_not = input("are there more bidders ? type 'yes or 'no' :\n")

	if continue_or_not == 'no' :
		bids_dictionary = True
	elif continue_or_not == 'yes' :
		clear()
