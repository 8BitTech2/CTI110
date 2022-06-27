import random

# generates random number and returns

def generateRandomNo():
    return random.randint(10, 999)
    
# checks whether the guess made is correct or not

def checkGuess(number, guess):
    if (guess < number):
        print("Sorry, guess is too low.")
        return 0
    if (guess > number):
        print("Sorry, guess is too high.")
        return 0
    if (guess == number):
        print("Congratulations!!!! your answer is correct..")
        return 1
                       
def main():
    print("\nWelcome to Math Quiz")
# Loops as long as user wants to continue
    while True:
        choice = menu()
        if choice == 1:
            a = generateRandomNo()
            b = generateRandomNo()
            print("  "+ str(a) + "\n+ " + str(b))
            ans = a + b
            guess = int(input("Enter answer.\n"))
            i = 1
            while(checkGuess(ans, guess) != 1 ):
                guess = int(input("try again: "))  
                i = i + 1
            print("Number of guesses: "+str(i))
        elif choice == 2:
            a = generateRandomNo()
            b = generateRandomNo()
            print("  "+ str(a) + "\n- " + str(b))
            ans = a - b
            guess = int(input("Enter answer.\n"))
            i = 1
            while(checkGuess(ans, guess) != 1 ):
                guess = int(input("try again: "))  
                i = i + 1
            print("Number of guesses: "+str(i))
        elif choice == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid option... Try again")
            
        
# Method to display menu and read choice from user 
  
def menu():
    print("\nMAIN MENU")
    print("-----------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    choice = int(input("Please choose one of the menu options: "))
    return choice

main()
