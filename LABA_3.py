import math

def function_value(x, a=1.9, b=1.1):
  return a * math.log(x / (b * x**2 + 2))

def for_fun(n):
    s = 0
    for i in range(1, n):
        y = function_value(i)
        s += y
    return print(s)

def while_fun(n):
    s = 0
    i = 1
    while i < n:
        y = function_value(i)
        i += 1
    return print(y)


def main():
    x1 = 3
    xn = 6
    dx = 0.3

    n = int(input("n = "))

    for_fun(n)
    while_fun(n)


if __name__ == "__main__":
    main()
