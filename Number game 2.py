# Number game 2.
# Complete the following program

num_in_tens = int(input('Enter the tens digit:\n'))
num_in_ones = int(input('Enter the ones digit:\n'))

num_in = num_in_tens*10 + num_in_ones

print('You entered', num_in)
print(num_in, '* 11 is', num_in*11)

num_out_hundreds = num_in_tens + ((num_in_tens + num_in_ones) // 10)
num_out_tens = num_in_tens + (num_in_ones) // 1
num_out_ones = num_in_ones 

print('An easy mental way to find the answer is:')
print(num_in_tens, ',', num_in_tens, '+', num_in_ones, ',', num_in_ones)

#Build num_out from its digits:
num_out = str(num_out_hundreds) + str(num_out_tens) str(num_out_ones)  

# Note this line will generate an error until the above program is complete.
print(num_out)
