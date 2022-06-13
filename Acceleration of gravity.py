# Acceleration of gravity

# Compute the approximate acceleration of gravity for an object above the
# earth's surface, assigning accel_gravity with the result. The expression
# for the acceleration of gravity is: (G * M) / (d 2), where G is the
# gravitational constant 6.673 x 10-11, M is the mass of the earth 5.98 x 1024
# (in kg), and d is the distance in meters from the Earth's center
# (stored in variable dist_center).

# Sample output with input: 6.3782e6 (top of Mt. Everest)
# (100 m above the Earth's surface at the equator)


G = 6.673e-11
M = 5.98e24
accel_gravity = 0.0

# user input of meters above the surface
dist_center = float(input('Distance in meters from the Center of Earth:'))

# Calculate the graviational force(F) and acceleration due to gravity(g) caused
# by the gravitational force exerted by the earth.
accel_gravity = (G * M) / dist_center**2

print(f'Acceleration of gravity: {accel_gravity:.2f}')
