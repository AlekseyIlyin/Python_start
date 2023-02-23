# Одинаковые цифры
# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
digit = num % 10
num = num // 10
lastDig = digit
while num > 0 and digit == lastDig:
    digit = num % 10
    num = num // 10
if digit == lastDig:
    print('YES')
else:
    print('NO')