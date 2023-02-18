first = (int(input("Введите первое число:")))
a = (input("Введите знак:"))
second = (int(input("Введите второе число:")))
otvet = (int)
if a == "+":
    otvet = first + second
elif a == "/":
    otvet = first / second
elif a == "*":
    otvet = first * second
elif a == "-":
    otvet = first - second
else:
    otvet = "Неверный знак"


print(otvet)