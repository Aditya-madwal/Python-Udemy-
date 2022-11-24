# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight/height**2
bmi = round(bmi,2)
print(f"your bmi is {bmi}")

if bmi < 18:
  print("you are under weight")
elif bmi >=18 and bmi<25 :
  print("you are normal weight")
else :
  print("you are over weight")
