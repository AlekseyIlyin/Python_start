
sp2 = [1, 5, 3, -4, -11, 7, -7, 54, 32, 34, 4]
sp1 = [7, 43, 8, 5, 322, 64, -5]
maxLen = max(len(sp1), len(sp2))
sp = []
for idx in range(maxLen):
    if idx >= len(sp1):
        sp.append(sp2[idx])
    elif idx >= len(sp2):
        sp.append(sp1[idx])
    else:
        sp.append(sp1[idx] + sp2[idx])

print(sp1)
print(sp2)
print(sp)
import random
sp4 = [[random.randint(-1000,1000) for i in range(10)] for k in range(4)]
for t_sp in sp4:
    print(t_sp)
print("---------------------------------------")
row = int(input("Выберите строку для вывода на экран:"))
if 1 <= row and row < len(sp4):
    print(sp4[row-1])
else:
    print("Ошибка!Указанной строки не существует!")
t_mas = []
colomn = int(input("Выберите столбец для вывода на экран:"))
if 1 <= colomn and colomn < len(sp4[0]):
    for row in sp4:
        t_mas.append(row[colomn-1])
    print(t_mas)
else:
    print("Ошибка!Указанной строки не существует!")