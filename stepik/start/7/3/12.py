# На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы
# 1-2+3-4+5-6+...+(-1)^n+1 * n
n = int(input())
sign = 1
summ = 0
for count in range(1, n + 1):
    summ += count * sign
    sign *= -1
print(summ)