# Variables, input, and type conversion
#

user_int = int(input('Enter integer (32 - 126):\n'))

float = float(input('Enter float:\n'))

character = str(input('Enter character:\n'))

string = str(input('Enter string:\n'))

# 1): Finish reading other items into variables, then output the four values on a single line separated by a space
print(user_int, float, character, string)

# (2): Output the four values in reverse
print(string, character, float, user_int)

# (3): Convert the integer to a characer, and output that character
print(user_int, 'converted to a character is', chr(user_int))
      
