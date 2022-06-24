# CTI-110
# P4HW2 - Expenses
# Timothy Ingram
# 24Jun2022
#
'''
here are the steps for this program: 
Input
 1.  ask user for the amount of money in account
 2.  ask user for the expense amount for # 1
3.  ask user if they would like to withdraw again
4.  if so, how much, if not then run calculations
 Processing 
5.  calculate the total buy subtracting the expense(s)
6.  calculate the number of expenses that were processed
7. calculate the remaining amount in account
Results 
7.  display a set of results that includes amount before and after expenses and the # of transactions
'''

starting_amount = float(input("Enter starting amount in account $"))#for entering starting amount
count = 1                                                           #for keeping count of expenses
remaining_amount = 0                                                #for remaining_amount 
temp = starting_amount                                              #storing starting amount in temp
# 10 
while(True):                                                        #for asking expenses again and again
    isExpense = ''
    print("\nEnter expense",count,":", end =" ")                    #for asking user if he want to continue entering expense 
    expense = float(input())                                        #asking user to enter expense
    remaining_amount = temp - expense                               #Calculating remaining amount 
    temp = remaining_amount                                         #updating temp 
    count = count + 1                                               #increasing counter
    isExpense = input("Do you want to enter another expense?(y/n) ")#asking user if he want to enter more expenses 
    if(isExpense == 'y'):                                           #if yes 
        continue
    elif(isExpense == 'n'):                                         #if no 
        break                                                       #break the loop

#printing the details 
print("\nAmount in account before expenses subtracted $", starting_amount) #starting amount
print("Number of expenses entered:", count-1)                              #number of expenses 
print("Amount in account after expenses subtracted is $", remaining_amount)#remaining balance
