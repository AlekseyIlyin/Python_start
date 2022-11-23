# сколько единиц в двоичной записи числа 4**1015 - 2** 1014 +5
n = 1015
a = 4**n
b = 2**(n -1)
print(a - b + 5)
print("{:0b}".format(a - b + 5))
s ="{:0b}".format(a - b + 5)
print("тип переменной s:", type(s))
cn = 0
for i in range(len(s)):
    if s[i] == '1':
        cn += 1
print(cn)