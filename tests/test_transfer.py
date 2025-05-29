from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from url import sign_in_URL, main_URL
from locators import LocatorsMainPageUserAccount

main_locators = LocatorsMainPageUserAccount()

class TestTransfer:

    #1 Переход по клику на "Личный кабинет"
    def test_transfer_using_user_account(self, driver, sign_in_using_user_account):

        # Осуществляется вход в аккаунт через "Личный кабинет"

        wait = WebDriverWait(driver, 3)
        wait.until(expected_conditions.element_to_be_clickable(main_locators.button_place_an_order))
        button_order = driver.find_element(*main_locators.button_place_an_order)  # Найти кнопку "Оформить заказ"

        # Проверка, что осуществлен переход на страницу конструктора и кнопка "Оформить заказ" отображается и активна
        assert driver.current_url == main_URL and button_order.is_displayed() and button_order.is_enabled()

    #2 Переход по клику на «Конструктор» в "Личном кабинете"
    def test_transfer_to_constructor_using_user_account(self, driver, sign_in_using_user_account):

        # Осуществляется вход в аккаунт через "Личный кабинет"

        wait = WebDriverWait(driver, 3)
        constructor_in_user_account = wait.until(expected_conditions.element_to_be_clickable(main_locators.button_constructor_in_user_account))
        constructor_in_user_account.click()  # Нажать "Конструктор" в "Личном кабинете"

        wait.until(expected_conditions.element_to_be_clickable(main_locators.button_place_an_order))
        button_order = driver.find_element(*main_locators.button_place_an_order)  # Найти кнопку "Оформить заказ"

        # Проверка, что осуществлен переход на страницу конструктора и кнопка "Оформить заказ" отображается и активна
        assert driver.current_url == main_URL and button_order.is_displayed() and button_order.is_enabled()


    #3 Переход по клику на логотип Stellar Burgers в "Личном кабинете"
    def test_transfer_to_constructor_using_logo_in_user_account(self, driver, sign_in_using_user_account):

        # Осуществляется вход в аккаунт через "Личный кабинет"

        wait = WebDriverWait(driver, 3)
        button_logo = wait.until(expected_conditions.element_to_be_clickable(main_locators.logo))
        button_logo.click()  # Нажать логотип Stellar Burgers в "Личном кабинете"

        wait.until(expected_conditions.element_to_be_clickable(main_locators.button_place_an_order))
        button_order = driver.find_element(*main_locators.button_place_an_order)  # Найти кнопку "Оформить заказ"

        # Проверка, что осуществлен переход на страницу конструктора и кнопка "Оформить заказ" отображается и активна
        assert driver.current_url == main_URL and button_order.is_displayed() and button_order.is_enabled()
