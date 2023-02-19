import math

a = int(input())
b = int(input())
countCub49 = 0
resExpected = [4,9]
for count in range(a, b + 1):
   if math.pow(count, 3) % 10 in resExpected:
        countCub49 += 1
print(countCub49)