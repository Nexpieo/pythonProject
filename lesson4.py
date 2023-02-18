# numbers = [(1, 2), (1,2)]
#
# numbers = list(numbers)
#
# numbers.append(34)
#
#
# print(numbers)


#new = tuple("oop")#превратить в кортеж
#print(new)


# a = "qwe", "asd" #кортеж - неизменяемый список(tuple)
# print(a)
# print(type(a))


num = [23, 4.6, True]
# num = [i for i in num if type(i) not in [int, float]]#выводить все значения кроме int float
num = [i**2 for i in num]# умножить все значения на 2
print(num)


# objects = [False, 24, 13, 'python', 'java', 2.7, 1.38, True] #Список []
# # print(objects, new, sep = '\n') #перенос строки
# new = objects
# print(id(objects))
# print(id(new))
#
# print(objects == new)
# print(objects is new)
#
# print(objects)
# print(new)


"""добавление"""
# objects.append(new) #добавить в конец
#objects.insert(4, new) #добавить в укащанное место (индекс, куда вставить , что вставить)
#objects.extend(new)#добавить отдельно
#objects += new #также как и extend

"""изменение"""
# objects[3], objects[4] = objects[4], objects[3]
#objects.reverse()#перевернуть
#objects[-3] = 3 #замена
#objects[3:5] = ["php"]
#objects[objects.index(13)] = [23, 24, 35]
#objects.sort(reverse=True)#отсортировать по значениям(наоборот)
# objects.sort(key=len, reverse=True)



'''удаление'''
# del objects[1: -1] #[начальное число:конечное число:шаг]
#
# objects = ['s', 'asd', 13, 345]
# print(objects)
#objects.clear()#полное удаление
#objects.remove(24) #удаление по значению
#objects.remove('python') #удаление по значению
# deleted = objects.pop(1) #удаление по индексу
# print(deleted)
#print(objects)
