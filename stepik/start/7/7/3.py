count = 0
p = 1
x = 0
for i in range(1, 10+1):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')