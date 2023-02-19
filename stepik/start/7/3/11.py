# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
n = int(input())
dividerSumm = 0
for count in range(1, n + 1):
    if n % count == 0:
        dividerSumm += count
print(dividerSumm)