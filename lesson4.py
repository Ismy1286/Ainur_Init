# FUNKSII

# def my_func():
#     print('Hello world')
# my_func()

# def my_func(name):
#     print(f"Hello, my name is {name}")
# my_func("Erkin")

# def add(num1, num2):
#     print(num1 + num2)
# add(1, 2)
#
# def add(num1, num2, num3):
#     result = num1 + num2 + num3
#     return result
# print(add(10, 20, 30))

# def add(q, w, e, r, t, y, u, i, o, p):
#     return q + w + e + r + t + y + u + i + o + p
#
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def add(*args):
#     result = 0
#     for i in args:
#         for x in i
#             results = result + i
#             result += x
#     return result
# nums = list(range(20))
# print(add(nums))
#
# num = 100
# def myfunc():
#     num = 200
#     print(num)
#
# myfunc()
# print(num)

# def add(x, y):
#     return x + y
#
# print(add(12, 22))
# print(add('22', '33'))

# list1 = [1, 2, 3, 4, 5, 6]
# print(sum(list1))


# # REKURSIYA___--------------------------------
# def short_story():
#     print("У попа была собака, он ее любил.")
#     print("Она съела кусок мяса, он ее убил,")
#     print("В землю закопал и надпись написал:")
#     # time.sleep(1)
#     short_story()
#
# short_story()

# from datetime import datetime
# start1 = datetime.now()
#
# list_ = []
# for i in range(2000000):
#     list_.append(i)
# # print(list_)
#
# stop1 = datetime.now()
# start2 = datetime.now()
#
# list1 = [i for i in range(2000000)]
# # print(list1)
# stop2 = datetime.now()
#
# print(f"res1 = {stop1 - start1}")
# print(f"res2 {stop2 - start2}")
#
# def add(x, y):
#     return x + y
#
# lamda_func = lambda x, y: x + y
#
# print(add(2, 3))
# print(lamda_func(2, 3))

# old_list =['1', '2', '3', '4', '5', '6', '7']
# new_list =list(map(int, old_list))
# print(new_list)
#
# def func_upper(word):
#     return word.upper()
#
# list_ = list('hello world')
# print(list_)
#
# new_list = list(map(func_upper, list_))
# print(new_list)

# Erkin, [26 февр. 2021 г., 11:27:32]:
# mixed =['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
#
# zolushka =list(filter(lambda x: x == 'мак', mixed))
# print(zolushka)
#
# list_ = [i for i in range(100)]
# my_func = lambda x: x % 2 == 0
# even_numbers = list(filter(my_func, list_))
# print(list_)
# print(even_numbers)
#
# a =[1,2,3]
# b ="xyz"
# c =(None, True)
# res =list(zip(a, b, c))
# print(res)
#
# a =[1,2,3,4,5,6,7,8]
# b ="qwertyui"
# c =(None, True, False, None, True, False)
# res =tuple(zip(a, b, c))
# print(res)

