print("squaring numbers")

numbers = [2,4,5,8,5,3]
print(numbers)
squared_num = []

for i in numbers :
	squared_num.append(i)
	i = i*i
	squared_num.append(i)

print(squared_num)