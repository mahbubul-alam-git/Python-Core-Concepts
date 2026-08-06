# print funtion uses...
print("Hello World")
print("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.")

# Simple funtion doing sum
def add_numbers(num1,num2):
    return (num1 + num2)

user_input_01 = float(input("Enter your first digit:"))
user_input_02 = float(input("Enter your second digit:"))

total = add_numbers(user_input_01,user_input_02)
print(f"Total number is {total}")

# Greeting the user 
users = input("Please enter your name: ")
print(f"Good Afternoon {users}\nKindly scan your ID card!")

# find() method returns the index of the first occurrence of the specified value.
rhyme = 'saki b, a  s'
find = rhyme.find("  ")
print(find)
