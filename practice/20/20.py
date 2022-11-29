import random
NLEN = 30
sp = [random.randint(-10,10) for idx in range(NLEN)]
print(sp)
counter1 = 0
for idx in range(NLEN-1):
    if sp[idx] == sp[idx+1]:
        counter1 += 1
        print("idx = ", idx,", ",idx+1, ", значение:", sp[idx])
print("Количество одинаковых пар в массиве равно", counter1)


# 2 задача


import random
firstNumber = 53 #TODO:int(input())
NLEN = 30 #TODO:int(input())

K = firstNumber
if K % 2 == 0:
    K += 1
spSimplNum = []
while len(spSimplNum) < NLEN:
    flag = True
    for dev in range(3,K,2):
        if K%dev == 0:
            flag = False
            break
    if flag:
        spSimplNum.append(K)
    K += 2
print(spSimplNum)






