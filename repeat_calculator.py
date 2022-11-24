# a calculator


#add
def add(n1, n2):
    return n1 + n2


#subtract
def subtract(n1, n2):
    return n1 - n2


#multiply
def multiply(n1, n2):
    return n1 * n2


#divide
def divide(n1, n2):
    return n1 / n2


operations_dict = {'+': add, '-': subtract, '*': multiply, '/': divide}

# one way to call out the function operation
addition = operations_dict['+']
print(addition(2, 3))

num1 = int(input("num 1 : \n"))
num2 = int(input("num 2 : \n"))

for symbol in operations_dict:
    print(symbol)
operation_symbol = input('pick an operation line above : \n')

final_calculation_function = operations_dict[operation_symbol]
answer = final_calculation_function(num1, num2)

print(answer)

should_continue = True
