# Факториал
n = int(input())
fact = 1
for count in range(1, n + 1):
    fact *= count
print(fact)