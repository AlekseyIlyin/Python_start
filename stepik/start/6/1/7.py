# Dog age
# На вход программе подается число nn – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.
#
# Формат входных данных
# На вход программе подаётся натуральное число – количество собачьих лет.
#
# Формат выходных данных
# Программа должна вывести возраст собаки в человеческих годах.
#
# Примечание. В течение первых двух лет собачий год равен 10.5 человеческим годам.
# После этого каждый год собаки равен 4 человеческим годам.
dogAges = int(input())
firstTwoAges = min(dogAges, 2)
print(firstTwoAges * 10.5 + (dogAges - firstTwoAges) * 4)