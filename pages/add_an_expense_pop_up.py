from selenium.webdriver.common.by import By
import time
from random import randrange
from pages.base_page import BasePage
class AddAnExpense(BasePage):

    def __init__(self, driver, mileage):
        BasePage.__init__(self, driver)
        self.mileage = mileage + 100
    def add_an_expense_form(self):
        expense_liters = randrange(9999)
        expense_total_cost = randrange(1000000)
        self._driver.find_element(By.XPATH, '//*[@id="addExpenseCar"]').send_keys("Audi")
        self._driver.find_element(By.XPATH, '//*[@id="addExpenseDate"]').clear()
        self._driver.find_element(By.XPATH, '//*[@id="addExpenseDate"]').send_keys("24.12.2023")
        self._driver.find_element(By.XPATH, '//*[@id="addExpenseMileage"]').clear()
        self._driver.find_element(By.XPATH, '//*[@id="addExpenseMileage"]').send_keys(self.mileage)
        self._driver.find_element(By.XPATH, '//*[@id="addExpenseLiters"]').send_keys(expense_liters)
        self._driver.find_element(By.XPATH, '//*[@id="addExpenseTotalCost"]').send_keys(expense_total_cost)
    def add_expense_button(self):
        self._driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]').click()
        time.sleep(5)