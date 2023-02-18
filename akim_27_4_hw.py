data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.pop(0)
deleted = numbers.pop(0)
letters.append(deleted)
numbers.insert(2, 2)

numbers.sort()
letters.reverse()
letters[1], letters[-2] = 'G', 'c'

numbers = [a**2 for a in numbers]

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)