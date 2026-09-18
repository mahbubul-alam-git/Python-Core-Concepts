#1 this program will print the multiplication table of a given number
user = int(input('Enter multiplication table number: '))
for i in range(1,10+1): 
    # for user in range(1,11):
    print(f'{user} X {i} = {user*i}')

#2 greet all the person which starts with 'S'
l = ['Sakib','Soham','Shifat','Sanjoy','Rahul','Akash','Shihab']
for i in l:
    if i.startswith(('S','s')): 
        print(f'Good Morning {i}')

#3 write multiplication table with while loop
user = int(input('Enter multiplication table number: '))
x = 0
while x < 10:
    x = x + 1
    print(f'{user} X {x} = {user*x}')

#4 check the prime number
user = int(input('Prime number checker: '))
if user >1:
    is_prime = True
    for i in range(2,user):
        if (user % i == 0):
            is_prime = False
            break
    if is_prime == True:
        print(f"{user} is a prime number")
    else:
        print(f"{user} is not a prime number")
else:
    print(f"{user} is not a prime number")

# 5 Write a program to find the sum of first n natural numbers using while loop
n = int(input("Enter a number: "))
sum = 0  
i = 1    
while i <= n:   
    sum = sum + i
    i = i + 1    
print(f"1 to {n} sum result {sum}")

#6 write a program to calculate the factorial of a give number using for loop .
n = int(input('Enter your factorial number: '))
l = 1

for i in range(n,0,-1): 
    l = l * i # 3*2*1 = 6
print(f'{n} factorial result is {l}')

'''
07 write a program to print following pattern.
   *
  ***
 *****
'''
n = int(input('Enter the number of rows: '))
for i in range(1,n+1):
    print(' '*(n-i) + '*'*(2*i-1)) # Print spaces and stars for each row
