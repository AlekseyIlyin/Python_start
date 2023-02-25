# Сумма факториалов

n = int(input())
summ = 0
for p in range(1, n + 1):
    fact = 1
    for num in range(1, p + 1):
        fact *= num
    summ += fact
print(summ)
