# CTI-110
# P4HW1 -  Score List
# Timothy Ingram 
# 24Jun2022
#
'''
here  are the steps for this program:
Input
1.  ask user for the number of exams to score
2.  receive the valid input from user for those exams
Processing
3.  calculate the average of all exams
4.  calculate the grade distribution
5.  exit if user input is -1 or above 100
6.  repeat process of exit happens
Results
7.  display a set of results that includes the minimum, average, and letter grade plus the list entered
'''

list_Scores = []                               # Creating an empty list
number_Scores = int(input("How many exams do you want to score? ")) # Taking user input for number_Scores  
print()
currentNum_Scores = 0                          # Initializing currentNum_Scores to 0
while(True):                                   # Looping until we have all all required number of scores
    while(currentNum_Scores<number_Scores):    # Looping for user input
        scores = float(input('Enter score #{}: '.format(currentNum_Scores+1)))
        while(True):                           # Prompting for user input if entered score was invalid
            if(scores<0 or scores>100):
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(currentNum_Scores+1)))
            else:                              # If valid score was entered 
                list_Scores.append(scores)     # Adding this to the list
                break                          # Breaking out of the loop as we do not require further input
        currentNum_Scores+=1                   # Incrementing the count of currentNum_Scores by 1 when a valid score was entered
    if(currentNum_Scores==number_Scores):      # If user entered all required number of valid scores
        break                                  # Breaking out of the loop as we do not require further input
min_Element = min(list_Scores)                  # Computing minimum score
list_Scores.remove(min(list_Scores))           # Removing min score from the list
average = sum(list_Scores)/len(list_Scores)    # Computing average score
if(average>=90 and average<=100):              # Computing grade based on the average score
    grade = 'A'
elif(average>=80 and average<=89.9):
    grade = 'B'
elif(average>=70 and average<=79.9):
    grade = 'C'
elif(average>=60 and average<=69.9):
    grade = 'D'
elif(average<59.9):
    grade = 'F'
print()                                        # Displaying result on the console
print()
print("--------------------Results----------------------")
print("Lowest Score  :",min_Element)
print("Modified List :",list_Scores)
print("Scores Average:",average)
print("Grade         :",grade)
print("-------------------------------------------------")



