# Many Values to Multiple Variables

x, y, z = "orange", "banana", "cherry"

print(x)
print(y)
print(z)
print(x, y, z)

"""
num =  5
name = "Abu SHahma"
print(num + name)
# this give error
"""

# Global Variable

name1 = "Very beginner friendly language"

def myfunc():
    print("Python is " + name1)

myfunc()

name2 = "awesome"

def myfunc1():
    name2 = "fantastic"
    print("Python is " + name2)
    print("Python is " + name2)

myfunc1()

def hello():
    global x1
    x1 = "Nice"

hello()
print("Pytohn is " + x1)

x2 = "Good"

def hello2():
    global x2 
    x2 = "fantastic"

hello2()

print("Python is " + x2)





