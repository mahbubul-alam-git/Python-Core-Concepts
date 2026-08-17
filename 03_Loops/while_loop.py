# write a program that uses a while loop to print the numbers from 1 to 58
i = 1
while (i<59):
    print(i)
    i = i + 1

# write a program to print the content of a list
l = [1,2,3,4,5,6,[3,32,[5,[0,4],4],0],7,8,9]
while (len(l) > 0):
    print(l[0])
    l.pop(0)

# write a program to print the numbers from 0 to 10 in steps of 2 
i = 0
while (i < 10):
    i = i + 2
    print(i)

# write a program to print the numbers from 10 to 1 in reverse order
i = 11 
while (i > 1):
    i = i - 1
    print(i)
print('Happy code journy')

# write a program to calculate the sum of numbers from 1 to 10
i = 0
summ = 0

while (i < 10):
    i = i + 1
    summ = summ + i
print(summ)
