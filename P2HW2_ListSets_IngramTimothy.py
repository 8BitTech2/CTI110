# CTI-110
# P2HW2 - List and Sets
# Timothy Ingram 
# 13Jun2022
#
# Program assesses the understanding of Lists and Sets
# Glasses of water drank per day during the week excluding Sunday

# Asks the user to enter a series of 6 numbers.(10 points)

print ('provide the number of glasses you drank on a daily basis')
print ('this week, excluding Sunday:')
print()
num1 = float(input('number 1: '))
num2 = float(input('number 2: '))
num3 = float(input('number 3: '))
num4 = float(input('number 4: '))
num5 = float(input('number 5: '))
num6 = float(input('number 6: '))
print()

# store the numbers in a list. Give the list created a descriptive name
print('Created list')
daily_glasses = ([num1,num2,num3,num4,num5,num6])
print (daily_glasses)

# print the lowest number in the list
s_glasses = min(daily_glasses)
print('Smallest number  in list:', s_glasses)

# The highest number in the list
l_glasses = max(daily_glasses)
print('Largest number  in list:', l_glasses)

# The total of the numbers in the list
total = sum(daily_glasses)
print('Sum of numbers  in List:', total)

# The average of the numbers in the list
avg = total/len(daily_glasses)
print('Average of numbers in List:', avg)
print()

# Convert to set
daily_set = set(daily_glasses)
# Display list and set content
print('Created set')
print(daily_set)

# Note that if list contained duplicated numbers, duplicates will no longer appear in the set created.

