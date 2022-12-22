# Квадратное уравнение 🌶️🌶️
# Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения
# ax^2 + bx + c = 0.
# ax
# 2
#  +bx+c=0.
# Формат входных данных
# На вход программе подается три вещественных числа a != 0, b, c каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
#
# Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.
import math

a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0.0 or d == -0.0:
    print(-b / (2 * a))
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))