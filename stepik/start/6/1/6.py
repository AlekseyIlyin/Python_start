# 451 градус по Фаренгейту
# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту».
# Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.
#
# Используйте формулу для перевода: C = 5/9 (F - 32)
#
# Формат входных данных
# На вход программе подаётся вещественное число градусов по шкале Фаренгейта.
#
# Формат выходных данных
# Программа должна вывести число градусов по шкале Цельсия.
f = float(input())
print(5/9 * (f - 32))