# Сортировка трёх 🌶️
# Напишите программу, которая упорядочивает три числа от большего к меньшему.
#
# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.
dig1 = int(input())
dig2 = int(input())
dig3 = int(input())
if dig1 < dig2:
    dig1, dig2 = dig2, dig1
if dig2 < dig3:
    dig2, dig3 = dig3, dig2
if dig1 < dig2:
    dig1, dig2 = dig2, dig1
print(dig1, dig2, dig3, sep='\n')