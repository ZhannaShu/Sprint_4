import allure
from selenium.webdriver.common.by import By
from locators.scooter_order_locators import LocatorOrder, SecondPage, ModalWindow
from .base_page import BasePage

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
