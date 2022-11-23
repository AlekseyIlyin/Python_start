# 4 ЗАДАЧА

import random
import math
a, b = int(input("Введите границы интервала для случайного выбора")), int(input())
x = random.randint(a, b)
lim = b - a
cnt = 0
phi = (math.sqrt(5) - 1) / 2
while True:
    z = int((a + b) / 2)
    cnt += 1
    if z < x:
        a = z