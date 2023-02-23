# max и min
# Дано натуральное число n,(n≥10).
# Напишите программу, которая определяет его максимальную и минимальную цифры.
num = int(input())
maxDig = num % 10
minDig = maxDig
num = num // 10
while num != 0:
    digit = num % 10
    num = num // 10
    if digit > maxDig:
        maxDig = digit
    if digit < minDig:
        minDig = digit
print('Максимальная цифра равна', maxDig)
print('Минимальная цифра равна', minDig)
