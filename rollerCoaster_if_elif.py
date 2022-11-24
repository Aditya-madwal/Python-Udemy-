# multiple if elif else statements
#rollercoaster problem
name = input("enter your name : ")
age = int(input("enter your age : "))
if age >= 18:
    print("u can go for $3.")
    pics = input("do u want a photo (Y/N) : ")
    if pics == "Y":
        print("okay...")
    elif pics == "N":
        print("no problem...")
    else:
        print("please answer in Y/N...")
elif age >= 16 and age <= 18:
    print("u may go for $5.")
else:
    print("sorry u cant go...chal bhaag")
