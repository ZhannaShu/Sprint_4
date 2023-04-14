from selenium.webdriver.common.by import By

class LocatorOrder:
    Cookies = (By.CLASS_NAME, "App_CookieButton__3cvqF")                              # локатор Куки
    BUTTON_ORDER_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g']")       # кнопка Заказать в Шапке
    BUTTON_ORDER_BODY = (By.XPATH, "(//button[text()='Заказать'])[2]")
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")                                # поле Имя
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")                         # поле Фамилия
    ADDRES = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")       # поле Имя
    STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")                   # клик по полю Станция метро
    CLICK_STATION = (By.CLASS_NAME, "select-search__select")                          # клик по названию станции
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # поле Телефон
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")                              # кнопка Далее

class SecondPage:
    DATE = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]                # поле Когда привезти самокат
    DATE_SELECTED = [By.CLASS_NAME, 'react-datepicker__day--selected']                # выбираем дату
    DROPDOWN = (By.XPATH, ".//*[@class='Dropdown-arrow']")                            # поле Срок аренды
    DROPDOWN_OPTION = (By.XPATH, ".//*[@class='Dropdown-menu']/div")                  # поле выбираем срок аренды
    COMMENT = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")              # поле Комментарий для курьера
    BUTTON_NEXT = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")   # кнопка Заказать в форме Про аренду

class ModalWindow:
    BUTTON_WINDOW = (By.XPATH, "//button[text()='Да']")                               # кнопка Да в окне Хотите оформить заказ
    BUTTON_CHECK_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")          # кнопка Посмотреть статус в окне Заказ оформлен
    TITLE_WINDOW = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")                        # заголовок Заказ оформлен

class Logo:
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")                                # логотип Самокат
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")                                  # логотип Яндекс


