from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class HomePage(BasePage):
    def click_sign_in_button(self):
        self._driver.find_element(By.XPATH, "//header//button[text()='Sign In']").click()
    def open_garage_page(self):
        self._driver.find_element(By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[1]').click()
    def settings_button(self):
        self._driver.find_element(By.XPATH,'/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[2]').click()
    def open_profile_button(self):
        self._driver.find_element(By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[1]').click()
