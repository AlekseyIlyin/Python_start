# Обратное число
# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
dig = float(input())
if dig == 0:
    print('Обратного числа не существует')
else:
    print(1 / dig)