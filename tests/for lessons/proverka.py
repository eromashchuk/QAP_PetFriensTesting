# from decorators import do_twice, debug
#
# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# @my_decorator
# def my_first_decorator():
#     print("Это мой первый декоратор!")
#
# @do_twice
# def tes_twice():
#     print("\nЭто вызов функции test_twice!")
#
# @do_twice
# def tes_twice_without_params():
#     print("Этот вызов без параметров")
#
# @do_twice
# def tes_twice_2_params(str1, str2):
#     print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))
#
# @do_twice
# def tes_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#
# @do_twice
# def tet_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#     return "Done"
#
# @debug
# def age_passed(name, age=None):
#   if age is None:
#     return "Необходимо передать значение age"
#   else:
#     return "Аргументы по умолчанию заданы!"
#
# age_passed("Роман")
# age_passed("Роман", age=21)
#
