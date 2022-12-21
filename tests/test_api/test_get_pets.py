from api import PetFriends
from conftest import *
from generators import *

pf = PetFriends()

class TestCasesPositive:

    @pytest.mark.parametrize("filter",['', 'my_pets'],ids=['empty string', 'only my pets'])
    def test_get_pets_with_valid_key(self, auth_key, filter):
        """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой.
        Доступное значение параметра filter - 'my_pets' либо '' """
        status, result = pf.get_list_of_pets(auth_key, filter)

        assert status == 200
        assert len(result['pets']) > 0

class TestCasesNegative:

    def test_no_pets_shown_for_unauthorized_user(self, filter=''):
        """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой.
        Доступное значение параметра filter - 'my_pets' либо '' """

        auth_key = {'key': ''}
        status, result = pf.get_list_of_pets(auth_key, filter)

        assert status == 403
        assert 'pets' not in result