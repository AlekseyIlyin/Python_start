print("Введите данные для расчёта среднего значения")
print("завершите ввод данных нулём")

summa = 0
x = 1
idx = 0
while x != 0:
    x = float(input())
    if x == 0 and idx == 0:
        print("ошибка")
    summa += x
    idx += 1
if idx > 1:
    print("Среднее введённых значений равно: ", summa / (idx - 1))


    # 2 задача

print("Градусы Цельсия (С)\t Градусы Фаренгейта (F)")
 # print(len("Градусы Цельсия (С)"))
for tempC in range(0, 101, 10):
    tempF = tempC * 9 / 5 + 32
    print("{:10d}\t\t {:10.0f}".format(tempC, tempF))


    # 3 задача

A, B = int(input("Введите два целых числа: ")), int(input())
NOD = 1
operations = 0
for n in range(2, min(A, B) + 1):
    operations += 1
    if A % n == 0 and B % n == 0:
         NOD = n
print("NOD = ", NOD, " operations = ", operations)