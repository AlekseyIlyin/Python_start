# Вторая цифра
# Дано натуральное число n (n > 9). Напишите программу, которая определяет его вторую (с начала) цифру.
num = int(input())
digit = num % 10
num = num // 10
firstDig = digit
digit = num % 10
num = num // 10
secondDig = firstDig
firstDig = digit
while num != 0:
    digit = num % 10
    num = num // 10
    secondDig = firstDig
    firstDig = digit
print(secondDig)