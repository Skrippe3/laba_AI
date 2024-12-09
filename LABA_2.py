from math import *

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

print("Choose the form of f(x):")
print("1. sin(y - 0.5x)")
print("2. e^y")
print("3. ln(x)")

f_choice = int(input("Enter your choice (1, 2, or 3): "))
f_x = None

match f_choice:
    case 1:
        f_x = sin(y - 0.5 * x)
    case 2:
        f_x = exp(y)
    case 3:
        f_x = log(x)
    case _:
        print("Invalid choice")
        sys.exit()

a = None

if x > y:
    a = y * sqrt(f_x) + 3 * sin(x)
elif x < y:
    a = x * sqrt(f_x)
elif x == y:
    a = sqrt(abs(f_x)) + (x ** 3) / 3

print("The calculated value of a is:", a)