# user mute be greater than 18 or equal to 18 to vote
users = int(input('Enter your age: '))
if (users >=18 and users <70):
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

# Write 4 numbers by users and find greatest number among them
a1 = int(input("Enter your 1st number: "))
a2 = int(input("Enter your 2nd number: "))
a3 = int(input("Enter your 3rd number: "))
a4 = int(input("Enter your 4th number: "))

if (a1>a2) and (a1>a3) and (a1>a4):
    print(f"Greatest number is: {a1}")
elif (a2>a1) and (a2>a3) and (a2>a4):
    print(f"Greatest number is: {a2}")
elif (a3>a2) and (a3>a1) and (a1>a4):
    print(f"Greatest number is: {a3}")
elif (a4>a2) and (a4>a3) and (a4>a1):
    print(f"Greatest number is: {a4}")
