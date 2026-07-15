# python operator

print(10 + 5)

sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2
print(sum3)

x = 16
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assignment operator

numbers = [1,2,3,4,5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Ternary Operator

num = 6
x = "WEEKEND!" if num > 5 else "Workday"

print(x)

num2 = 7

x1 = "Fri" if num2 == 5 else "Sat" if num2 == 6 else "Sun" if num2 == 7 else "weekday"

print(x1)