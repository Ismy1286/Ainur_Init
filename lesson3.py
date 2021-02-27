# MNOJESTVA ---- SET
# set_ = {1, 2, 3, 4}
# print(type(set_))
# set2 = set()
# set2 = {1, 2, 3, 4, 5, 2, 1}
# print(set2)
# list_ = [1, 3, 4, 5, 2, 1]
# list_ = set(list_)
# print(list_)
# set_ = {1,77,6,44,7,'adc', 'djsw'}
# print(set_)

# print(len(set_))

# add() update() dobavlyaet elementy v mnojestvo
#  dobavlyaet 1 element/ dobavlyaet mnojestva
# set_.add(1234)
# print(set)
#
# set.update(set2)
# set_ = set_ + set2

# discard() remove() --- udaleniye elementov mnojestva
# set_ = {1, 3, 6, 10, 21, 44, 32}
# set_.discard(10)
# print(set_)
# set_.discard(0)
# # set_.remove(0)
# # print(set_.pop())
# set_.clear()
# print(set_)

# metod------ union ---- obyediyaet mnojestva

# set_a = {1, 2, 4, 5, 3}
# set_b = {6, 7, 8}
# set_c = set_a.union(set_b)
# print(set_c)

# method--intersection ------ vozvrawaet novoe mnojestvo
# (soderjit mnojestva v pohojie pervom i vo vtorom)


# set_a = {1, 2, 4, 5, 3}
# set_b = {6, 4, 3, 7, 8}
# set_c = set_a.intersection(set_b)
# print(set_c)

#  method difference() ----- raznost ---vozvrashaet novoe mnojestvo, soderjashee vse
#  elementy kotoriye est v mnojestve a_set kotorih net v b_set


# set_c= set_a.difference(set_b)
# print(set_c)


#  boolean --- true---false---

# == (sravneniye)
# != ( ne ravno)
# >< (bolwe-menwe)
# >= (bolwe-ravno)
# <= (menwe-ravno)

# and (i)
# or (ili)
# not (ne)

# point = input('Введите вашу оценку: ')
# if point == '5':
#     print('Молодец')
# elif point == '4':
#     print('Хорошо')
# else:
#     print('Ты можешь лучше')
#
# point = input('Введите вашу оценку: ')
# if point.isalpha():
#     print('Введите пожалуйста цифры: ')
# elif point.isdigit():
#     if point == '5':
#         print('Молодец')
#     elif point == '4':
#         print('Хорошо')
#     elif point < '0' or point > '5':
#         print('error')
#
# else:
#     print('haaaa')




# a = int(input('Input number: '))
# b = int(input('input number: '))
#
# if a % 10 == 0 or b % 10 == 0:
#     print('Одно из чисел делится на 10 без остатка')

#
# print(True and True)
# print(True and False)
# print(False and True)
# print(True or False)
# print(False or True)
#

# text = 'pyton'
# if text == True:
#     print(True)
# else:
#     print(False)


# list_ = [1, 2, 3, 4, 5]
# if 5 in list_:
#     print('5 in list_')
# if 10 in list_:
#     print('10 in list')
# else:
#     print('10 not in list')

# text = 'i like python'
# if 'like' in text:
#     print('word "like" in text')
# if 'hello' not in text:
#     print(text)


# SIKLY  ----  while-----for-----
# range_ = int(input('input range: '))
# for i in range(range_):
#     print(i)
# range(начало, конец, шаг) - не включает последнюю цифору

# break------continue---
# for i in range(20):
#     print(text)
#     if i == 10:
#         print('break')
#         break
#     print(f'Шаг {i}')
# #
# for i in range(20):
#     print(text)
#     if i == 10:
#         print('continue')
#         continue
#     print(f'Шаг {i}')
#
# import time
#
#
# # while-----
#
# i = 0
# while i < 10:
#     print('True')
#     time.sleep(1)
#     i = i + 1
#     print(i)


