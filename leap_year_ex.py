#leap year exercise 
#theory:-
#2100 1700 1900 arent leap years divisble by 100 and 4 but not div by 400

year = int(input("enter the year : "))

if year % 4 == 0 :
  print(f"{year} is divisible by 4")
  if year % 100 == 0 :
    print(f"{year} is divisible by 100")
    if year % 400 == 0 :
      print(f"{year} is divisible by 400")
      print(f"{year} is a leap year")
    else :
      print(f"{year} is not a leap year")
  else :
    print(f"{year} is a leap year")
else :
  print(f"{year} is not a leap year")
 