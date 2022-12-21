import time
import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
#
# def test_search_example(driver):
#     """ Search some phrase in google and make a screenshot of the page. """
#
#     # Open google search page:
#     driver.get('https://google.com')
#
#     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # Find the field for search text input:
#     search_input = driver.find_element(By.NAME, 'q')
#
#
#     # Enter the text for search:
#     search_input.clear()
#     search_input.send_keys('first test')
#
#     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # Click Search:
#     search_button = driver.find_element(By.NAME, 'btnK')
#     search_button.submit()
#
#     time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # Make the screenshot of browser window:
#     #driver.screen('result.png')
#     time.sleep(2)
#     driver.quit()
#
#
# import time
#
# def test_petfriends(web_browser):
#    # Open PetFriends base page:
#     web_browser.get("https://petfriends.skillfactory.ru/")
#
#     time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
#
#    # click on the new user button
#     btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
#     btn_newuser.click()
#
#    # click existing user button
#     btn_exist_acc = web_browser.find_element_by_link_text(u"У меня уже есть аккаунт")
#     btn_exist_acc.click()
#
#    # add email
#     field_email = web_browser.find_element_by_id("email")
#     field_email.clear()
#     field_email.send_keys("shumak@gmail.com")
#
#     #  add password
#     field_pass = web_browser.find_element_by_id("pass")
#     field_pass.clear()
#     field_pass.send_keys("94969496")
#
#     # click submit button
#     btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
#     btn_submit.click()
#
#     time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
#
#     assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"
#
# def test_show_my_pets():
#     # Вводим email
#     pytest.driver.find_element_by_id('email').send_keys('shumak@gmail.com')
#     # Вводим пароль
#     pytest.driver.find_element_by_id('pass').send_keys('94969496')
#     # Нажимаем на кнопку входа в аккаунт
#     pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
#     # Проверяем, что мы оказались на главной странице пользователя
#     assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
#
#     images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
#     names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
#     descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')
#
#     for i in range(len(names)):
#          assert images[i].get_attribute('src') != ''
#          assert names[i].text != ''
#          assert descriptions[i].text != ''
#          assert ', ' in descriptions[i]
#          parts = descriptions[i].text.split(", ")
#          assert len(parts[0]) > 0
#          assert len(parts[1]) > 0

