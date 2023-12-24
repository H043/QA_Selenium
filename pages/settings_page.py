import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SettingsPage(BasePage):
    def remove_my_account_button(self):
        self._driver.find_element(By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[5]/div/button').click()

    def remove_button(self):
        self._driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-remove-account-modal/div[3]/button[2]').click()
        time.sleep(5)
