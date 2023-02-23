# Упорядоченные цифры 🌶️
# Дано натуральное число. Напишите программу, которая определяет,
# является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
num = int(input())
digit = num % 10
num = num // 10
lastDig = digit - 1
while num > 0 and digit >= lastDig:
    lastDig = digit
    digit = num % 10
    num = num // 10
if digit >= lastDig:
    print('YES')
else:
    print('NO')