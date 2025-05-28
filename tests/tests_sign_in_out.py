from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from url import main_URL, sign_in_URL
from locators import LocatorsMainPageUserAccount, LocatorsRegistration, LocatorsEntry, LocatorsPasswordRecovery
from sign_in_page import fill_sign_in_fields

main_locators = LocatorsMainPageUserAccount()
registration_locators = LocatorsRegistration()
entry_locators = LocatorsEntry()
recovery_password_locators = LocatorsPasswordRecovery()

class TestSignIn:

    #1 Проверка успешного входа через кнопку "Войти в аккаунт"
    def test_success_sign_into_account(self, driver):

        wait = WebDriverWait(driver, 3)

        sign_in_account = wait.until(expected_conditions.element_to_be_clickable(main_locators.button_sign_in_to_account))
        sign_in_account.click() # Нажать кнопку "Войти в аккаунт"

        fill_sign_in_fields(driver) # Заполнить поля формы "Вход" существующими данными, войти в аккаунт

        wait.until(expected_conditions.element_to_be_clickable(main_locators.button_place_an_order))
        button_order = driver.find_element(*main_locators.button_place_an_order) # Найти кнопку "Оформить заказ"

        # Проверка, что кнопка "Оформить заказ" отображается и активна
        assert driver.current_url == main_URL and button_order.is_displayed() and button_order.is_enabled()


    #2 Проверка успешного входа через кнопку "Личный кабинет"
    def test_success_sign_into_user_account(self, driver):

        wait = WebDriverWait(driver, 3)
        button_user_account = wait.until(expected_conditions.element_to_be_clickable(main_locators.user_account))
        button_user_account.click()  # Нажать "Личный кабинет"

        fill_sign_in_fields(driver) # Заполнить поля формы "Вход" существующими данными, войти в аккаунт

        wait.until(expected_conditions.element_to_be_clickable(main_locators.button_place_an_order))
        button_order = driver.find_element(*main_locators.button_place_an_order) # Найти кнопку "Оформить заказ"

        # Проверка, что кнопка "Оформить заказ" отображается и активна
        assert driver.current_url == main_URL and button_order.is_displayed() and button_order.is_enabled()


    #3 Проверка успешного входа через кнопку в форме регистрации
    def test_success_sign_into_registration_form(self, driver, registration_window):
        # Осуществлен переход в раздел "Регистрация"

        wait = WebDriverWait(driver, 3)
        sign_in = wait.until(expected_conditions.element_to_be_clickable(registration_locators.button_sign_in_registration))
        sign_in.click() # Нажать "Войти"

        fill_sign_in_fields(driver) # Заполнить поля формы "Вход" существующими данными, войти в аккаунт

        wait.until(expected_conditions.element_to_be_clickable(main_locators.button_place_an_order))
        button_order = driver.find_element(*main_locators.button_place_an_order) # Найти кнопку "Оформить заказ"

        # Проверка, что кнопка "Оформить заказ" отображается и активна
        assert driver.current_url == main_URL and button_order.is_displayed() and button_order.is_enabled()


    #4 Проверка успешного входа через кнопку в форме восстановления пароля
    def test_success_sign_into_password_recovery(self, driver):

        wait = WebDriverWait(driver, 3)
        button_user_account = wait.until(expected_conditions.element_to_be_clickable(main_locators.user_account))
        button_user_account.click()  # Нажать "Личный кабинет"

        password_recovery = wait.until(expected_conditions.element_to_be_clickable(entry_locators.button_password_recovery))
        password_recovery.click()  # Нажать "Восстановить пароль"

        sign_in_recovery = wait.until(expected_conditions.element_to_be_clickable(recovery_password_locators.button_sign_in_password_recovery))
        sign_in_recovery.click()  # Нажать кнопку "Войти" на форме "Восстановление пароля"

        fill_sign_in_fields(driver)  # Заполнить поля формы "Вход" существующими данными, войти в аккаунт

        wait.until(expected_conditions.element_to_be_clickable(main_locators.button_place_an_order))
        button_order = driver.find_element(*main_locators.button_place_an_order)# Найти кнопку "Оформить заказ"

        # Проверка, что кнопка "Оформить заказ" отображается и активна
        assert driver.current_url == main_URL and button_order.is_displayed() and button_order.is_enabled()


class TestSignOut:

    #5 Выход из аккаунта
    def test_success_sign_out(self, driver):

        wait = WebDriverWait(driver, 3)
        button_user_account = wait.until(expected_conditions.element_to_be_clickable(main_locators.user_account))
        button_user_account.click()  # Нажать "Личный кабинет"

        fill_sign_in_fields(driver) # Заполнить поля формы "Вход" существующими данными, войти в аккаунт
        button_user_account = wait.until(expected_conditions.element_to_be_clickable(main_locators.user_account))

        button_user_account.click()  # Нажать "Личный кабинет"

        sign_out = wait.until(expected_conditions.element_to_be_clickable(main_locators.button_sign_out))
        sign_out.click()  # Нажать кнопку "Выход"

        wait.until(expected_conditions.element_to_be_clickable(entry_locators.button_sign_in))

        # Проверка, что осуществлен переход на страницу "Входа"
        assert driver.current_url == sign_in_URL

