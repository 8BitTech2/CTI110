# Face-printing program
nose = '0'  # Looks a little like a nose
user_value = '-'

while user_value != 'q':
    print(f' {user_value} {user_value} ')  # Print eyes     
    print(f'  {nose}  ')  # Print nose     
    print(user_value*5)  # Print mouth
    print('\n')

    # Get new character for eyes and mouth
    user_input = input("Enter a character ('q' for quit): \n")
    user_value = user_input[0]

print('Goodbye.\n')

# Iterate while c equals 'g'.
#  while c=='g'    As long as c is 'g', the loop executes 

# Iterate until c equals 'z'.
#     while !='g'  word "until", meaning to loop while c does not equal 'z'
#  
