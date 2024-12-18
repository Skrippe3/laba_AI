import math

def main(x, y, z):
    part1 = abs(x ** (y / z) - (y / x) ** (1 / 3))
    part2 = (y - x) * (math.cos(y) - z ** 2) / (1 + (y - x) ** 2)
    return part1 + part2


if __name__ == "__main__":
    x = int(input('x= '))
    y = int(input('y= '))
    z = int(input('z= '))

    s = main(x, y, z)

    print(f"s = {s}")