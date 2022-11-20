a = input("Задайте первое слагаемое")
b = input("Задайте второе слагаемое")
error = False

# Проверка: Есть ли точка в веденной строке
if a.find(".") != -1:
    # Если введены НЕ целые числа с десятыми
    # Получение массива строк
    aComps = a.split(".")
    laComps = len(aComps[1])
    a = int(aComps[0] + aComps[1]) / 10 ** laComps
else:
    if a.isdigit():
        a = int(a)
    else:
        print("a - Вы ввели не число")
        error = True

if b.find(".") != -1:
    bComps = b.split(".")
    lbComps = len(bComps[1])
    b = int(bComps[0] + bComps[1]) / 10 ** lbComps
else:
    if b.isdigit:
        b = int(b)
    else:
        print("b - Вы ввели не число")
        error = True

if not error:
    print("Сумма a + b = {:.3f}".format(a + b))
