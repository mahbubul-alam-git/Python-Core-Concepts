# 01 write a program using function to find greatest of three numbers.
a = 1
b = 2
c = 3

def greatest (a,b,c):
    if a > b and a > c:
        print(f"The greatest numbers is {a}")
    if b > a and b > c:
        print(f"The greatest numbers is {b}")
    if c > b and c > a:
        print(f"The greatest numbers is {c}")
greatest(a,b,c)

# 02 write a program to convert Celsius to Fahrenheit.
c = float(input("Enter Celsius for converting to Fahrenheit: "))
def convert(c):
    f = (c * 1.8) + 32  #formula= f = (cx1.8)+32 
    print(f"{c}C to {f:.2f}F")

convert(c)
