# write a program to print the numbers from 1 to 5 using for loop
l = [ 1,2,3,4,5]
for item in l:
    print(item)
    
# write a program to print the numbers from 0 to 10 in steps of 2
for i in range(0,5,2):
    print(i)

# write a program to print the numbers from 10 to 1 in reverse order and execute the else block after the loop is completed
for i in range(10,0,-1):
    print(i)
else:
    print('Done')

# for loop with break statement
for i in range(0,100):
    print(i)
    if (i == 50):
        break

# for loop with continue statement it will skip the current iteration and continue with the next iteration of the loop 
for i in range(1,10):
    # print('Printing')
    if i == 2:
        continue
    print(i)
