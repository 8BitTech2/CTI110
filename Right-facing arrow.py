# Input and formatted output: Right-facing arrow
# Given input characters for an arrowhead and arrow body,
# print a right-facing arrow.

# Ex: If the input is:  *  #

base_char = input('input a star')
head_char = input('input a pound')

row1= '      '+head_char
row2=base_char*6+head_char*2
row3=base_char*6+head_char*3


# print results
print(row1)
print(row2)
print(row3)
print(row2)
print(row1)
