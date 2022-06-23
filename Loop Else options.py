# Loop Else options
result = 0
n = 2
while n < 5:
    print(n, end=' ')
    result += 2
    n += 1
else:
    print(f'/ {result}')
print('done')

'''
2 3 4 / 6
done
'''

result = 1
n = 2
while n > -1:
    print(n, end=' ')
    result *= 4
    n -= 1
else:
    print(f'\ {result}')
print('done')
'''
2 1 0 \ 64
done
'''

result = 0
n = 1
while n < 9:
    print(n, end=' ')
    result += 4
    if result > 9:
        print('@')
        break
    n += 1
else:
    print(f'/ {result}')
print('done')
'''
1 2 3 @
done
'''
result = 0
for n in range(3):
    print(n, end=' ')
    result += 4
else:
    print(f'\ {result}')
print('done')
'''
0 1 2 \ 12
done
'''

stop = 18
total = 0
for number in [4, 6, 7, 5, 3, 7]:
    print(number, end=' ')
    total += number
    if total > stop:
        print('$')
        break
else:
    print(f'| {total}')
print('done')
'''
4 6 7 5 $
done
'''





