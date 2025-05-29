from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LocatorsMainPageUserAccount, Constructor

main_locators = LocatorsMainPageUserAccount()
constructor_locators = Constructor()


class TestConstructor:
    #1 Переход к разделу "Булки" в "Конструкторе"
    def test_transfer_using_broads_in_constructor(self, driver, sign_in_using_user_account):

        # Осуществляется вход в аккаунт через "Личный кабинет"

        wait = WebDriverWait(driver, 3)
        button_constructor = wait.until(expected_conditions.element_to_be_clickable(main_locators.button_constructor_in_user_account))
        button_constructor.click()  # Нажать "Конструктор"

        span_bread = wait.until(expected_conditions.element_to_be_clickable(constructor_locators.button_breads))

        try:
            span_bread.click() # Нажать "Булки"

        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", span_bread) # Нажать "Булки" второй раз

        # Найти активный элемент
        active_element = driver.find_element(*constructor_locators.active_tab)

        #Найти и вывести текст активного раздела
        active_tab_text = driver.find_element(*constructor_locators.active_tab).text

        # Проверка, что активный раздел называется 'Булки' и элемент отображается и активен
        assert active_tab_text == 'Булки' and active_element.is_displayed() and active_element.is_enabled()


    #2 Переход к разделу "Соусы" в "Конструкторе"
    def test_transfer_using_sauces_in_constructor(self, driver, sign_in_using_user_account):

        # Осуществляется вход в аккаунт через "Личный кабинет"

        wait = WebDriverWait(driver, 3)
        button_constructor = wait.until(expected_conditions.element_to_be_clickable(main_locators.button_constructor_in_user_account))
        button_constructor.click()  # Нажать "Конструктор"

        span_sauces = wait.until(expected_conditions.element_to_be_clickable(constructor_locators.button_sauces))

        try:
            span_sauces.click()  # Нажать "Соусы"

        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", span_sauces)  # Нажать "Соусы" второй раз

        # Найти активный элемент
        active_element = driver.find_element(*constructor_locators.active_tab)

        #Найти и вывести текст активного раздела
        active_tab_text =  driver.find_element(*constructor_locators.active_tab).text

        # Проверка, что активный раздел называется 'Соусы' и элемент отображается и активен
        assert active_tab_text == 'Соусы' and active_element.is_displayed() and active_element.is_enabled()


    #3 Переход к разделу "Начинки" в "Конструкторе"
    def test_transfer_using_fillings_in_constructor(self, driver):

        # Осуществляется вход в аккаунт через "Личный кабинет"

        wait = WebDriverWait(driver, 3)
        button_constructor = wait.until(expected_conditions.element_to_be_clickable(main_locators.button_constructor_in_user_account))
        button_constructor.click()  # Нажать "Конструктор"

        span_fillings = wait.until(expected_conditions.element_to_be_clickable(constructor_locators.button_fillings))

        try:
            span_fillings.click()  # Нажать "Начинки"

        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", span_fillings)  # Нажать "Начинки" второй раз

        # Найти активный элемент
        active_element = driver.find_element(*constructor_locators.active_tab)

        # Найти и вывести текст активного раздела
        active_tab_text =  driver.find_element(*constructor_locators.active_tab).text

        # Проверка, что активный раздел называется 'Начинки' и элемент отображается и активен
        assert active_tab_text == 'Начинки' and active_element.is_displayed() and active_element.is_enabled()
