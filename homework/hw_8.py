# Введите целое число и найдите сумму всех его делителей

num = int(input())
sum = 0

endRange = num // 2
for i in range(1, endRange, 1):
    if num % i == 0:
        # print(i)
        sum = sum + i

print("Сумма делителей числа:", num, "=", sum)

