# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
mull = 1
for count in range(0, 10):
    num = int(input())
    if num != 0:
        mull *= num
print(mull)