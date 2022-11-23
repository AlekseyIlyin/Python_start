# 3 задача

import random
a, b = int(input("введите границы интервала для случайного выбора")), int(input())
x = random.randint(a, b)
while True:
    y = int(input("угадайте загаданное значение:"))
    if y == "здаюсь":
        break
    elif y < x:
        print("Больше")
    elif y > x:
        print("Меньше")
    elif y == x:
        print("Победа")
print("загаданное число:", x)