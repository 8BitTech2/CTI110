
# Assign point_dist with the distance between point (x1, y1) and point (x2, y2).
# The calculation is: Distance = SquareRootOf( (x2 - x1)2 + (y2 - y1)2)

import math

x1 = float(input('x1:'))
y1 = float(input('y1:'))
x2 = float(input('x2:'))
y2 = float(input('y2:'))



point_dist = math.sqrt((x2 - x1)**2+(y2 - y1)**2) 

print('Points distance:', point_dist)

