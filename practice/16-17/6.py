n = int(input('Введите натуральное число: '))
f = 1
if n > 0:
    for i in range(1, n+1):
        f = f*i
    print("n! =", f)
elif n == 0:
    f = 1
    print("n! =", f)
else:
    print("Ошибка! Требуется неотрицательное значение.")