# from datetime import datetime
#
# def timeit(func):
#     def wrapper():
#         start = datetime.now()
#         func()
#         print(datetime.now() - start)
#     return wrapper
# @timeit
# def one():
#     l = []
#     for i in range(10000):
#         l.append(i)
#     return f"{len(l)}"
#
# @timeit
# def two():
#     l = [i for i in range(10000)]
#     return f"{len(l)}"
#
# first = timeit(one)
# second = timeit(two)
#
# # one()
# # two()
# print(first())

#
# def make_upper(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
#
# def make_lower(func):
#     def wrapper():
#         return func().lower()
#     return wrapper
#
# @make_upper
# def hello():
#     return "Hello World"
#
# @make_lower
# def myfunc():
#     return"I love Python"
#
# print(hello())
# print(myfunc())


# def decorator_func(func):
#     def wrapper():
#         print("Функция обертка")
#         print(f"Оборачиваемая функция {func}")
#         print("Выполняем обернутую функцию")
#         func()
#         print("Выходим из обертки")
#     return wrapper
#
# @decorator_func
# def hello():
#     print('Hello world')