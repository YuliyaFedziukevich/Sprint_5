import random
import string

class DataGenerator:
    @staticmethod
    def random_string(characters, length):
        return ''.join(random.choice(characters) for _ in range(length))

    # Создание случайного валидного имени
    @staticmethod
    def generate_random_name(min_len = 3, max_len = 10):
        length = random.randint(min_len, max_len)
        characters = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
        name_valid = DataGenerator.random_string(characters, length)
        return name_valid.capitalize()

    # Создание случайного валидного email
    @staticmethod
    def generate_random_email():
        random_str = DataGenerator.random_string(string.digits, 3)
        domains = ['test.ru', 'example.com', 'ya.ru', 'gmail.com']
        domain = random.choice(domains)
        email_valid = f'Yuliya_Fedziukevich_23_{random_str}@{domain}'
        return email_valid

    # Создание случайного валидного пароля
    @staticmethod
    def generate_random_password(min_len = 6, max_len = 11):
        length = random.randint(min_len, max_len)
        allowed_chars = '!#$*%&'
        characters = string.ascii_letters + string.digits + allowed_chars
        password_valid = DataGenerator.random_string(characters, length)
        return password_valid

