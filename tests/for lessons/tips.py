# from settings import valid_email, valid_password
# import pytest
# import requests
# from datetime import datetime
# import functools
#
# import json
#
# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f"\nТест шел: {end_time - start_time}")
#
# @pytest.fixture(scope="class")
# def get_key():
#     response = requests.get('https://petfriends.skillfactory.ru/api/key',
#                             headers={"email": valid_email, "password": valid_password})
#     result = response.json()
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'key' in result, 'В запросе не передан ключ авторизации'
#     return result
#
# def logger(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         value = func(*args, **kwargs)
#         with open('log.txt', 'a', encoding='utf8') as file:
#             print(f"Вызвали {signature} \nВывело: {func.__name__!r} вернула значение - {value!r}")
#         return value
#     return wrapper
#
#
#
# def debug(func):
#     """Выводит сигнатуру функции и возвращаемое значение"""
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Вызываем {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__!r} вернула значение - {value!r}")
#         return value
#     return wrapper_debug
#
# @logger
# def request_get(headers, params):
#     res = requests.get('https://petfriends.skillfactory.ru/api/pets', headers=headers, params=params)
#     status = res.status_code
#     result = res.json()
#     return status, result
#
#
# def test_get_list_of_pets(get_key, filter = 'my_pets'):
#     headers = {'auth_key': get_key['key']}
#     params = {'filter': filter}
#     status, result = request_get(headers, params)
#     assert status == 200
#     assert len(result['pets']) > 0

#
# import pytest
#
#
# def is_triangle(a: int, b: int, c: int) -> bool:
#     if a > 0 and b > 0 and c > 0:
#         if a >= b + c or b >= a + c or c >= a + b:
#             return False
#         else:
#             return True
#     else:
#         return False
#
#
# @pytest.mark.parametrize("a", [-1, 0, 1, 3])
# @pytest.mark.parametrize("b", [-1, 0, 3])
# @pytest.mark.parametrize("c", [-1, 0, 4, 3])
# def test_it_is_triangle(a, b, c):
#     try:
#         assert is_triangle(a, b, c) == True
#     except AssertionError as e:
#         print('\nЭто не треугольник', e)
