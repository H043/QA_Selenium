import time

from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.garage_page import GaragePage
from pages.sign_in_pop_up import SignInPopUp
from pages.registration_page import createNewUser
from pages.add_a_car_pop_up import AddACar
from pages.settings_page import SettingsPage
from pages.add_an_expense_pop_up import AddAnExpense
def test_open_QAuto_page_and_click_sign_in_button(browser):
    browser.get("https://guest:welcome2qauto@qauto.forstudy.space/")
    home_page = HomePage(browser)
    home_page.click_sign_in_button()
    sign_in_pop_up = SignInPopUp(browser)
    sign_in_pop_up.click_registration_button()
    registration_pop_up = createNewUser(browser)
    registration_pop_up.new_user_registration()
    registration_pop_up.click_register_button()
    home_page.open_profile_button()
    time.sleep(3)
    user_name_element = browser.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-profile/div/div[2]/div/p")
    assert user_name_element.text == registration_pop_up.user_name + " " + registration_pop_up.user_last_name
    home_page.open_garage_page()
    garage_page = GaragePage(browser)
    garage_page.add_car_button()
    add_a_car = AddACar(browser)
    add_a_car.add_init_mileage()
    add_a_car.add_button()
    time.sleep(5)
    garage_page.add_expense_button()
    add_an_expense = AddAnExpense(browser, add_a_car.mileage)
    add_an_expense.add_an_expense_form()
    add_an_expense.add_expense_button()
    home_page.settings_button()
    settings_page = SettingsPage(browser)
    settings_page.remove_my_account_button()
    settings_page.remove_button()


