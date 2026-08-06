# This program takes input from the user for seven fruit names and stores them in a list. It then prints out the list of fruits that the user likes.
user_input = str([input("Enter seven fruits name:")])
print(f"All seven fruits you likes:\n{user_input}")

# This program will take 7 fruit names from the user and store them in a list. It will then print the list of fruits.
fruits = []

f1 = input('Enter Fruit name: ')  
fruits.append(f1)
f2 = input('Enter Fruit name: ')  
fruits.append(f2)
f3 = input('Enter Fruit name: ')  
fruits.append(f3)
f4 = input('Enter Fruit name: ')  
fruits.append(f4)
f5 = input('Enter Fruit name: ')  
fruits.append(f5)
f6 = input('Enter Fruit name: ')  
fruits.append(f6)
f7 = input('Enter Fruit name: ')  
fruits.append(f7)

print(fruits)


# This program will take 6 marks from the user and store them in a list. It will then sort the list of marks and print it.
marks = []

f1 = int(input('Enter mark: '))  
marks.append(f1)
f2 = int(input('Enter mark: '))  
marks.append(f2)
f3 = int(input('Enter mark: '))  
marks.append(f3)
f4 = int(input('Enter mark: '))  
marks.append(f4)
f5 = int(input('Enter mark: '))  
marks.append(f5)
f6 = int(input('Enter mark: '))  
marks.append(f6)

marks.sort()
print(marks)
