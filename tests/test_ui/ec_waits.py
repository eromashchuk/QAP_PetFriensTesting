from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox()
# driver.get("http://somedomain/url_that_delays_loading")
# element = WebDriverWait(driver, 10).until(
# EC.presence_of_element_located((By.ID, "myDynamicElement"))
# )

class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False

wait = WebDriverWait(driver, 10)
element = wait.until(element_has_css_class((By.ID, 'checklistItem'), "greenChecklistItem"))

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")