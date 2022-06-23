# nested loops examples

count = 0
for i in range(5):
   for j in range(4):
      count = count + 1
print(count)
# Anwser is 20

count = 0
for i in range(4, 8):
   for j in range(2):
      count = count + 1
print(count)
# Anwser is 8

i = 0
count = 0
while i < 2:
   for j in range(3, 8):
      count = count + 1
   i = i + 1
print(count)
# Anwser is 10

letter1 = 'h'
while letter1 < 'j':
    letter2 = 'w'
    while letter2 <= 'x':
        print(f'{letter1}{letter2}')
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)
'''
Answer:
hw
hx
iw
ix
'''

i = 1
while i < 21:
    j = 5
    while j <= 8:
        print(f'{i}{j}')
        j = j + 3
    i = i + 19
'''
Answer:
15
18
205
208
'''
