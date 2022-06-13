import math

# The math.sqrt() function takes 81.0 as an input value,
# and produces that value's square root.

x = math.sqrt(81.0)
print(x)

# The math.fabs() function takes 2.5 as an input value,
# and produces that value's absolute value.
x = math.fabs(2.5)
print(x)


# The math.pow() function takes two arguments, 5.0 and 3.0,
# as input values. math.pow(5.0, 3.0) raises 5.0 to power 3.0.
x = math.pow(5.0, 3.0)
print(x)

# The innermost expression, -8.0 + 5.0, is evaluated first.
# Then, math.fabs() takes the result as an input value,
# and produces that result's absolute value.
x = math.fabs(-8.0 + 5.0)
print(x)

# The innermost expression, math.sqrt(9.0), is evaluated first,
# producing 3.0. Then math.pow(2.0, 3.0) is evaluated. 
x = math.pow(2.0, math.sqrt(9.0))
print(x)


# Compute z = y * square root of x
x = float(input('enter a number:'))
y = float(input('enter a number:'))

z = y * math.sqrt(x)
print(round(z, 2)) # This will output only 2 decimal places.

# compute z = (sqtr of x/y) fifth power
# z = math.pow(math.sqrt(x / y), 5)

#
# z = math.fabs(math.sqrt(y) - x)


# compute z = (sqrt of y-x) fifth power
# z = math.pow(math.sqrt(y - x), 5)

# compute z = sqrt y to the fifth - x
# z = math.sqrt(math.pow(y, 5) - x)

# compute z = sqrt y to the fifth / x
# z = math.sqrt(math.pow(y, 5) / x)

# compute z = sqrt |x| * y third power
z = math.sqrt(math.fabs(x) * math.pow(y, 3))

