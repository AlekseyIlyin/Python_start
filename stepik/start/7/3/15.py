# Последовательность Фибоначчи 🌶️
# Напишите программу, которая считывает натуральное число n и выводит первые
# n чисел последовательности Фибоначчи.
n = int(input())
firstNum = 1
secondNum = 0
for count in range(1, n + 1):
    thirdNum = firstNum
    firstNum = thirdNum + secondNum
    secondNum = thirdNum
    print(thirdNum, end='')
