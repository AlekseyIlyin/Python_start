# 2 задача

A, B = int(input("Введите два целых числа: ")), int(input())
NOD = 1
operations = 0
for n in range(2,min(A,B)+1):
    operations +=1
    if A%n == 0 and B%n == 0:
        NOD = n
print("NOD =", NOD," operations = ", operations)

