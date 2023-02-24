n = int(input())
half = n // 2 + 1
for i in range(half):
    print('*' * i)
for j in range(half, 0, -1):
    print('*' * j)
