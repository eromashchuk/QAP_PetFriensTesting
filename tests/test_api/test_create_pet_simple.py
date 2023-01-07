import pytest

from api import PetFriends
from conftest import *
from generators import *

pf = PetFriends()

class TestCasesPositive:

    @pytest.mark.parametrize("name"
        , [generate_string(255), russian_chars(), russian_chars().upper(), chinese_chars(),
           special_chars(), '123']
        , ids=['255 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    @pytest.mark.parametrize("animal_type"
        , [generate_string(255), russian_chars(), russian_chars().upper(), chinese_chars(),
           special_chars(), '123']
        , ids=['255 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    @pytest.mark.parametrize("age", ['1'], ids=['min'])
    def test_successful_create_pet_simple(self, auth_key, name, animal_type,
                                          age):
        """Проверяем что можно добавить питомца с корректными данными без фото"""
        # Добавляем питомца
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert 'id' in result
        assert result['name'] == name
        assert result['age'] == age
        assert result['animal_type'] == animal_type

class TestCasesNegative:

    @pytest.mark.skip(reason='known bug')
    @pytest.mark.parametrize("name", ['', generate_string(1001)], ids=['empty', 'more than 1000 symbols'])
    @pytest.mark.parametrize("animal_type", ['', generate_string(1001)], ids=['empty', 'more than 1000 symbols'])
    @pytest.mark.parametrize("age",
                             ['', '-1', '0', '100', '1.5', '2147483647', '2147483648', special_chars()]
        , ids=['empty', 'negative', 'zero', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials'])
    def test_no_add_new_pet_simple_validation(self, auth_key, name, animal_type, age):
        """Проверяем что нельзя добавить питомца без фото с некорректными данными"""
        # Добавляем питомца
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 400

    def test_unsuccessful_add_new_pet_simple_no_auth(self, auth_key, name='Imya', animal_type="Test", age='7'):
        """Проверяем что нельзя добавить питомца без фото неавторизованному пользователю"""
        # Добавляем питомца
        auth_key = {"key": ""}
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 403

