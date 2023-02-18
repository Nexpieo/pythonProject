"""Структуры данных: словари, множества"""
# numbers1 = {1, 2, 3, 2, 1, 4, 3}#set -множество (изменяемый тип данных)
# numbers1.add(2)
#
# print(numbers1)

# lagman = {"мясо", "тесто", "лук"}
# manty = {"мясо", "перец", "лапша"}
# print(lagman.union((manty)))#можно заменить на |
# print(lagman.intersection(manty))#можно заменить на  &
# print(lagman.difference(manty))#можно заменить на -
# print(lagman.symmetric_difference(manty))#можно заменить на ^

# {key: value}({ключ:значение})
# print(type(student))
# print(student)
# new = dict(enumerate('python'))
# print(new)

new = dict(name = 'donald', age = 19, country = "USA")
student = {
    'name': "jack",
    "age": 20,
    'weight': 65.7,
    "hobby":['chess', 'english', 'books'],
    'sex': "male"
}
print(student)
# словарь - dictionary(dict)
# for k, v in student.items():
#     print(f'{k} == {v}')



#print(student.keys())#вывести только ключи
#print(student.values())#вывести только значения
#print(student.items())#вывести все по парам

"""удаление"""
# del student["hobby"][-1]
# deleted = student.pop('weight')
# print(deleted)
# del student ['hobby']
# new['weight'] = deleted
# print(new)

"""изменение"""
# student["sex"] = 'female'
# student["hobby"][0] = 'football'
# student["age"] += 1

"""добавление"""
# student['car'] = True
# student["hobby"].append('boxing')
# student.update(new)

# print(student)
# data = ["cola", "cola", "lays", "pepsi", "cola", "lays"]
#
# res = {i: data.count(i) for i in data}
# print(res)
# print(max(res.values()))