all_regions = (int(input("Введите общее количество областей:")))#Количество областей, для подсчета среднего значения

chuy = (int(input("Введите температуру в Чуйской области:")))#Команда ввода температуры отдельной области
issyk_kyl = (int(input("Введите температуру в Исык-Кульской области:")))#Команда ввода температуры отдельной области
naryn = (int(input("Введите температуру в Нарынской области:")))#Команда ввода температуры отдельной области
jalal_abad = (int(input("Введите температуру в Джалал-Абадской области:")))#Команда ввода температуры отдельной области
talas = (int(input("Введите температуру в Таласской области:")))#Команда ввода температуры отдельной области
osh = (int(input("Введите температуру в Ошской области:")))#Команда ввода температуры отдельной области
batken = (int(input("Введите температуру в Баткенской области:")))#Команда ввода температуры отдельной области

average = (chuy + issyk_kyl + naryn + jalal_abad + talas + osh + batken) / all_regions#Подсчет среднего значения

print('Средний показатель температуры воздуха по КР на сегодня', average.__round__(1), "°C")
#Команда вывода на экран среднего показателя введенных чисел