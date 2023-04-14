import allure
from locators.scooter_order_locators import LocatorOrder, Logo
from pages.scooter_order_page import ScooterOrderPage, UserData

class Test:
    @allure.description('Флоу позитивного сценария по кнопке Заказать в шапке')
    def test_order_by_button_in_the_header(self, driver):
        scooter_order = ScooterOrderPage(driver)
        scooter_order.go_to_site()
        scooter_order.click_element(LocatorOrder.Cookies)
        scooter_order.click_element(LocatorOrder.BUTTON_ORDER_HEADER)
        scooter_order.fill_out_the_form_for_whom_the_scooter(name=UserData.firstname_male, surname=UserData.surname_male, addres=UserData.address_male,
                           station=UserData.station_male, phone=UserData.phone_male)
        scooter_order.click_element(LocatorOrder.BUTTON_NEXT)
        scooter_order.fill_out_the_rental_form(date=UserData.date_male, index=UserData.indx_male, color=UserData.color_male, comment=UserData.comment_male)
        scooter_order.fill_second_form_button_next()
        scooter_order.button_yes_confirmation_window()
        title = scooter_order.order_window()
        scooter_order.button_check_status_modal_window()
        assert 'Заказ оформлен' in title

        scooter_order.click_element(Logo.LOGO_SCOOTER)
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

        scooter_order.go_to_yandex(driver)
        url_yandex = driver.current_url
        assert url_yandex == "https://dzen.ru/?yredirect=true"


    @allure.description('Флоу позитивного сценария по кнопке Заказать в середине страницы')
    def test_order_by_button_in_the_body(self, driver):
        scooter_order = ScooterOrderPage(driver)
        scooter_order.go_to_site()
        scooter_order.click_element(LocatorOrder.Cookies)
        scooter_order.scroll_to(LocatorOrder.BUTTON_ORDER_BODY)
        scooter_order.click_element(LocatorOrder.BUTTON_ORDER_BODY)
        scooter_order.fill_out_the_form_for_whom_the_scooter(name=UserData.firstname_female,
                                                                 surname=UserData.surname_female,
                                                                 addres=UserData.address_female,
                                                                 station=UserData.station_female,
                                                                 phone=UserData.phone_female)
        scooter_order.click_element(LocatorOrder.BUTTON_NEXT)  # клик по кнопке Далее
        scooter_order.fill_out_the_rental_form(date=UserData.date_female, index=UserData.indx_female,
                                                   color=UserData.color_female, comment=UserData.comment_female)
        scooter_order.fill_second_form_button_next()
        scooter_order.button_yes_confirmation_window()
        title = scooter_order.order_window()
        scooter_order.button_check_status_modal_window()
        assert 'Заказ оформлен' in title

        scooter_order.click_element(Logo.LOGO_SCOOTER)
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

        scooter_order.go_to_yandex(driver)
        url_yandex = driver.current_url
        assert url_yandex == "https://dzen.ru/?yredirect=true"




