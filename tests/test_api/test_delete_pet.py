from api import PetFriends
from conftest import *
from settings import *
from generators import *
import os

pf = PetFriends()

class TestCasesPositive:

    def test_successful_delete_self_pet(self, auth_key):
        """Проверяем возможность удаления питомца"""

        # Запрашиваем список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
        if len(my_pets['pets']) == 0:
            pf.add_new_pet_with_photo(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
            _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Берём id первого питомца из списка и отправляем запрос на удаление
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key, pet_id)

        # Ещё раз запрашиваем список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
        assert status == 200
        assert pet_id not in my_pets.values()

class TestCasesNegative:

    def test_unsuccessful_delete_pet_for_unauthorized_user_403(self, auth_key):
        """Проверяем невозможность удаления питомца неавторизованным юзером"""

        # Создаем питомца, запрашиваем список своих питомцев
        pf.add_new_pet_with_photo(auth_key, "Последний", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Берём id последнего питомца из списка и отправляем запрос на удаление неавторизованным пользователем
        pet_id = my_pets['pets'][-1]['id']
        auth_key = {"key": ""}
        status, result = pf.delete_pet(auth_key, pet_id)

        # Проверяем что статус ответа равен 403
        assert status == 403
        assert "Forbidden" in result