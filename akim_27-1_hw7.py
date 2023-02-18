ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0,ten))
print(list(map(lambda x: x**2, evens)))
while True:

    try:
        def index(list1,a):
            print(list1[int(a)])
            return
        input1 = input("Введите индекс: ")
        index(ten, int(input1))
    except IndexError:
        print("несуществующий индекс")

    except ValueError:
        if input1 != "exit":
            print('неверный индекс, введите число')
    if input1 == "exit":
        break