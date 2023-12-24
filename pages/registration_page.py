from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import string
import random
def id_generator(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size)) + "@gmail.com"
class createNewUser(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.user_name = "NewName"
        self.user_last_name = "NewLastName"
    def new_user_registration(self):
        self._driver.find_element(By.XPATH, "//*[@id='signupName']").send_keys(self.user_name)
        self._driver.find_element(By.XPATH, "//*[@id='signupLastName']").send_keys(self.user_last_name)
        self._driver.find_element(By.XPATH, "//*[@id='signupEmail']").send_keys(id_generator())
        self._driver.find_element(By.XPATH, "//*[@id='signupPassword']").send_keys("Qwerty123")
        self._driver.find_element(By.XPATH, "//*[@id='signupRepeatPassword']").send_keys("Qwerty123")
    def click_register_button(self):
        self._driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button").click()
        time.sleep(3)








