def func1():
    print('Hello world') 

func1() 

def greet():
    print('Guten Tag')
greet()

# write a func to greet a user with "Good Morning"
user = 'Sakib'
def greet2():
    print(f"Good Morning {user}")
greet2()

# function default parameter
def greet(name = "Boss"):
    print(f"Good Morning {name}")

greet()
greet('sakib')

# function with arguments
def greet(name):
    gre = 'GOOD MORNING' + name
    return gre
greet("Sakib")
