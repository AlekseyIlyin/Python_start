# Программа должна вывести на экран "да", если введенный текст - палиндром и "нет" - если нет

str = "А роза упала на лапу Азора"
str1 = str.lower().replace(" ", "")
border = len(str1) // 2
if str1[:border:1] == str1[border::-1]:
    print("да")
else:
    print("нет")