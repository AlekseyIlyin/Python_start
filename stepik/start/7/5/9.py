# Одинаковые цифры
# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
for divider in range(2, num + 1):
    if num % divider == 0:
        break
print(divider)