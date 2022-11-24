# BMI CALCULATOR WITH PYTHON

#user inputs
name = input(str("enter your name : "))
height = input("enter your height in metres : ")
weight = input("enter your weight in kilograms : ")


#calculations
bmi = (int(weight) / float(height)**2)

#output
print(int(bmi))
print("hey "+name+" your bmi is : "+str(bmi))

print("hello ")

for i in range(0,19) :
    i += 1
    print(i)

