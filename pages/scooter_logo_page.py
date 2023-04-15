import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.scooter_order_locators import Logo
from pages.base_page import BasePage

class ScooterLogo(BasePage):
    @allure.step('Переход на главную страницу Яндекс')
    def go_to_yandex(self, driver, time=10):
        current_handle = driver.current_window_handle
        self.click_element(Logo.LOGO_YANDEX)
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != current_handle:
                driver.switch_to.window(handle)
        return WebDriverWait(self.driver, time).until(EC.url_to_be("https://dzen.ru/?yredirect=true"))