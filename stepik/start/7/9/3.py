# Делители - 1 🌶️
# На вход программе подается два натуральных числа a и b(a < b).
# Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.
#
# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести два числа на одной строке, разделенных пробелом: \
# число с максимальной суммой делителей и сумму его делителей.
#
# Примечание.
# Если таких чисел несколько, то выведите наибольшее из них.
a = 61 #int(input())
b = 71 #int(input())
numberWithMaxSummDividers = a
maxSummDiv = 0
summDiv = 0
for num in range(a, b + 1):
    summDiv = 0
    for div in range(1, num + 1):
        if num % div == 0:
            summDiv += div
    if maxSummDiv <= summDiv:
        numberWithMaxSummDividers = num
        maxSummDiv = summDiv
print(numberWithMaxSummDividers, maxSummDiv)
