# convert height in feet/inches to centimeters

CM_PER_INCH = 2.54
INCHES_PER_FOOT = 12
	
def height_US_to_cm(feet, inches):
   """Converts height in feet/inches to centimeters"""
   total_inches = feet * INCHES_PER_FOOT + inches
   cm = total_inches * CM_PER_INCH
   return cm
	
feet = 6
inches = 4
	
centimeters = height_US_to_cm(feet, inches)
print('Centimeters:', centimeters)
