import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from url import main_URL
from sign_in_page import fill_sign_in_fields
from data_generator import DataGenerator
from locators import LocatorsMainPageUserAccount, LocatorsEntry

main_locators = LocatorsMainPageUserAccount()
entry_locators = LocatorsEntry()


# Открытие, закрытие браузера
@pytest.fixture(scope='function')
def driver():

    driver = webdriver.Chrome()
    driver.get(main_URL)
    driver.maximize_window()

    yield driver

    driver.quit()


# Генерирование валидных данных для регистрации пользователя
@pytest.fixture(scope='function')
def random_valid_user():

    name_valid = DataGenerator.generate_random_name()
    email_valid = DataGenerator.generate_random_email()
    password_valid = DataGenerator.generate_random_password()

    return {
        "name_valid": name_valid,
        "email_valid": email_valid,
        "password_valid": password_valid
    }


# Вход в аккаунт с существующими данными
@pytest.fixture(scope='function')
def sign_in_using_user_account(driver):

    driver.get(main_URL)
    driver.maximize_window()

    wait = WebDriverWait(driver, 3)
    button_user_account = wait.until(expected_conditions.element_to_be_clickable(main_locators.user_account))
    button_user_account.click() # Нажать "Личный кабинет"

    fill_sign_in_fields(driver)  # Заполнить поля формы "Вход" существующими данными, войти в аккаунт

    return driver


# Переход в раздел "Регистрация"
@pytest.fixture(scope='function')
def registration_window(driver):

    driver.get(main_URL)
    driver.maximize_window()

    wait = WebDriverWait(driver, 3)
    button_user_account = wait.until(expected_conditions.element_to_be_clickable(main_locators.user_account))
    button_user_account.click() # Нажать "Личный кабинет"

    button_registration_user_account = wait.until(expected_conditions.element_to_be_clickable(entry_locators.registration))
    button_registration_user_account.click() # Нажать "Зарегистрироваться"

    return driver

