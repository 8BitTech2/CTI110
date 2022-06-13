# program to compute how many gallons of paint are needed to cover the given
# square feet of walls. Assume 1 gallon can cover 350.0 square feet.

# gallons = the square feet divided by 350.0.
wall_area = float(input('Enter the Wall Area in Sq. Ft.:'))
gallons_paint = (wall_area / 350)

# Assign gallons_paint below
print('If Wall Area is:', f'{wall_area:.2f}')


print('The amount of paint in gallons needed is:', f'{gallons_paint:.12f}')
