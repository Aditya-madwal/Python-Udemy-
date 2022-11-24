print("prime number checker")

num = int(input("enter any number : "))


def prime_or_not(number = num) :
	print(num)
	is_prime = True
	for i in range(2 , num):
		if num % i == 0 :
			is_prime = False

		if is_prime :
			print(f"{num} is prime")
		else :
			print(f"{num} is not prime")


prime_or_not()