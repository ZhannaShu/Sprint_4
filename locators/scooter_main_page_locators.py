from selenium.webdriver.common.by import By


class LocatorScooterMainPage:
    Cookies = (By.CLASS_NAME, "App_CookieButton__3cvqF")                                  # локатор Куки
    Questions_About_Important = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")  # Вопросы о важном
    Questions_0 = (By.ID, "accordion__heading-0")                                         # вопрос Сколько это стоит
    Questions_1 = (By.ID, "accordion__heading-1")                                         # вопрос Хочу сразу несколько самокатов
    Questions_2 = (By.ID, "accordion__heading-2")                                         # вопрос Как рассчитывается время аренды
    Questions_3 = (By.ID, "accordion__heading-3")                                         # вопрос Можно ли заказать самокат прямо на сегодня
    Questions_4 = (By.ID, "accordion__heading-4")                                         # вопрос Можно ли продлить заказ или вернуть самокат раньше
    Questions_5 = (By.ID, "accordion__heading-5")                                         # вопрос Вы привозите зарядку вместе с самокатом
    Questions_6 = (By.ID, "accordion__heading-6")                                         # вопрос Можно ли отменить заказ
    Questions_7 = (By.ID, "accordion__heading-7")                                         # вопрос Я живу за МКАДом, привезёте

    MESSAGE_0 = (By.XPATH, '//div[@id="accordion__panel-0"]/p')                       # сообщение MESSAGE_0
    MESSAGE_1 = (By.XPATH, '//div[@id="accordion__panel-1"]/p')                       # сообщение MESSAGE_1
    MESSAGE_2 = (By.XPATH, '//div[@id="accordion__panel-2"]/p')                       # сообщение MESSAGE_2
    MESSAGE_3 = (By.XPATH, '//div[@id="accordion__panel-3"]/p')                       # сообщение MESSAGE_3
    MESSAGE_4 = (By.XPATH, '//div[@id="accordion__panel-4"]/p')                       # сообщение MESSAGE_4
    MESSAGE_5 = (By.XPATH, '//div[@id="accordion__panel-5"]/p')                       # сообщение MESSAGE_5
    MESSAGE_6 = (By.XPATH, '//div[@id="accordion__panel-6"]/p')                       # сообщение MESSAGE_6
    MESSAGE_7 = (By.XPATH, '//div[@id="accordion__panel-7"]/p')                       # сообщение MESSAGE_7
class Data:
    Answer_To_Question_0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    Answer_To_Question_1 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, ' \
                           'можете просто сделать несколько заказов — один за другим.'
    Answer_To_Question_2 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт ' \
                           'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли ' \
                           'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    Answer_To_Question_3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    Answer_To_Question_4 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    Answer_To_Question_5 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если ' \
                           'будете кататься без передышек и во сне. Зарядка не понадобится.'
    Answer_To_Question_6 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    Answer_To_Question_7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
