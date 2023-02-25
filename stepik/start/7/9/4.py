# Делители-2
# На вход программе подается натуральное число n. Напишите программу, выводящую графическое изображение делимости чисел от
# 1 до n включительно. В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести графическое изображение чисел от 1 до n, каждое на отдельной строке.
n = int(input())
for num in range(1, n + 1):
    print(num, end='')
    for div in range(1, num + 1):
        if num % div == 0:
            print('+', end='')
    print()
