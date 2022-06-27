#  Function call with parameters - Converting measurements
'''
Define a function calc_total_inches, with parameters num_feet and num_inches, that returns the total number of inches. Note: There are 12 inches in a foot.

Sample output with inputs: 5 8
Total inches: 68
'''

def calc_total_inches (num_feet, num_inches): 
     return num_feet * 12 + num_inches
    
feet = int(input('Enter # of feet:'))
inches = int(input('Enter # of inches:'))
print('Total inches:', calc_total_inches(feet, inches))
