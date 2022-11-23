sp = []
for i in range(4):
    x = int(input('Введите число: '))
    sp.append(x)

sp1 = [el**3 for el in sp] # Генератор списка
print(sp, sp1)