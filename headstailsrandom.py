import random

random_side = random.randint(0,1)

your_call = input("heads(1) or tails(0) ? : ")

if random_side == 1:
	print("its heads")
else :
	print("its tails")
