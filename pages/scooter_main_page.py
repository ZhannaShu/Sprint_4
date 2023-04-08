from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base_page import BasePage


class LocatorScooterMainPage:
    Locator_Scooter_Cookies = (By.CLASS_NAME, "App_CookieButton__3cvqF")     # локатор Куки
    Locator_Scooter_Questions_About_Important = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")


class ScooterMainPage(BasePage):
    def click_on_cookies(self):
        return self.find_element(LocatorScooterMainPage.Locator_Scooter_Cookies).click()    # клик по Куки

    def scroll_to_questions_about_important(self, driver):
        element = self.find_element(LocatorScooterMainPage.Locator_Scooter_Questions_About_Important, time=3)
        return driver.execute_script("arguments[0].scrollIntoView();", element)





        #element_Questions_about_important = [By.CLASS_NAME]
