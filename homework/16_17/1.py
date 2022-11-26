import math
import random

cnt = 0
phi = (math.sqrt(5) - 1) / 2
while True:
    # Y = int(input("Угадайте загаданное значение:"))
    # Z = int(random.randint(a, b))
    Z = int((a + b) / 2)
    cnt += 1
    if Z < X:
        # print('Больше')
        a = Z
    elif Z > X:
        # print('Меньше')
        b = Z
    elif Z == X:
        print('Победа')
        break
    if cnt > lim:
        break
print("Загаданное число:", X, "число для сравнения:", Z)
print("Число отгадано за:", cnt, "попыток")
