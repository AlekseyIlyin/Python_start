n = int(input())
for i in range(n):
    s = ''
    for b in range(n - i):
        s = s + '*'
    print(s)