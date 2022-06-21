# Boolean operators: Detect specific values
# an expression using membership operators that prints "Special number" if 
# special_num is one of the special numbers stored in the list special_list = [-99, 0, 44].

special_list = [-99, 0, 44]
special_num = int(input('Enter number from -100 to 50:'))

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')
    
