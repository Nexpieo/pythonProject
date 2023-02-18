dict = dict()
with open('results.txt', 'r', encoding='UTF-8') as file:
    for i in file.read().split('\n'):
        key = i.split(" ")[2]
        value = i.split(" ")[3:]
        dict[key] = value
sorted_dict = {}
sorted_keys = sorted(dict, key=dict.get, reverse=True)
for w in sorted_keys:
    sorted_dict[w] = dict[w]
print(sorted_dict.get(sorted_dict, ))
