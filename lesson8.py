'''Работа с файлами.'''
#w - write   перезапись
#a - add   дозапись
#x - безконфликтный режим записи, создает файл если такого нет
#r - read


# with open('file.txt', 'r', encoding='UTF-8') as file:
#     print(file.readlines())
    #read выдает все содержимое, readlines выдает в виде списка, readline игнорирует первую строку

# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан')
# file.close() #закрыть открытый файл чтобы не засорять память

# with open('file2.txt', 'x', encoding='UTF-8') as file:
#     #with открывает файл и автоматически его закрывает
#     #as использует переменную
#     file.write('\nвторая строкa')