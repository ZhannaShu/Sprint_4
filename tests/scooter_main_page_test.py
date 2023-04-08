import pytest
from selenium import webdriver
from scooter_main_page import ScooterMainPage
from base_page import BasePage

class Test:
    def test_click_on_cookies(self, driver):
        scooter_main = ScooterMainPage(BasePage)
        scooter_main.click_on_cookies(self)







        # yandex_scooter_main_page.click_on_the_order_button_in_the_header_of_the_page()   # клик по кнопке Заказать в шапке страницы
        # page_with_a_form_for_whom_scooter.go_to_page()        # переход на страницу с формой Для кого самокат
        # element_field_name.send_name()     # ввести имя в поле Имя на странице Для кого самокат
        # element_field_last_name.send_last()  # ввести фамилию в поле Фамилия на странице Для кого самокат






