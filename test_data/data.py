from faker import Faker

name = 'Яна'
email = "yana_kormshchikova_11666@yandex.ru"
password = 'Practicum11'

fake = Faker()
fake_email = fake.email()
fake_password = fake.password()
print(fake_email, fake_password)