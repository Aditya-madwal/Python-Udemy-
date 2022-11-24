# nested if else statements 

print("welcome to the rollercoaster.")
name = str(input("what is your name? "))
height = float(input("whats is your height(in cm)? "))
age = int(input("what is your age? "))

if height >= 120:
  if age>= 18:
    print(f"you are welcome mr.{name}.")
  else :
      print(f"sorry you cant enter mr.{name}.")
else:
  print(f"sorry you cannot enter mr.{name}.")
