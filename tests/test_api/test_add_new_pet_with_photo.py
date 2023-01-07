import os
from api import PetFriends
from conftest import *
from settings import *
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
        , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    @pytest.mark.parametrize("age", ['1'], ids=['min'])
    def test_add_new_pet_with_valid_data(self, auth_key, name, animal_type,
                                         age, pet_photo='images/cat1.jpg'):
        """Проверяем что можно добавить питомца с корректными данными с фото"""

        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Добавляем питомца
        status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name

class TestCasesNegative:



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
