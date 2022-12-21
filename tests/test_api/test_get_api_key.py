from api import PetFriends
from conftest import *
from settings import *

pf = PetFriends()

class TestCasesPositive:

    def test_get_api_key_for_valid_user(self, email=valid_email, passwrd=valid_password):
        """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.get_api_key(email, passwrd)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 200
        assert 'key' in result

class TestCasesNegative:

    def test_no_auth_key_for_invalid_password(self, email=valid_email, password=invalid_password):
        """ Проверяем что запрос api ключа возвращает статус 403 и в результате не содержится слово key"""

        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.get_api_key(email, password)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 403
        assert 'key' not in result


    def test_no_auth_key_for_invalid_email(self, email=invalid_email, password=valid_password):
        """ Проверяем что запрос api ключа возвращает статус 403 и в результате не содержится слово key"""

        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.get_api_key(email, password)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 403
        assert 'key' not in result