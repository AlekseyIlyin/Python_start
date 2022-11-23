a, b = int(input("Введите диапазон A - B: ")), int(input())
if a > b:
    a, b = b, a
s = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        s += i
print("Сумма нечетных чисел =", s)

