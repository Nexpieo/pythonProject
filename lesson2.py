login = "akim"
password = "qwerty"
trylog = input("Введите логин: ")
if trylog == login:
    trypass = input("Введите пароль")
    if trypass == password:
        checkpass = input("Подтвердите пароль:")
        if checkpass == trypass:
            print("Успешно")
else:
    print("неверный логин")