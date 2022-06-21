# Automobile service invoice
#Output a menu of automotive services and the corresponding cost of each service.
# Davy's auto shop services
# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# Car wax -- $12

# print title
print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

# Prompt the user for two services from the menu. 
service1_cost = 0
service2_cost = 0
service1 = input("Select first service:\n")
service2 = input("Select second service:\n")
if service1 == "Oil change":
  service1_cost = 35

elif service1 == "Tire rotation":
  service1_cost = 19

elif service1 == "Car wash":
  service1_cost = 7

elif service1 == "Car wax":
  service1_cost = 12

elif service1 == "-":
  service1 = "No service"
  service1_cost = 0

if service2 == "Oil change":
  service2_cost = 35

elif service2 == "Tire rotation":
  service2_cost = 19

elif service2 == "Car wash":
  service2_cost = 7

elif service2 == "Car wax":
  service2_cost = 12

elif service2 == "-":
  service2 = "No service"
  service2_cost = 0
  
# Output an invoice for the services selected.
# Output the cost for each service and the total cost
# Extend the program to allow the user to enter a dash (-), which indicates no service.
print()
print("Davy's auto shop invoice\n")
if service1 == "No service":
    print("Service 1: No service") 
else:
    print("Service 1: " + service1 + ", $" + str(service1_cost))

if service2 == "No service":
    print("Service 2: No service") 
else:
    print("Service 2: " + service2 + ", $" + str(service2_cost))
print()
print("Total: $" + str(service1_cost + service2_cost))


