# Цвет настроения синий
# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока
# «синий» и «NO» в противном случае.
#
# Формат входных данных
# На вход программе подается одна строка.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
str = input()
if 'синий' in str:
    print('YES')
else:
    print('NO')