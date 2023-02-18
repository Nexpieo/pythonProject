eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,. "
rus = "йцукенгшщзхъфывапролджэячсмитьбю "


while True:
    word = input("\nВведите ваше слово: ").lower()
    if word == "exit":
        break
    for letter in word:
        if letter in eng:
            print(rus[eng.index(letter)], end = "")#end чтобы вывести все на одной строке
        else:
            print(eng[rus.index(letter)], end = "")




# word = "трактор синий"
# c = 0

# while c != len(word):  # длина переменной
#     print(word[c])  # буква под номером
#     c += 1
# word = "geektech"
# a = 0
# for i in word:
#     if i == "e":
#         a += 1
# print(a)
# for num in range(1, 11):
#     if num % 2 != 0:
#         print(num)


# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             print(i, j, k)


  # cash = 100
  # years = 5
  # percents = 0.05
  #
  # for year in range(years):
  #     cash += cash * percents
#     print(cash)



