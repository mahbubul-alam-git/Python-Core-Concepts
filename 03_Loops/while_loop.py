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
