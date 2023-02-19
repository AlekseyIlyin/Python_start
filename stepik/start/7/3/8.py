# На вход программе подается натуральное число
# n. Напишите программу, которая подсчитывает сумму тех чисел от
# 1 до n (включительно) квадрат которых оканчивается на
# 2,5 или 8
import math

n = int(input())
countQ258 = 0
resExpected = [2, 5, 8]
for count in range(1, n + 1):
    if math.pow(count, 2) % 10 in resExpected:
        countQ258 += count
print(countQ258)
