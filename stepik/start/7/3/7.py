# Асимптотическое приближение
# (1/1 + 1/2 + 1/n) - ln(n)
import math

n = int(input())
res = 0
for count in range(1, n + 1):
    res += 1 / count
res -= math.log(n)
print(res)