from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SignInPopUp(BasePage):
    def click_registration_button(self):
        # time.sleep(10)
        self._driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[1]").click()