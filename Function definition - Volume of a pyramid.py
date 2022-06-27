# Function definition: Volume of a pyramid.
'''
Define a function calc_pyramid_volume with parameters base_length, base_width, and pyramid_height, that returns the volume of a pyramid with a rectangular base.

Sample output with inputs: 4.5 2.1 3.0
Volume for 4.5, 2.1, 3.0 is: 9.45
Relevant geometry equations:
Volume = base area x height x 1/3
Base area = base length x base width.
'''

def calc_base_area(base_length, base_width):
    return base_length * base_width

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    return (calc_base_area(base_length, base_width) * pyramid_height)/3

length = float(input('Length:'))
width = float(input('Width:'))
height = float(input('Height:'))
print('Volume for', length, width, height, "is:", calc_pyramid_volume(length, width, height))
