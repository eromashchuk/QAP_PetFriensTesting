from api import PetFriends
from conftest import *
from generators import *

pf = PetFriends()

class TestCasesPositive:

    def test_successful_update_self_pet_info(self, auth_key, name='Мурзик', animal_type='Котэ', age=5):
        """Проверяем возможность обновления информации о питомце"""

        # Получаем список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Если список не пустой, то пробуем обновить его имя, тип и возраст
        if len(my_pets['pets']) > 0:
            status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

            # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
            assert status == 200
            assert result['name'] == name
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")


class TestCasesNegative:

    def test_error_400_for_updating_not_existing_pet(self, auth_key, pet_id="0123456123456j", name='', animal_type='',
                                                     age=''):
        """Проверяем, что нельзя заменить данные несуществующего питомца"""

        # Пробуем обновить имя, тип и возраст несуществующего питомца
        status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)

        # Проверяем что статус ответа = 400
        assert status == 400



