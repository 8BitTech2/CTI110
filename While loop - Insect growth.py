# While loop: Insect growth
# Given positive integer num_insects, a while loop that prints,
# then doubles, num_insects each iteration.
# Print values ≤ 100. Follow each number with a space.
# Must be >= 1

num_insects = int(input('Type a number: ')) 

print(num_insects, end=' ')
while num_insects < 100:
        num_insects = num_insects * 2
        if num_insects <= 100:
            print(num_insects, end=' ')
        else:
            break
        

        

        
    
