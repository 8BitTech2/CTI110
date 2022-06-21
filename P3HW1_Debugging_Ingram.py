# A program faculty will use to calculate student grades from number to letter format.
# 21Jun2022
# CTI-110 P3HW1 - Debugging
# Timothy Ingram
#

def main():
   
     # This program takes a number grade and outputs a letter grade
     print()
     print("This system uses 10-point grading scale")
     A_score = 90
     B_score = 80
     C_score = 70
     D_score = 60
     F_score = 59
     # Get input from user and assign it to a score variable
    
     score = int(input('Please enter the numerical score: '))

     def letter_grade_conversion(score):

     # Branching control statements to associate score to Letter grade.
         letter_grade = ""
     if score >= A_score:
         letter_grade = "A"  
     elif score >= B_score:
         letter_grade = "B"
     elif score >= C_score:
         letter_grade = "C"
     elif score >= D_score:
         letter_grade = "D"   
     elif score <= F_score:
         letter_grade = "F"

     # Print the corresponding Letter grade.
     print ("Your letter grade is:",(letter_grade))
 
main()
  



