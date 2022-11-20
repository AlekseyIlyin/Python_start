phone = input("Введите строку:")
pos = phone.find("#")
if pos == -1:
    print(phone)
else:
    print(phone[:pos])