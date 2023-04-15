import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Переход на сайт Яндекс Самокат')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step('Ожидаем наличие элемента на странице')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    @allure.step('Ожидаем видимости элемента на странице')
    def wait_element_visible(self, element, time=10):
        """Ожидание видимости элемента."""
        return WebDriverWait(self.driver, time).until(EC.visibility_of(element), message=f'Element is not visible {element}')

    @allure.step('Прокручиваем до элемента по локатору')
    def scroll_to(self, locator):
        """Ищет элемент по локатору и прокручивает до него."""
        element = self.find_element(locator, time=3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Кликаем на элемент по локатору')
    def click_element(self, locator):
        """Находим элемент по локатору, ждем его видимости и кликаем его"""
        element = self.find_element(locator)
        self.wait_element_visible(element).click()
        return element
