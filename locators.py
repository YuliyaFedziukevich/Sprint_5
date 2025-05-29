from selenium.webdriver.common.by import By

# Локаторы главной страницы и "Личного кабинета"
class LocatorsMainPageUserAccount:

    # Кнопка "Личный кабинет"
    user_account = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Кнопка "Войти в аккаунт" на главной странице
    button_sign_in_to_account = (By.XPATH, '//main//button[text()="Войти в аккаунт"]')

    # Кнопка "Оформить заказ" на главной странице
    button_place_an_order = (By.XPATH, '//main//button[text()="Оформить заказ"]')

    # Кнопка "Конструктор"
    button_constructor_in_user_account = (By.XPATH, '//p[text()="Конструктор"]')

    # Логотип Stellar Burgers
    logo = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo")]')

    # Кнопка "Выйти" в "Личном кабинете"
    button_sign_out = (By.XPATH, '//main//button[text()="Выход"]')

# Локаторы раздела "Вход"
class LocatorsEntry:

    # Поле "Email" в разделе "Вход"
    sign_in_email = (By.NAME, 'name')

    # Поле "Пароль" в разделе "Вход"
    sign_in_password = (By.NAME, 'Пароль')

    # Кнопка "Вход"
    button_sign_in = (By.XPATH, '//form//button[text() ="Войти"]')

    # Кнопка "Зарегистрироваться" в разделе "Вход"
    registration = (By.CSS_SELECTOR, 'a[href="/register"]')

    # Кнопка "Восстановить пароль" в разделе "Вход"
    button_password_recovery = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')

# Локаторы раздела "Регистрация"
class LocatorsRegistration:

    # Поле "Имя" в разделе "Регистрация"
    registration_name = (By.XPATH, '//form//label[(text()="Имя")]/following-sibling::input')

    # Поле "Email" в разделе "Регистрация"
    registration_email = (By.XPATH, '//form//label[(text()="Email")]/following-sibling::input')

    # Поле "Пароль" в разделе "Регистрация"
    registration_password = (By.NAME, 'Пароль')

    # Кнопка "Зарегистрироваться" в разделе "Регистрация"
    button_registration = (By.XPATH, '//form//button[text() = "Зарегистрироваться"]')

    # Кнопка "Войти" в форме регистрации
    button_sign_in_registration = (By.CSS_SELECTOR, 'a[href="/login"]')

    # Ошибка "Некорректный пароль"
    password_error = (By.XPATH, '//form//p[text()="Некорректный пароль"]')

# Локаторы формы "Восстановление пароля"
class LocatorsPasswordRecovery:

    # Кнопка "Войти" в форме "Восстановление пароля"
    button_sign_in_password_recovery = (By.CSS_SELECTOR, 'a[href="/login"]')

# Локаторы "Конструктора"
class Constructor:

    # Кнопка "Булки" в "Конструкторе"
    button_breads = (By.XPATH, '//main//span[text()="Булки"]')

    # Атрибут активной вкладки
    active_tab = (By.XPATH, '//div[contains(@class, "tab_tab_type_current__2BEPc")]/span')

    # Кнопка "Соусы" в "Конструкторе"
    button_sauces = (By.XPATH, '//main//span[text()="Соусы"]')

    # Кнопка "Начинки" в "Конструкторе"
    button_fillings = (By.XPATH, '//main//span[text()="Начинки"]')
