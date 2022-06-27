# Assign max_sum with the greater of num_a and num_b,
# PLUS the greater of num_y and num_z. Use just one statement.
# Hint: Call find_max() twice in an expression.

def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input('Number:'))
num_b = float(input('Number:'))
num_y = float(input('Number:'))
num_z = float(input('Number:'))

max1 = find_max(num_a, num_b)
max2 = find_max(num_y, num_z)

max_sum = max1 + max2

print('max_sum is:', max_sum)
