phone = input("Введите ваш номер телефона:")
if len(phone) != 8:
    print("Длина номера не соответствует стандарту")
else:
    if phone.isdigit():
        careNumber = "****" + phone[-4:]
        print(careNumber)
    else:
        print("Ошибка")