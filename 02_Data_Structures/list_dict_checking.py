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

# create a dictionary using dict
bn_dh = { "bangladesh":"bangladesch",
         "desh":"land",
         "valo":"gut",
         "pochondor_jayga":"lieblingsland",
         "ami_tomake_valobasi":"ich_liebe_dich"
}

translation = bn_dh["ami_tomake_valobasi"] # key value pair access
print(translation)
translation = bn_dh.items() # returns a list of tuples
print(translation)

# take users eight numbers and display all unique numbers in a set
unique_numbers = []

p1 = int(input('Enter number: '))
unique_numbers.append(p1)
p2 = int(input('Enter number: '))
unique_numbers.append(p2)
p3 = int(input('Enter number: '))
unique_numbers.append(p3)
p4 = int(input('Enter number: '))
unique_numbers.append(p4)
p5 = int(input('Enter number: '))
unique_numbers.append(p5)
p6 = int(input('Enter number: '))
unique_numbers.append(p6)
p7 = int(input('Enter number: '))
unique_numbers.append(p7)
p8 = int(input('Enter number: '))
unique_numbers.append(p8)

print(set(unique_numbers))

# Meine vier Freunde und ihre Liblingsspreche in einem dict
emp_dict = {}

f1 = input('schreiben Sie ihrer Freund sprache hier : ')
emp_dict['akkash'] = f1
f2 = input('schreiben Sie ihrer Freund sprache hier : ')
emp_dict['sakib'] = f2
f3 = input('schreiben Sie ihrer Freund sprache hier : ')
emp_dict['keine_anung'] = f3
f4 = input('schreiben Sie ihrer Freund sprache hier : ')
emp_dict['mahbubul'] = f4

print(emp_dict.items())
print(f"Die Lieblingssprache von akkash ist {emp_dict['akkash']}")

# set can not have list as an element
s = {8,7,12,'hello',[1,2,3]} 
print(s)
