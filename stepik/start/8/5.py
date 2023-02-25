n = int(input())
digit = 0
while n > 99:
    digit = n % 10
    n //= 10
print(digit)