def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for a in range(i + 1, len(list)):
            if list[a] < list[min_index]:
                min_index = a
        (list[i], list[min_index]) = (list[min_index], list[i])
    return list
list_for_sort = [2, 4, 7, 1, 6, 3, 5]
print(selectionSort(list_for_sort))

def binary_search(list, num_for_search):
    n = 7
    resultok = False
    first = 0
    last = n - 1

    while first < last:
        middle = (first + last)
        if num_for_search == list[middle]:
            first = middle
            last = first
            resultok = True
            pos = middle
        else:
            if num_for_search > list[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if resultok == True:
        print(f'Элемент найден, {pos}')
    else:
        print("Элемент не найден")

binary_search(list_for_sort, 5)