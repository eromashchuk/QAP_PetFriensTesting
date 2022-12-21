import os
from api import PetFriends
from conftest import *
from settings import *
from generators import *

pf = PetFriends()

class TestCasesPositive:

    def test_add_new_pet_with_valid_data(self, auth_key, name='Барбоскин', animal_type='двортерьер',
                                         age='4', pet_photo='images/cat1.jpg'):
        """Проверяем что можно добавить питомца с корректными данными с фото"""

        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Добавляем питомца
        status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name

class TestCasesNegative:

    @pytest.mark.skip(reason="Баг в продукте - <ссылка>")
    def test_impossible_to_set_a_doc_file(self, auth_key, pet_photo='images/5.doc'):
        '''Проверка невозможности добавить фото размером 0 байт питомцу из списка моих питомцев по его id'''

        # определяем путь к фото
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Создаем питомца без фото
        pf.create_pet_simple(auth_key, "Суперкот", "кот", "3")

        # Запрашиваем список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Берём id последнего питомца из списка и отправляем запрос на добавление фото
        pet_id = my_pets['pets'][-1]['id']
        status, result = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)
        assert status == 400
        assert '500 Internal Server Error' not in result
        assert 'Bad Gateway' not in result

    @pytest.mark.xfail(reason="Баг в продукте - <ссылка>")
    def test_required_fields_for_adding_new_pet(self, auth_key, name='', animal_type='',
                                                age='', pet_photo='images/cat1.jpg'):
        """Проверяем, что нельзя добавить питомца без заполнения обязательных полей"""

        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Добавляем питомца
        status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 400
        assert 'error' in result
