import pytest
import requests
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from settings import *


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест шел: {end_time - start_time}")


@pytest.fixture(autouse=True)
def auth_key():
    res = requests.get('https://petfriends.skillfactory.ru/api/key',
                       headers={'email': valid_email, 'password': valid_password})
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return result

# @pytest.fixture
# def firefox_options(firefox_options):
#     firefox_options.binary = 'C:/geckodriver/geckodriver.exe'  # путь к exe-драйверу Firefox.
#     firefox_options.add_argument('-foreground') # возможность запуска в фоновом или реальном режиме. В нашем случае выбран последний.
#                                                 # Для фонового укажите ‘-background’.
#     firefox_options.set_preference('browser.anchor_color', '#FF0000') #выбор цвета подложки браузера.
#     return firefox_options

# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.binary_location = 'C:/chromedriver/chromedriver.exe' #путь к exe браузера (включая сам исполняемый файл).
#     # chrome_options.add_extension('/path/to/extension.crx') #включение дополнений браузера.
#     # chrome_options.add_argument('--kiosk') #можно задавать другие параметры запуска браузера из списка https://peter.sh/experiments/chromium-command-line-switches/.
#     return chrome_options

# @pytest.fixture
# def driver_args():
#     return ['--log-level=LEVEL']
#
# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.set_headless(True) #запуск без UI
#     return chrome_options

#content of file conftest.py

import uuid


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # This function helps to detect that some test failed
#     # and pass this information to teardown:
#
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep

# @pytest.fixture
# def web_browser(request, selenium):
#
#     browser = selenium
#     browser.set_window_size(1400, 1000)
#
#     # Return browser instance to test case:
#     yield browser
#
#     # Do teardown (this code will be executed after each test):
#
#     if request.node.rep_call.failed:
#         # Make the screen-shot if test failed:
#         try:
#             browser.execute_script("document.body.bgColor = 'white';")
#
#             # Make screen-shot for local debug:
#             browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
#
#             # For happy debugging:
#             print('URL: ', browser.current_url)
#             print('Browser logs:')
#             for log in browser.get_log('browser'):
#                 print(log)
#
#         except:
#             pass # just ignore any errors here

# @pytest.fixture(autouse=True)
# def testing():
#     pytest.driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
#     # Переходим на страницу авторизации
#     pytest.driver.get('http://petfriends.skillfactory.ru/login')
#
#     yield
#
#     pytest.driver.quit()
