# Basic function call.
'''
Complete the function definition to return the hours given minutes.
Sample output with input: 210.0
3.5
'''
def get_minutes_as_hours(orig_minutes):
     return orig_minutes/60

minutes = float(input('type the minutes to compute:'))
print(get_minutes_as_hours(minutes))
