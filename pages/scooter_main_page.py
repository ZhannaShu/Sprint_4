import allure
from locators.scooter_main_page_locators import LocatorScooterMainPage
from .base_page import BasePage

class ScooterMainPage(BasePage):
    @allure.step('Получаем текст на вопрос')
    def get_element_text(self, locator):
        """По локатору ищет элемент, ждет его видимости и отдает его текст."""
        element = self.find_element(locator)
        return self.wait_element_visible(element).text

    @allure.step('Прокручиваем страницу до раздела Вопросы о важном')
    def goto_important_questions(self):
        self.go_to_site()
        self.click_element(LocatorScooterMainPage.Cookies)
        self.scroll_to(LocatorScooterMainPage.Questions_About_Important)
