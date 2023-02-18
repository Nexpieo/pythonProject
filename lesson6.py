a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
    if i == 2:
        a.remove(i)
        print(i)

# contacts = {
#     'sam': "0505234354",
#     'aza': '0702345465',
#     "uri": '0777454545'
# }
# def new_contact(name, phone):
#     if name not in contacts.keys():
#         contacts[name] = phone
#     else:
#         contacts[name] = {contacts[name]}
#         contacts[name].add(phone)
#
# new_contact("rita", "0702341324")
# new_contact("aza", "0702354654")
# print(contacts)
# '''Контакты'''


# def calculator(n1, operator, n2):
#     if operator == '+':
#         return n1 + n2
#     elif operator == "-":
#         return n1 - n2
#     elif operator == "*":
#         return n1 * n2
#     elif operator == "/":
#         return n1 / n2
# print(calculator(10, "/", 5))
'''Калькулятор'''

# def menu(**kwargs):#kwargs показывает все с названиям в виде словаря
#     print(type(kwargs))
#     print(kwargs)
#     return kwargs
# menu(eat = 'pizza', drink = 'tea', one = 1, book = 'lutz')

# def plus(*args): #вместо args можно любое название, главное *
#     return sum(args)
# print(plus(2, 3, 3, 5, 4, 6))


'''args возвращает все как кортеж, kwargs возвращает как словарь'''


# def show_objects(name, surname = 'unknown'):
#     print('name', name, "surname", surname)
#
# show_objects("peter", 'parker')
# show_objects(surname="lee", name = "bruce")


# print(help(len)) #что делает (...) команда


# def get_square(width: int, lenght: int) -> int:
#     '''Принимает 2 числа (ширина и длина), возвращает площадь прямоугольника'''
#     return width * lenght
# print(get_square(12, 23))


# def max1(iterable):
#     max_value = 0
#     for i in iterable:
#         if i > max_value:
#             max_value = i
#     return max_value
# print(max1([12, 12, 23, 24, 34, 3, 423, 123]))


# def len1(iterable):
#     counter = 0
#     for _ in iterable: #временная переменная не используется _
#         counter += 1
#     return counter
# print(len('123') + 7)
# print(len1('123') + 7)