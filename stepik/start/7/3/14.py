# Only even numbers 🌶️
# Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
flagEven = True
for count in range(1, 11):
    num = int(input())
    if num % 2 != 0:
        flagEven = False
        break
if flagEven:
    print("YES")
else:
    print("NO")