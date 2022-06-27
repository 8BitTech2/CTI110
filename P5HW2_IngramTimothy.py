# Program offers simple math quizzes using a menu.
# The user can enter an answer and the program will determine the results and number of tries.
# 27Jun2022
# CTI-110 P5HW2 - Math Quiz
# Timothy Ingram
#

import random
print("\nWelcome to Math Quiz")
print()
# generates random number and returns
def add_Random():
	n1=random.randint(0,1000)
	n2=random.randint(0,1000)
	print(f"{n1:>6}")
	print(f"+{n2:>5}")
	print("Enter answer")
	i = 1
	ans=int(input())
	while ans!=n1+n2:
		if ans<n1+n2:
			print("Sorry, guess is too low.")
			print()
		else:
			print("Sorry, guess is too high")
			print()
		ans=int(input("try again : "))
		i = i + 1
	print("Congratulations!!!! your answer is correct..")
	print("Number of guesses: "+str(i))
	print()

def sub_Random():
	n1=random.randint(0,1000)
	n2=random.randint(0,1000)
	print(f"{n1:>6}")
	print(f"-{n2:>5}")
	print("Enter answer")
	i = 1
	ans=int(input())
	while ans!=n1-n2:
		if ans<n1-n2:
			print("Sorry, guess is too low.")
			print()
		else:
			print("Sorry, guess is too high")
			print()
		ans=int(input("try again : "))
		i = i + 1
	print("Congratulations!!!! your answer is correct..")
	print("Number of guesses: "+str(i))
	print()
	
if __name__=="__main__":

	while 1:
		print("MAIN MENU")
		print("----------------------")
		print("1) Add Random Numbers ")
		print("2) Subtract Random Numbers")
		print("3) Exit")
		print()
		num=int(input("Please choose one of the menu options: "))
		if num==3:
			print("Thank you for playing...")
			print("Bye!!")
			break
		if num==1:
			add_Random()
		if num==2:
			sub_Random()


'''
Program steps:
Input
1.  From a menu option, offer 3 choices
2.  Prompt user for correct answer to equation

Process
1.  First, receive input from menu choice
2.  Display 2 random numbers
3.  Receive answer and calculate to find status

Display
1.  Menu option
2.  random numbers
3.  result of calculation
4.  result of number of tries
5.  prompt to choose from menu
'''
