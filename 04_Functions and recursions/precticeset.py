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