# program computes the greatest common divisor (GCD)
# greatest common divisor (GCD) among two user-entered integers num_a and num_b,
# using Euclid's algorithm: # If num_a > num_b, set num_a to num_a - num_b,
# else set num_b to num_b - num_a.
# Repeat until num_a equals num_b, at which point num_a and num_b both equal the GCD.


num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
        print(num_a)
    else:
        num_b = num_b - num_a

print(f'GCD is {num_a}') 
