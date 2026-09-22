# Recusion is a function which calls itself.
def num(n):
    if (n == 1 or n == 0):
        return 1
    return n * num(n-1)
n = int(input('Enter a number: '))
print(f"The factorial of this number is: {num(n)}")