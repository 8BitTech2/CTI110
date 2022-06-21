# Conditional expression: Print negative or non-negative
# conditional expression that evaluates to string "negative"
# if user_val is less than 0, and "non-negative" otherwise.


user_val = int(input('enter a neg or non-neg #'))

cond_str = 'negative' if (user_val < 0) else 'non-negative'

print(user_val, 'is', cond_str)

