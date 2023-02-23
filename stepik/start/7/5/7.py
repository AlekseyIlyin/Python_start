# Все вместе
# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
num = int(input())
summ = 0
countDigs = 0
multDigs = 0
avr = 0

digit = num % 10
num = num // 10
summ += digit
countDigs += 1
lastDig = digit
multDigs = digit

while num != 0:
    digit = num % 10
    num = num // 10
    summ += digit
    countDigs += 1
    multDigs *= digit

print(summ)
print(countDigs)
print(multDigs)
print(summ / countDigs)
print(digit)
print(digit + lastDig)