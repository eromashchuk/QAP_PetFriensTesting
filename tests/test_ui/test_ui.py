# import time
#
#
# def test_search_example(selenium):
#     """ Search some phrase in google and make a screenshot of the page. """
#
#     # Open google search page:
#     selenium.get('https://google.com')
#
#     time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # Find the field for search text input:
#     search_input = selenium.find_element_by_name('q')
#
#
#     # Enter the text for search:
#     search_input.clear()
#     search_input.send_keys('first test')
#
#     time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # Click Search:
#     search_button = selenium.find_element_by_name('btnK')
#     search_button.click()
#
#     # time.sleep(1)  # just for demo purposes, do NOT repeat it on real projects!
#     #
#     # # Make the screenshot of browser window:
#     # selenium.save_screenshot('result.png')
#
#
#
# def test_petfriends(selenium):
#     # Open PetFriends base page:
#     selenium.get("https://petfriends.skillfactory.ru/")
#
#     time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # click on the new user button
#     btn_newuser = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
#
#     btn_newuser.click()
#
#     # click existing user button
#     btn_exist_acc = selenium.find_element_by_link_text(u"У меня уже есть аккаунт")
#     btn_exist_acc.click()
#
#     # add email
#     field_email = selenium.find_element_by_id("email")
#     field_email.clear()
#     field_email.send_keys("shumak@gmail.com")
#
#     # add password
#     field_pass = selenium.find_element_by_id("pass")
#     field_pass.clear()
#     field_pass.send_keys("94969496")
#
#     # click submit button
#     btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
#     btn_submit.click()
#
#     time.sleep(2)  # just for demo purposes, do NOT repeat it on real projects!
#     if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
#         # Make the screenshot of browser window:
#         selenium.save_screenshot('result_petfriends.png')
#     else:
#         raise Exception("login error")
