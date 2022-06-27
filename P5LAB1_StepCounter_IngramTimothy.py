# CTI-110
# P5LAB1_StepCounter
# Timothy Ingram
# 27Jun2022
#
'''A pedometer treats walking 1 step as walking 2.5 feet.
Define a function named feet_to_steps that takes a float as a parameter,
representing the number of feet walked, and returns an integer that represents
the number of steps walked. Then, write a main program that reads the
number of feet walked as an input, calls function feet_to_steps() with
the input as an argument, and outputs the number of steps.
Use floating-point arithmetic to perform the conversion.'''

# Define your function here 

def feet_to_steps(feet_walked):
    return int(feet_walked / 2.5)
    

if __name__ == '__main__':
    # Type your code here.
    
    feet_walked = float(input())
    print(feet_to_steps(feet_walked))
    
'''
Program steps:
Input
1. ask user for the total number of feet walked.

Process:
1. receive input and divide by 2.5
2. call a function that produces the conversion to steps

Output:
1. display the conversion from feet to steps statement
'''
