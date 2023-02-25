n = int(input())
countThree = 0
countInLast = 0
countEven = 0
summDigAbove5 = 0
multDigAbove7 = 1
countDig05 = 0

lastDigit = n % 10

while n > 0:
    digit = n % 10
    if digit == 3:
        countThree += 1
    if digit == lastDigit:
        countInLast += 1
    if digit % 2 == 0:
        countEven += 1
    if digit > 5:
        summDigAbove5 += digit
    if digit > 7:
        multDigAbove7 *= digit
    if digit == 0 or digit == 5:
        countDig05 += 1
    n //= 10
print(countThree)
print(countInLast)
print(countEven)
print(summDigAbove5)
print(multDigAbove7)
print(countDig05)