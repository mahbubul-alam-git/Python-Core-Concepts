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

# a student pass or fail find out by using conditional expression. evey subject marks must be greater than 33 and average must be greater than 40 to pass the exam
bangla = int(input("Enter your Bangla marks: "))
english = int(input("Enter your English marks: "))
math = int(input("Enter your Math marks: "))

avarage = (bangla + english + math) / 3

if avarage >= 40 and bangla >= 33 and english >= 33 and math >= 33:
    print(f"Congratulations! You have passed the exam with an average of {avarage:.2f}")
else:
    print(f"Sorry! You have failed the exam with an average of {avarage:.2f}")

# detect spam comment 
def_comment = ["make a lot of money", "buy now", "subscribe this", "click this", "check this out", "free gift", "limited time offer", "act now", "don't miss out", "exclusive deal"]
user = input("Enter your comment: ")
if user in def_comment:
    print("This comment is detected as spam.")
else:
    print("This comment is not detected as spam.")

#username length check
user = input("Enter your username: ")

if (len(user) < 10):
    print("your username contains less than 10 characters")
else:
    print("your username correct length")

# mark grading system 
user = int(input('Enter your mark:'))
if (user <= 100 and user >= 90):
    print('You got EX')
elif (user >= 80 and user < 90):
    print('You got A')
elif (user >= 70 and user < 80):
    print('You got B')
elif (user >= 60 and user < 70):
    print('You got C')
elif (user >= 50 and user < 60):
    print('You got D')
elif (user < 50):
    print("You got F")
else:
    ("Something wrong")
