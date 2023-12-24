from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
class GaragePage(BasePage):
    def my_profile(self):
        self._driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[1]").click()
    def add_car_button(self):
        self._driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button").click()
    def add_expense_button(self):
        self._driver.find_element(By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]').click()
        time.sleep(5)
    def open_profile_button(self):
        self._driver.find_element(By.XPATH,"/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[1]").click()

