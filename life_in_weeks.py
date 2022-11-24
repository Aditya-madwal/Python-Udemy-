# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
years_remaining = 90 - age
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
print(f"you have currently {years_remaining} years,{days_remaining} days ,{weeks_remaining} weeks to live.")
