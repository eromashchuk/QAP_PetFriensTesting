import datetime

import pytest
import requests
from settings import valid_email, valid_password

# @pytest.mark.skipif(sys.version_info < (3, 6), reason="Тест требует python версии 3.6 или выше")
# или
# minversion = pytest.mark.skipif(sys.version_info < (3, 6), reason="at least mymodule-1.1 required")
# @minversion

# @pytest.mark.xfail(sys.platform == "win32", reason="Ошибка в системной библиотеке")
# # На платформе Windows ожидаем, что тест будет падать

# @pytest.mark.xfail(raises=RuntimeError)
#     ''' следующий тест будет помечен xfail только в том случае, если произойдет исключение типа RuntimeException,
#     в противном случае тест будет выполняться как обычно (помечаться passed, если пройдет успешно,
#     и failed, если пройдет неуспешно)'''

@minversion
def test_python36_and_greater():

@pytest.fixture
def get_key():
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": valid_email, "pass": valid_password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    return response.request.headers.get('Cookie')

@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    print (f"\nТест шел: {end_time - start_time}")

def test_getAllPets(get_key):
    response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                            headers={"Cookie": get_key})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'


@pytest.fixture()
def request_fixture(request):
    print('\nFixtures name: ', request.fixturename)
    print('Scope: ', request.scope)
    print('func name: ', request.function.__name__)
    print('Class name: ', request.cls)
    print('module name: ', request.module.__name__)
    print('fsPath: ', request.fspath)
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"


def test_request_1(request_fixture):
    print(request_fixture)


class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)


'''Теперь фикстура получающая токен будет запускаться один раз перед стартом тестов из класса TestClassPets, 
   независимо от того сколько раз мы её вызовем внутри класса. 
   Таким образом мы сможем сэкономить время на получение токена, особенно когда количество тестов возрастёт. '''
@pytest.fixture(scope="class")
def get_key(request):
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": valid_email, "pass": valid_password})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print("\nreturn auth_key")
    return response.request.headers.get('Cookie')


'''Также мы добавили request_fixture, которая будет сообщать о том, что тест запущен при условии, 
   что в названии теста есть слово Pets.'''
@pytest.fixture(autouse=True)
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")


class TestClassPets:

    def test_getAllPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

    def test_getMyPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/my_pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

    def test_anotherTest(self):
        pass