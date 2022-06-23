# While loop: Print 1 to N
# loop that prints from 1 to user_num, increasing by 1 each time.

i = 1
user_num = int(input('enter number: '))  # assume positive


while i <= user_num:
    print(i)
    i += 1 # incrementation, if not you will have an infinite loop
    
