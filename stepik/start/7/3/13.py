# Наибольшие числа 🌶️🌶️
# На вход программе подается натуральное число n, а затем n различных натуральных чисел,
# каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
n = int(input())
firstBig = int(input())
secondBig = int(input())
if firstBig < secondBig:
    firstBig, secondBig = secondBig, firstBig
for count in range(3, n + 1):
    newBig = int(input())
    if newBig > secondBig:
        secondBig = newBig
    if firstBig < secondBig:
        firstBig, secondBig = secondBig, firstBig
print(firstBig)
print(secondBig)