from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LocatorsEntry
from test_data import UserData

#1 Функция заполнения полей раздела "Вход" существующими данными
def fill_sign_in_fields(driver):
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LocatorsEntry.button_sign_in))
    driver.find_element(*LocatorsEntry.sign_in_email).send_keys(UserData.user_email)
    driver.find_element(*LocatorsEntry.sign_in_password).send_keys(UserData.user_password)
    driver.find_element(*LocatorsEntry.button_sign_in).click()
