n = int(input())
product = n % 10
n //= 10
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)