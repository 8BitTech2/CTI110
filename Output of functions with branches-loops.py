# Output of functions with branches-loops

def print_message(message):
    if len(message) > 5:
        print('too long')
    else:
        print(message)

print_message('Can you repeat that?')
print_message('Who?')

def print_message(message):
    if len(message) > 7:
        print('too long')
    else:
        print(message)

print_message('How are you today?')
print_message('Look!')

def compute(numbers):
    result = 1
    for num in numbers:
        result *= num + 3
    return result

values = [7, 4, 6]
computed_value = compute(values)
print(computed_value)

def get_numbers():
    user_input = input()
    values = [10, 18, 8, 2, 19, 9]
    for token in user_input.split():
        values.append(int(token))
    return values

def print_selected_numbers():
    numbers = get_numbers()
    for number in numbers:
        if number <= 6:
            print(number)

print_selected_numbers()
