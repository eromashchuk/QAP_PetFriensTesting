from api import PetFriends
from conftest import *
from generators import *

pf = PetFriends()

class TestCasesPositive:

    @pytest.mark.parametrize("name"
        , [generate_string(255), russian_chars(), russian_chars().upper(), chinese_chars(),
           special_chars(), '1234567890']
        , ids=['255 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    @pytest.mark.parametrize("animal_type"
        , [generate_string(255), russian_chars(), russian_chars().upper(), chinese_chars(),
           special_chars(), '1234567890']
        , ids=['255 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    @pytest.mark.parametrize("age", [1], ids=['min'])
    def test_successful_update_self_pet_info(self, auth_key, name, animal_type, age):
        """Проверяем возможность обновления информации о питомце"""

        # Получаем список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Если список не пустой, то пробуем обновить его имя, тип и возраст
        if len(my_pets['pets']) > 0:
            status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

            # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
            assert status == 200
            assert result['name'] == name
            assert result['animal_type'] == animal_type
            assert result['age'] == age
        else:
            # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")


class TestCasesNegative:

    def test_error_400_for_updating_not_existing_pet(self, auth_key, pet_id="0123456123456j", name='test', animal_type='test', age=1):
        """Проверяем, что нельзя заменить данные несуществующего питомца"""

        # Пробуем обновить имя, тип и возраст несуществующего питомца
        status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)

        # Проверяем что статус ответа = 400
        assert status == 400


    @pytest.mark.skip(reason='known bug')
    @pytest.mark.parametrize("name", ['', generate_string(1001)], ids=['empty', 'more than 1000 symbols'])
    @pytest.mark.parametrize("animal_type", ['', generate_string(1001)], ids=['empty', 'more than 1000 symbols'])
    @pytest.mark.parametrize("age",
                             ['', -1, 0, 100, 1.5, 2147483647, 2147483648, special_chars()]
        , ids=['empty', 'negative', 'zero', 'greater than max', 'float', 'int_max', 'int_max + 1', 'specials'])
    def test_error_400_for_updating_pet_with_invalid_data(self, auth_key, name, animal_type, age):
        """   """
        # Запрашиваем список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
        if len(my_pets['pets']) == 0:
            pf.add_new_pet_with_photo(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
            _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        else:
            pet_id = my_pets['pets'][0]['id']

        # Пробуем обновить имя, тип и возраст существующего питомца невалидными значениями
        status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)

        # Проверяем что статус ответа = 400
        assert status == 400



