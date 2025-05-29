import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LocatorsMainPageUserAccount, LocatorsEntry, LocatorsRegistration
from data_generator import DataGenerator
from test_data import UserData
from url import sign_in_URL, registration_URL

main_locators = LocatorsMainPageUserAccount()
entry_locators = LocatorsEntry()
registration_locators = LocatorsRegistration()
data_generator = DataGenerator()
user_data = UserData()

class TestRegistration:
    #1 Успешная регистрация
    def test_successful_registration(self, driver, registration_window, random_valid_user):

        user_name = random_valid_user['name_valid']
        user_email = random_valid_user['email_valid']
        user_password = random_valid_user['password_valid']

        # Осуществлен переход в раздел "Регистрация"

        driver.find_element(*registration_locators.registration_name).send_keys(user_name) # Ввести валидное имя
        driver.find_element(*registration_locators.registration_email).send_keys(user_email) # Ввести валидный email
        driver.find_element(*registration_locators.registration_password).send_keys(user_password) # Ввести валидный пароль
        driver.find_element(*registration_locators.button_registration).click() # Нажать кнопку "Зарегистрироваться"

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(entry_locators.button_sign_in))

        # Проверка, что регистрация прошла успешно и осуществлен переход на страницу "Входа"
        assert driver.current_url == sign_in_URL


    #2 Негативный тест при невалидных Имени или Email и валидном пароле
    @pytest.mark.parametrize(
        'name, email, password',
        [
            # пустое поле "Имя" при валидных Email и пароле
            ('', data_generator.generate_random_email(), data_generator.generate_random_password()),
            # пустое поле "Email" при валидных имени и пароле
            (data_generator.generate_random_name(), '', data_generator.generate_random_password()),
            # невалидное поле "Email" при валидных имени и пароле (без @)
            (data_generator.generate_random_name(), 'login*test.com', data_generator.generate_random_password()),
            # невалидное поле "Email" при валидных имени и пароле (без логина)
            (data_generator.generate_random_name(), '@test.com', data_generator.generate_random_password()),
            # невалидное поле "Email" при валидных имени и пароле (без домена)
            (data_generator.generate_random_name(), 'login@', data_generator.generate_random_password()),
            # пустое поле "Пароль" при валидных имени и Email
            (data_generator.generate_random_name(), data_generator.generate_random_email(), '')
        ])
    def test_failed_registration_by_invalid_email(self, driver, registration_window, name, email, password):

        # Осуществлен переход в раздел "Регистрация"

        driver.find_element(*registration_locators.registration_name).send_keys(name) # Ввести имя
        driver.find_element(*registration_locators.registration_email).send_keys(email)  # Ввести email
        driver.find_element(*registration_locators.registration_password).send_keys(password)  # Ввести пароль
        driver.find_element(*registration_locators.button_registration).click()  # Нажать кнопку "Зарегистрироваться"

        # Проверка, что регистрация не произошла и переход на иную страницу не осуществлен
        assert driver.current_url == registration_URL


    #3 Ошибка при некорректном пароле
    @pytest.mark.parametrize('invalid_password', ['1', 'abcde']) # Проверяется минимальное и граничное количество символов, недопустимых в поле "Пароль"
    def test_failed_registration_by_invalid_password(self, driver, registration_window, invalid_password):

        # Осуществлен переход в раздел "Регистрация"

        driver.find_element(*registration_locators.registration_name).send_keys(user_data.user_name) # Ввести валидное имя
        driver.find_element(*registration_locators.registration_email).send_keys(user_data.user_email) # Ввести валидный email
        driver.find_element(*registration_locators.registration_password).send_keys(invalid_password) # Ввести невалидный пароль
        driver.find_element(*registration_locators.button_registration).click() # Нажать кнопку "Зарегистрироваться"

        # Ожидание возникновения ошибки и одновременная проверка на соответствие текста ошибки
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(registration_locators.password_error))

        # Проверка, что регистрация не произошла и переход на иную страницу не осуществлен
        assert driver.current_url == registration_URL
