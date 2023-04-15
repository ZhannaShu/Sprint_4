from faker import Faker
from faker.generator import random
class UserData:
    fake = Faker("ru_RU")
    a = random.randint(920, 999)
    b = random.randint(1000000, 9999999)

    firstname_male = fake.first_name_male()
    surname_male = fake.last_name_male()
    address_male = 'Москва, улица Кибальчича,1'
    station_male = 'ВДНХ'
    phone_male = f'7{a}{b}'
    date_male = '15.04.2023'
    indx_male = 6
    color_male = 'grey'
    comment_male = 'Какой то коммент'

    firstname_female = fake.first_name_female()
    surname_female = fake.last_name_female()
    address_female = 'Москва, проспект Мира, 76с2'
    station_female = 'Рижская'
    phone_female = f'7{a}{b}'
    date_female = '15.04.2023'
    indx_female = 4
    color_female = 'black'
    comment_female = 'Какой то коммент'