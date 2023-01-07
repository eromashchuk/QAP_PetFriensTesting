from api import PetFriends
from conftest import *
from settings import *
from generators import *
import os
pf = PetFriends()

class TestCasesPositive:

    @pytest.mark.student
    def test_set_photo_on_pets_by_id(self, auth_key, pet_photo='images/cat1.jpg'):
        '''Check adding a photo to a pet from the list of my pets by its id'''

        # determine the path to the photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Request a list of own pets
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Check the list of my pets is empty, then add a new one without a photo and again request a list of my pets
        if len(my_pets['pets']) == 0:
            pf.create_pet_simple(auth_key, "Суперкот", "кот", "3")
            _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Select the id of the first pet from the list and send a request to add a photo
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)

class TestCaseNegative:

    @pytest.mark.skip(reason="Баг в продукте - <ссылка>")
    @pytest.mark.parametrize("pet_photo", ['images/5.doc', 'images/0.jpg'])
    def test_impossible_to_set_unsupported_format_file(self, auth_key, pet_photo):
        '''Check that impossible to add a photo of 0 bytes or doc file to my pet from the list by its id'''

        # determine the path to the photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Create a pet without photo
        pf.create_pet_simple(auth_key, "Суперкот", "кот", "3")

        # Get list of my pets
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        # Select the id of the first pet from the list and send a request to add a photo
        pet_id = my_pets['pets'][-1]['id']
        status, result = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)
        assert status == 400
        assert '500 Internal Server Error' not in result
        assert 'Bad Gateway' not in result

    @pytest.mark.xfail(reason="Баг в продукте - <ссылка>")
    def test_error_400_for_set_photo_on_not_existing_pet(self, auth_key, pet_photo='images/cat1.jpg'):
        '''Check that 400 error occurred when tried to add a photo to a non-existent pet'''

        # determine the path to the photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Try to add photo for unexciting pet_id
        pet_id = "0123456789456j"
        status, _ = pf.set_photo_by_pet_id(auth_key, pet_id, pet_photo)
        assert status == 400