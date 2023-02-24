# 12 месяцев
# Решите уравнение в натуральных числах
# 28n+30k+31m=365.
num = 365
for n in range(1, 13):
    for k in range(1, 13):
        for m in range(1, 13):
            if n * 28 + k * 30 + m * 31 == num:
                print(n, k, m)
