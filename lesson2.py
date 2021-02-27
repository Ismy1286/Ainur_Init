# list_= [1, 2, 3, 4, 5, 6]
# list2 = [1, 'abc ', [1, 2, 3], (1, 2, 3)]
# print(type(list2))
# print(len(list_))
# text = 'hello world'

# method append dobavlyaet v kones spiska
# list1 = [1, 2, 3, 4, 5, 6]
# list1.append(10)
# list1.append('new element')
# print(list1)

# method extend - raswiryaet( skladivayet) spisok drugim spiskom

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [8, 9, 67]
# list1.extend(list2)
# print(list1)


# method insert - dobavlyaet element v ukazannoe mesto
# cars = ['mersedes', 'honda', 'subbaru']
# cars.insert(1, 'bmw')
# print(cars)

# method remove - udalyaet element
# cars.remove('honda')
# print(cars)

# method pop - virezayet element (po umolchaniyu posledniy)
# last_element = cars.pop()
# print(cars)
# print(last_element)

#  --------------takje po indeksu
# x = cars.pop(1)


# method index - vozvryashaet index elementa
# students = ['Shabdan', 'Mahmud', 'erkin']
# print(students.index('Mahmud'))

# method count -

# print(students.count(123))

# print(len(students)) - schitaet kolichestvo indeksov

# method reverse - razvorachivaet (perevorachivaet) spiskom
# students.reverse()
# print(students)

#  method sort - sortiruet po kakomu to kluchum

# students.sort()    sortiruet po alfavitu
# students.sort(key=len) sort-po dline
# print(students)



# method clear - udalyaet vse elementy

# method del - udalyaet po indeksu

# diapozon = list(range(50))
# print(diapozon)



# KORTEJI - ne izmenyaemy.
# TUPLE - kortej
# new_tuple = (1, 2, 4, 3, 2, 6, 8, 7, 1)
# new_tuple2 = tuple()
# print(type(new_tuple))
# # print(dir(tuple))
# print(new_tuple.count(1))
# print(new_tuple.index(2))


# SLOVARI - dictionary

# dict_ = {}
# dict2 = dict()
# capitals = {'Moscow': 'Russia', 'Bishkek': 'Kyrghyzstan', 'Kiev': 'Ukraine'}
#             kluch-----znacheniye
# print(capitals)
# print(len(capitals))
# print(dir(dict))


# method fromkeys

# dictionary = dict.fromkeys(['key1', 'key2'], 'value')
# print(dictionary)

# method get - poluchaet po kluchu znacheniye

# capitals = {'Moscow': 'Russia', 'Bishkek': 'Kyrghyzstan', 'Kiev': 'Ukraine'}
# print(capital.get('Bishkek'))

# method keys vivodit vse kluchi


#  method items() - vozvrawaet pari (kluch:znacheniye)

# pairs = capitals.items()
# print(pairs)

# method pop - udalyaet (vyrezaet)  po kluchu i znacheniye (vozvrawaet to chto hranitsya

# val = capitals.pop('Moscow')
# print(val)
# print(capitals)

# method popitem -vyrezaet poslednee znacheniye

# last_pair = capitals.popitem()
# print(type(last_pair))
# print(capitals)

# method update - skladivayet (ili dobavlyaet)
# capitals2 = {'Washington': 'USA', 'Paris': 'France'}
# capitals.update(capitals2)
# print(capitals)

#
# SOZDANIYE SLOVAREY
#  (kluchi doljni byt unikalny)
# -------------kluch-------znacheniye
# capitals2 = {'Washington': 'USA', 'Paris': 'France'}
# capitals2 = dict(Washington= 'USA', Paris= 'France'}
# capitals2 = dict([
#     ('Moskow', 'Russia')
#     ('Bishkek', 'Kyrghyzstan')
# ])

