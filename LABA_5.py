def task():
    n = int(input("Введите количество элементов списка -> "))
    x = []
    y = []

    for i in range(n):
        x.append(int(input(f"Введите элемент {i + 1} -> ")))

    for i in range(n - 1):
        if x[i] < 0 and x[i + 1] < 0:
            y.append((x[i], x[i + 1]))
    print("Исходный список: ", x)
    print("Новый список: ", str(y).replace('(', '', 1).replace(')', '', 1))


def task2():
    n = int(input("Введите количество элементов списка -> "))
    x = []
    y = []
    for i in range(n):
        x.append(int(input(f"Введите элемент {i} -> ")))
    y.append(list(dict.fromkeys(x)))


    print("Исходный список: ", x)
    print("Новый список: ", str(y).replace('[', '', 1).replace(']', '', 1))


if __name__ == '__main__':
    task()
    task2()