import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from random import randrange

class AddACar(BasePage):

    def add_init_mileage(self):
        self.mileage = randrange(100000)
        self._driver.find_element(By.XPATH, "//*[@id='addCarMileage']").send_keys(self.mileage)
    def add_button(self):
        self._driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]').click()

                                # random car selection function
    # def add_a_car_brand(self):
    #     select_brand = Select(self._driver.find_element(By.ID, 'addCarBrand'))
    #     select_brand.select_by_value('2')
    #
    # def add_a_car_model(self):
    #     select_model = Select(self._driver.find_element(By.ID, 'addCarModel'))
    #     select_model.select_by_value('6')
