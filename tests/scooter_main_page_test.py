import allure
from pages.scooter_main_page import ScooterMainPage
from locators.scooter_main_page_locators import LocatorScooterMainPage, Data

class Test:
    @allure.description('Получаем ответ на вопрос "Сколько стоит?" и сравниваем с ожидаемым')
    def test_check_answer_for_Questions_0(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMainPage.Questions_0)
        actual_text = scooter_main.get_element_text(LocatorScooterMainPage.MESSAGE_0)
        expected_text = Data.Answer_To_Question_0
        assert actual_text == expected_text

    @allure.description('Получаем ответ на вопрос Хочу сразу несколько самокатов! Так можно? и сравниваем с ожидаемым')
    def test_check_answer_for_Questions_1(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMainPage.Questions_1)
        actual_text = scooter_main.get_element_text(LocatorScooterMainPage.MESSAGE_1)
        expected_text = Data.Answer_To_Question_1
        assert actual_text == expected_text

    @allure.description('Получаем ответ на вопрос Как рассчитывается время аренды? и сравниваем с ожидаемым')
    def test_check_answer_for_Questions_2(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMainPage.Questions_2)
        actual_text = scooter_main.get_element_text(LocatorScooterMainPage.MESSAGE_2)
        expected_text = Data.Answer_To_Question_2
        assert actual_text == expected_text

    @allure.description('Получаем ответ на вопрос Можно ли заказать самокат прямо на сегодня? и сравниваем с ожидаемым')
    def test_check_answer_for_Questions_3(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMainPage.Questions_3)
        actual_text = scooter_main.get_element_text(LocatorScooterMainPage.MESSAGE_3)
        expected_text = Data.Answer_To_Question_3
        assert actual_text == expected_text

    @allure.description('Получаем ответ на вопрос Можно ли продлить заказ или вернуть самокат раньше? и сравниваем с ожидаемым')
    def test_check_answer_for_Questions_4(self, driver):
            scooter_main = ScooterMainPage(driver)
            scooter_main.goto_important_questions()
            scooter_main.click_element(LocatorScooterMainPage.Questions_4)
            actual_text = scooter_main.get_element_text(LocatorScooterMainPage.MESSAGE_4)
            expected_text = Data.Answer_To_Question_4
            assert actual_text == expected_text

    @allure.description('Получаем ответ на вопрос Вы привозите зарядку вместе с самокатом? и сравниваем с ожидаемым')
    def test_check_answer_for_Questions_5(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMainPage.Questions_5)
        actual_text = scooter_main.get_element_text(
            LocatorScooterMainPage.MESSAGE_5)
        expected_text = Data.Answer_To_Question_5
        assert actual_text == expected_text

    @allure.description('Получаем ответ на вопрос Можно ли отменить заказ? и сравниваем с ожидаемым')
    def test_check_answer_for_Questions_6(self, driver):
            scooter_main = ScooterMainPage(driver)
            scooter_main.goto_important_questions()
            scooter_main.click_element(LocatorScooterMainPage.Questions_6)
            actual_text = scooter_main.get_element_text(LocatorScooterMainPage.MESSAGE_6)
            expected_text = Data.Answer_To_Question_6
            assert actual_text == expected_text

    @allure.description('Получаем ответ на вопрос Я живу за МКАДом, привезёте? и сравниваем с ожидаемым')
    def test_check_answer_for_Questions_7(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMainPage.Questions_7)
        actual_text = scooter_main.get_element_text(LocatorScooterMainPage.MESSAGE_7)
        expected_text = Data.Answer_To_Question_7
        assert actual_text == expected_text










        # yandex_scooter_main_page.click_on_the_order_button_in_the_header_of_the_page()   # клик по кнопке Заказать в шапке страницы
        # page_with_a_form_for_whom_scooter.go_to_page()        # переход на страницу с формой Для кого самокат
        # element_field_name.send_name()     # ввести имя в поле Имя на странице Для кого самокат
        # element_field_last_name.send_last()  # ввести фамилию в поле Фамилия на странице Для кого самокат






