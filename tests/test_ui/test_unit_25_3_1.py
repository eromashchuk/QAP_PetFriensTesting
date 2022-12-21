import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_my_pets():
    # Entering an email and a password
    pytest.driver.find_element(By.ID, 'email').send_keys('shumak@gmail.com')
    pytest.driver.find_element(By.ID, 'pass').send_keys('94969496')
    # Press on submit button
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Check that we are on a main page
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Find a "my pets" link and click on it
    my_pets_button = pytest.driver.find_element(By.CSS_SELECTOR, "a[href='/my_pets']")
    my_pets_button.click()

    pytest.driver.implicitly_wait(10)

    # Find a total quantity of a pets cards and check its elements
    my_pets_qty = pytest.driver.find_element(By.XPATH, "//div[contains(@class,'.col-sm-4 left')]")
    total_qty = len(pytest.driver.find_elements(By.CSS_SELECTOR, "[scope='row']"))

    wait = WebDriverWait(pytest.driver, 10)

    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr th img")))
    names = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[1]")))
    breeds = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[2]")))
    ages = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[3]")))

    img = 0
    pets_names = []
    for i in range(total_qty):
        if images[i].get_attribute('src') != '':
            img += 1
        pets_names.append(names[i].text)  # The list of all pets names
        assert names[i].text != "" and names[i].text != " "  # Name field is not empty
        assert breeds[i].text != "" and names[i].text != " "  # Breed field is not empty
        assert ages[i].text != "" and ages[i].text != " "  # Age field is not empty
    assert img >= total_qty / 2  # Numbers of pets photo is at least half of total quantity(or more) of my pet`s cards
    assert str(total_qty) in my_pets_qty.text.split("\n")[1]  # Total quantity of card the same as in a counter
    assert pets_names.sort() == list(
        set(pets_names)).sort()  # Check that pets have a different names(so it enough to check that cards are not duplicated)
