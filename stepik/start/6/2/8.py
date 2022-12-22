# Три города
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
#
# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
#
# Примечание. Гарантируется, что длины названий всех трех городов различны.
cityName1 = input()
cityName2 = input()
cityName3 = input()
cityNameLen1 = len(cityName1)
cityNameLen2 = len(cityName2)
cityNameLen3 = len(cityName3)
if cityNameLen1 < cityNameLen2 and cityNameLen1 < cityNameLen3:
    print(cityName1)
if cityNameLen2 < cityNameLen1 and cityNameLen2 < cityNameLen3:
    print(cityName2)
if cityNameLen3 < cityNameLen1 and cityNameLen3 < cityNameLen2:
    print(cityName3)
if cityNameLen1 > cityNameLen2 and cityNameLen1 > cityNameLen3:
    print(cityName1)
if cityNameLen2 > cityNameLen1 and cityNameLen2 > cityNameLen3:
    print(cityName2)
if cityNameLen3 > cityNameLen1 and cityNameLen3 > cityNameLen2:
    print(cityName3)