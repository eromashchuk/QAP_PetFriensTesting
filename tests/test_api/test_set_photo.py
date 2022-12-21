from api import PetFriends
from conftest import *
from settings import *
from generators import *
import os
pf = PetFriends()

class TestCasesPositive:

    @pytest.mark.student
    def test_set_photo_on_pets_by_id(self, auth_key, pet_photo='images/cat1.jpg'):
        '''Проверка возможности добавить фото питомцу из списка моих питомцев по его id'''

        # определяем путь к фото
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Запрашиваем список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Проверяем - если список своих питомцев пустой, то добавляем нового без фото и опять запрашиваем список своих питомцев
        if len(my_pets['pets']) == 0:
            pf.create_pet_simple(auth_key, "Суперкот", "кот", "3")
            _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Берём id первого питомца из списка и отправляем запрос на добавление фото
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)

class TestCaseNegative:

    @pytest.mark.xfail(reason="Баг в продукте - <ссылка>")
    def test_error_400_for_set_photo_on_not_existing_pet(self, auth_key, pet_photo='images/cat1.jpg'):
        '''Проверка возниконовения 400 ошибки при попытке добавить фото несуществующему питомцу'''

        # определяем путь к фото
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Берём несуществующий id питомца из и отправляем запрос на добавление фото
        pet_id = "0123456789456j"
        status, _ = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)
        assert status == 400