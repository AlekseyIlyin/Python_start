
digStr = input("Задайте первое слагаемое: ")
error = False
digComps = digStr.split(".")
if len(digComps) == 2:
    if digComps[0].find("-") != -1:
        digComps[0] = digComps[0].replace("-", "")
        sign = -1
    else:
        sign = 1
    lDigComps = len(digComps[1])
    dig = int(digComps[0]) * sign + int(digComps[1]) * sign / 10 ** lDigComps
elif digStr.find("-") != -1:
    digStr = digStr.replace("-", "")
    dig = int(digStr) * -1
elif digStr.isdigit():
    dig = int(digStr)
else:
    error = True

if error:
    print("Вы ввели не число")

errorDig1 = error
if not error:
    dig1 = dig

digStr = input("Задайте второе слагаемое: ")
error = False
digComps = digStr.split(".")
if len(digComps) == 2:
    if digComps[0].find("-") != -1:
        digComps[0] = digComps[0].replace("-", "")
        sign = -1
    else:
        sign = 1
    lDigComps = len(digComps[1])
    dig = int(digComps[0]) * sign + int(digComps[1]) * sign / 10 ** lDigComps
elif digStr.find("-") != -1:
    digStr = digStr.replace("-", "")
    dig = int(digStr) * -1
elif digStr.isdigit():
    dig = int(digStr)
else:
    error = True

if error:
    print("Вы ввели не число")

errorDig2 = error
if not error:
    dig2 = dig

if not errorDig1 and not errorDig2:
     print("Сумма a + b = {:.3f}".format(dig1 + dig2))
