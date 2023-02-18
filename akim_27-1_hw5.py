GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del GeekTech['bag']

GeekTech['address'] = 'Ibraimova 103'

GeekTech['number'] = '+996507052018'
GeekTech['Instagram'] = 'geektech_edu'

GeekTech['courses'] += 'IOS', 'UX/UI', 'Основы'
GeekTech['courses'] = set(GeekTech['courses'])

GeekTech['date'] = '2018'

courses_amount = 0
for i in GeekTech['courses']:
    courses_amount += 1
GeekTech['courses amount'] = courses_amount

for a, b in GeekTech.items():
    print(f'{a}:{b}')