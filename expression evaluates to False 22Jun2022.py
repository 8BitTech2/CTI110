# Statements to execute after the expression evaluates to False
curr_power = 2
user_char = 'y'

while user_char != 'n':
    print(curr_power)
    curr_power = curr_power * 2
    user_char = input()

print('Done')

# Assume user would enter 'a', then 'b', then 'n'
# First check: 'a' != 'n' is True. Second: 'b' != 'n' is True.
# Third: 'n' != 'n' is False (because they ARE equal),
# so loop body is not entered a third time.
#(loop runs 2 times but displays 3 outputs)
