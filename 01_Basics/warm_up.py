# print funtion uses...

print("Hello World")
print("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.")


# Simple funtion doing sum
def add_numbers(num1,num2):
    return (num1 + num2)

f = float(input("Enter your first digit:"))
s = float(input("Enter your second digit:"))

a = add_numbers(f,s)
print(f"Total number is {a}")
