# Temperature conversion
'''
function that converts a temperature from Celsius into Fahrenheit.
Use the formula F = C x 9/5 + 32. Test your program knowing that
50 Celsius is 122 Fahrenheit.
'''
def c_to_f():
    fahrenheit = temp_c * (9/5) + 32

    return fahrenheit 

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

# Call conversion function
temp_f = (temp_c*9/5)+32

# Print result
print('Fahrenheit:' , temp_f)






