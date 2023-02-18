day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))

if (31 >= day >= 21 and month == 3) or (30 >= day <= 20 and month == 4):
    print('Овен')

elif (30 >= day >= 21 and month == 4) or (31 >= day <= 21 and month == 5):
    print("Телец")

elif (31 >= day >= 22 and month == 5) or (30 >= day <= 21 and month == 6):
    print("Близнецы")

elif (30 >= day >= 22 and month == 6) or (31 >= day <= 22 and month == 7):
    print("Рак")

elif (31 >= day >= 23 and month == 7) or (31 >= day <= 21 and month == 8):
    print("Лев")

elif (31 >= day >= 22 and month == 8) or (30 >= day <= 23 and month == 9):
    print("Дева")

elif (30 >= day >= 24 and month == 9) or (31 >= day <= 23 and month == 10):
    print("Весы")

elif (31 >= day >= 24 and month == 10) or (30 >= day <= 22 and month == 11):
    print("Скорпион")

elif (30 >= day >= 23 and month == 11) or (31 >= day <= 22 and month == 12):
    print("Стрелец")

elif (31 >= day >= 23 and month == 12) or (31 >= day <= 20 and month == 1):
    print("Козерог")

elif (31 >= day >= 21 and month == 1) or (29 >= day <= 19 and month == 2):
    print("Водолей")

elif (29 >= day >= 21 and month == 2) or (31 >= day <= 20 and month == 3):
    print("Рыбы")
else:
    print("Неверная дата")