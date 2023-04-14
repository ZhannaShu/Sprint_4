from selenium.webdriver.support import expected_conditions as EC
import allure
from faker import Faker
from faker.generator import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators.scooter_order_locators import LocatorOrder, SecondPage, ModalWindow, Logo
from .base_page import BasePage

class UserData:
    fake = Faker("ru_RU")
    a = random.randint(920, 999)
    b = random.randint(1000000, 9999999)

    # генерация муж. first name, surname, address, phone
    firstname_male = fake.first_name_male()
    surname_male = fake.last_name_male()
    address_male = 'Москва, улица Кибальчича,1'
    station_male = 'ВДНХ'
    phone_male = f'7{a}{b}'
    date_male = '15.04.2023'
    indx_male = 6
    color_male = 'grey'
    comment_male = 'Какой то коммент'

    # генерация жен. first name, surname, address, phone
    firstname_female = fake.first_name_female()
    surname_female = fake.last_name_female()
    address_female = 'Москва, проспект Мира, 76с2'
    station_female = 'Рижская'
    phone_female = f'7{a}{b}'
    date_female = '15.04.2023'
    indx_female = 4
    color_female = 'black'
    comment_female = 'Какой то коммент'

class ScooterOrderPage(BasePage):
    @allure.step('Заполняем первую форму Для кого самокат')
    def fill_out_the_form_for_whom_the_scooter(self, name, surname, addres, station, phone):
        self.driver.find_element(*LocatorOrder.NAME).send_keys(name)
        self.driver.find_element(*LocatorOrder.SURNAME).send_keys(surname)
        self.driver.find_element(*LocatorOrder.ADDRES).send_keys(addres)
        self.driver.find_element(*LocatorOrder.STATION).click()
        self.driver.find_element(*LocatorOrder.STATION).send_keys(station)
        self.driver.find_element(*LocatorOrder.CLICK_STATION).click()
        self.driver.find_element(*LocatorOrder.PHONE).send_keys(phone)

    @allure.step('Заполняем вторую форму заказа Про аренду')
    def fill_out_the_rental_form(self, date, index, color, comment):
        self.driver.find_element(*SecondPage.DATE).click()
        self.driver.find_element(*SecondPage.DATE).send_keys(date)
        self.driver.find_element(*SecondPage.DROPDOWN).click()
        self.driver.find_elements(*SecondPage.DROPDOWN_OPTION)[index].click()
        self.driver.find_element(By.ID, color).click()
        self.driver.find_element(*SecondPage.COMMENT).send_keys(comment)

    @allure.step('После заполнения второй формы, нажимаем кнопку "Далее"')
    def fill_second_form_button_next(self):
        self.driver.find_element(*SecondPage.BUTTON_NEXT).click()

    @allure.step('В модальном окне нажимаем кнопку "Да"')
    def button_yes_confirmation_window(self):
        self.driver.find_element(*ModalWindow.BUTTON_WINDOW).click()

    @allure.step('В модальном окне проверям сообщение об успешном создании заказа')
    def order_window(self):
        text = self.driver.find_element(*ModalWindow.TITLE_WINDOW).text
        return text

    @allure.step('В модальном окне нажимаем кнопку "Проверить заказ"')
    def button_check_status_modal_window(self):
        self.driver.find_element(*ModalWindow.BUTTON_CHECK_STATUS).click()

    @allure.step('Переход на главную страницу Яндекс')
    def go_to_yandex(self, driver, time=10):
        current_handle = driver.current_window_handle  # запоминаем handle текущего окна --- делается до клика, перехода на другую вкладку.
        self.click_element(Logo.LOGO_YANDEX)           # кликаем по лого и переходим на другую вкладку
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != current_handle:
                driver.switch_to.window(handle)
        return WebDriverWait(self.driver, time).until(EC.url_to_be("https://dzen.ru/?yredirect=true"))

















# order_button_below =                       # кнопка Заказать внизу страницы