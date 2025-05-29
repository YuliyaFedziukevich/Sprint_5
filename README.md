* **Файлы с тестами**
* 1 Файл **test_registration.py** содержит тесты на регистрацию: 
* - успешная регистрация (test_successful_registration), 
* - негативные тесты на:
* -- пустые поля (test_failed_registration_by_invalid_email), 
* --заполнения поля Email данными не в заданном формате (test_failed_registration_by_invalid_email), 
* --минимальную длину пароля (test_failed_registration_by_invalid_password), 
* --ошибку для некорректного пароля (test_failed_registration_by_invalid_password)
* 2 Файл **test_sign_in_out.py** содержит тесты на проверку успешного выхода и входа через:
* - кнопку "Войти в аккаунт" (test_success_sign_into_account),
* - кнопку "Личный кабинет" (test_success_sign_into_user_account),
* - в форме регистрации (test_success_sign_into_registration_form),
* - кнопку в форме восстановления пароля (test_success_sign_into_password_recovery),
* - успешный выход из аккаунта (test_success_sign_out)
* 3 Файл **test_transfer.py** содержит тесты на проверку успешного перехода:
* - в "Личный кабинет" (test_transfer_using_user_account),
* - из "Личного кабинета" в конструктор по клику на «Конструктор» (test_transfer_to_constructor_using_user_account),
* - из "Личного кабинета" в конструктор по клику на на логотип Stellar Burgers (test_transfer_to_constructor_using_logo_in_user_account)
* 4 Файл **test_constructor.py** содержит тесты на проверку работоспособности переходов в разделе "Конструктор" к разделам:
* - "Булки" (test_transfer_using_broads_in_constructor), 
* - "Соусы" (test_transfer_using_sauces_in_constructor), 
* - "Начинки" (test_transfer_using_fillings_in_constructor)

* **Вспомогательные файлы**
* 1 В файле **conftest.py** - используемые фикстуры 
* 2 В файле **data_generator.py** - функции для рандомного генерирования данных (имя, email, пароль)
* 3 В файле **locators.py** - перечень используемых локаторов
* 4 В файле **sign_in_page.py** - функция для входа в систему с существующими логином и паролем (во избежание необходимости излишней регистрации при проверках, где предусловием или необходимым условием является вход в аккаунт)
* 5 В файле **test_data.py** - размещены существующие имя, логин и пароль для входа в аккаунт
* 6 В файле **url.py**  - размещены url