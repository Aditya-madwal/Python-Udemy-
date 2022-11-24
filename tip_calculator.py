#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# a tip calculator 


bill_amt = float(input("enter the total amount of bill : $"))
tip_percent = int(input("what percentage tip would u like to give? "))
total_bill = ((tip_percent/100)*bill_amt) + bill_amt
people = input("how many people are going to split the amount? ")
total_bill = float(total_bill)
people = float(people)
amt_per_head = float(total_bill/people)
amt_per_head = round(amt_per_head ,2)
print(" ")
print(f"each will have to pay ${amt_per_head}")
