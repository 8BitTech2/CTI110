# Calculate a factorial
# program that lets a user enter N and that outputs N! (N factorial, meaning N*(N-1)*(N-2)*...*2*1).
# Hint:Use a loop variable i that counts from total-1 down to 1.
# Compare your output with some of these answers: 1:1, 2:2, 3:6, 4:24, 5:120, 8:40320

total = int(input('Enter a number: '))  # Read user-entered number

# Initialize the loop variable
i = 1
while total > 0:
    # Set total to total * (i)
    i = i * total
    
    # Decrement i
    total = total - 1
print(i)
