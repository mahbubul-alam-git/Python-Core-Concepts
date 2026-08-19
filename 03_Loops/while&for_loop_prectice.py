# this program will print the multiplication table of a given number
user = int(input('Enter multiplication table number: '))
for i in range(1,10+1): 
    # for user in range(1,11):
    print(f'{user} X {i} = {user*i}')

# greet all the person which starts with 'S'
l = ['Sakib','Soham','Shifat','Sanjoy','Rahul','Akash','Shihab']
for i in l:
    if i.startswith(('S','s')): 
        print(f'Good Morning {i}')

# write multiplication table with while loop
user = int(input('Enter multiplication table number: '))
x = 0
while x < 10:
    x = x + 1
    print(f'{user} X {x} = {user*x}')

# check the prime number

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
