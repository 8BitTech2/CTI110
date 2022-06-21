# NFL Jersey numbers
# player positions have jersey numbers in specific ranges.

# An NFL wide receiver can only wear jersey numbers from 10 to 19 or 80 to 89.
if (j_num >= 10 and j_num <= 19) or (j_num >= 80 and j_num <= 89):

# Linebacker: 40 to 59 or 90 to 99
# The upper and lower bounds of the two ranges are 40 and 59 inclusive
# and 90 and 99 inclusive with a gap from 60 to 89.
if (j_num >= 40 and j_num <= 59) or (j_num >= 90 and j_num <= 99):
    print "Linebacker"

# Tight end: 40 to 49 or 80 to 89
# The two ranges are 40 to 49 and 80 to 89 with a gap from 50 to 79.
# Operator chaining is allowed.
if (40 <= j_num <= 49) or (80 <= j_num <= 89):

# Defensive lineman: 50 to 79 or 90 to 99
# Ranges can be detected using the > < relational operators or the => <=.
if (j_num > 49 and J_num < 80) or (j_num > 89 and j_num < 100):

# Quarterback: 1 to 19
# The range 1 to 19 includes numbers greater than 0 and less than 20.
if j_num > 0 or j_num < 20:

