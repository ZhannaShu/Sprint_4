import allure
from pages.scooter_logo_page import ScooterLogo
from locators.scooter_order_locators import LocatorOrder, Logo

class TestLogo:
    @allure.title('Клик на логотип Самоката, попадаем на главную страницу Самоката')
    def test_go_to_home_page_scooter(self, driver):
        scooter_logo = ScooterLogo(driver)
        scooter_logo.go_to_site()
        scooter_logo.click_element(LocatorOrder.Cookies)
        scooter_logo.click_element(LocatorOrder.BUTTON_ORDER_HEADER)
        scooter_logo.click_element(Logo.LOGO_SCOOTER)
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Клик на логотип Яндекс, попадаем на главную страницу Яндекса')
    def test_go_to_home_page_yandex(self, driver):
        scooter_logo = ScooterLogo(driver)
        scooter_logo.go_to_site()
        scooter_logo.click_element(LocatorOrder.Cookies)
        scooter_logo.go_to_yandex(driver)
        url_yandex = driver.current_url
        assert url_yandex == "https://dzen.ru/?yredirect=true"