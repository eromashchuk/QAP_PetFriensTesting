import pytest

from api import PetFriends
from settings import valid_email, valid_password, invalid_password, invalid_email
import os

pf = PetFriends()

class TestCasesPositive:

    def test_get_api_key_for_valid_user(self, email=valid_email, passwrd=valid_password):
        """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.get_api_key(email, passwrd)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 200
        assert 'key' in result

    def test_get_all_pets_with_valid_key(self, filter=''):
        """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой.
        Доступное значение параметра filter - 'my_pets' либо '' """

        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.get_list_of_pets(auth_key, filter)

        assert status == 200
        assert len(result['pets']) > 0

    def test_add_new_pet_with_valid_data(self, name='Барбоскин', animal_type='двортерьер',
                                         age='4', pet_photo='images/cat1.jpg'):
        """Проверяем что можно добавить питомца с корректными данными с фото"""

        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Запрашиваем ключ api и сохраняем в переменую auth_key
        _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Добавляем питомца
        status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name

    @pytest.mark.student
    def test_successful_create_pet_simple(self, name='Myrchik', animal_type='Sckotina',
                                          age='2'):
        """Проверяем что можно добавить питомца с корректными данными без фото"""
        # Запрашиваем ключ api и сохраняем в переменую auth_key
        _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Добавляем питомца
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert 'id' in result
        assert result['name'] == name
        assert result['age'] == age
        assert result['animal_type'] == animal_type

    @pytest.mark.student
    def test_set_photo_on_pets_by_id(self, pet_photo='images/cat1.jpg'):
        '''Проверка возможности добавить фото питомцу из списка моих питомцев по его id'''

        # определяем путь к фото
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Получаем ключ auth_key и запрашиваем список своих питомцев
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Проверяем - если список своих питомцев пустой, то добавляем нового без фото и опять запрашиваем список своих питомцев
        if len(my_pets['pets']) == 0:
            pf.create_pet_simple(auth_key, "Суперкот", "кот", "3")
            _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Берём id первого питомца из списка и отправляем запрос на добавление фото
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)

    def test_successful_delete_self_pet(self):
        """Проверяем возможность удаления питомца"""

        # Получаем ключ auth_key и запрашиваем список своих питомцев
        _, auth_key = pf.get_api_key(valid_email, valid_password)
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

    def test_successful_update_self_pet_info(self, name='Мурзик', animal_type='Котэ', age=5):
        """Проверяем возможность обновления информации о питомце"""

        # Получаем ключ auth_key и список своих питомцев
        _, auth_key = pf.get_api_key(valid_email, valid_password)
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

@pytest.mark.student
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

    def test_no_pets_shown_for_unauthorized_user(self, filter=''):
        """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой.
        Доступное значение параметра filter - 'my_pets' либо '' """

        auth_key = {'key': ''}
        status, result = pf.get_list_of_pets(auth_key, filter)

        assert status == 403
        assert 'pets' not in result

    @pytest.mark.skip(reason="Баг в продукте - <ссылка>")
    def test_impossible_to_set_a_doc_file(self, pet_photo='images/5.doc'):
        '''Проверка невозможности добавить фото размером 0 байт питомцу из списка моих питомцев по его id'''

        # определяем путь к фото
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Получаем ключ auth_key и создаем питомца без фото
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        pf.create_pet_simple(auth_key, "Суперкот", "кот", "3")

        # Запрашиваем список своих питомцев
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Берём id последнего питомца из списка и отправляем запрос на добавление фото
        pet_id = my_pets['pets'][-1]['id']
        status, result = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)
        assert status == 400
        assert '500 Internal Server Error' not in result
        assert 'Bad Gateway' not in result

    @pytest.mark.skip(reason="Баг в продукте - <ссылка>")
    def test_required_fields_for_adding_new_pet(self, name='', animal_type='',
                                         age='', pet_photo='images/cat1.jpg'):
        """Проверяем, что нельзя добавить питомца без заполнения обязательных полей"""

        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Запрашиваем ключ api и сохраняем в переменую auth_key
        _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Добавляем питомца
        status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 400
        assert 'error' in result

    def test_unsuccessful_delete_pet_for_unauthorized_user_403(self):
        """Проверяем невозможность удаления питомца неавторизованным юзером"""

        # Получаем ключ auth_key и создаем питомца, запрашиваем список своих питомцев
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        pf.add_new_pet_with_photo(auth_key, "Последний", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Берём id последнего питомца из списка и отправляем запрос на удаление неавторизованным пользователем
        pet_id = my_pets['pets'][-1]['id']
        auth_key = {"key": ""}
        status, result = pf.delete_pet(auth_key, pet_id)

        # Проверяем что статус ответа равен 403
        assert status == 403
        assert "Forbidden" in result

    def test_error_400_for_updating_not_existing_pet(self, pet_id="0123456123456j", name='', animal_type='', age=''):
        """Проверяем, что нельзя заменить данные несуществующего питомца"""

        # Получаем ключ auth_key и пробуем обновить имя, тип и возраст несуществующего питомца
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)

        # Проверяем что статус ответа = 400
        assert status == 400

    @pytest.mark.skip(reason="Баг в продукте - <ссылка>")
    def test_error_400_for_set_photo_on_not_existing_pet(self, pet_photo='images/cat1.jpg'):
        '''Проверка возниконовения 400 ошибки при попытке добавить фото несуществующему питомцу'''

        # определяем путь к фото
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Получаем ключ auth_key
        _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Берём несуществующий id питомца из и отправляем запрос на добавление фото
        pet_id = "0123456789456j"
        status, _ = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)
        assert status == 400

