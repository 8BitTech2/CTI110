# A "while loop" will run the program again and again because while loops run if the
#condition is True so we have made the condition true and as you know True is
#always true and never false.

while True:
  try:
    age = int(input("Enter your age: "))
    if (age == 15) or (age == 18) or(age == 20):
       break
    print("Invalid age entered")
  except Exception as e:
    print(e)
    
