""""Класс для работы с главной страницой Google"""

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class GooglePage(BasePage):
    """"Модель страницы Google"""

    I_AM_FEELING_LUCKY = (By.XPATH, "(//input[@name='btnI'])[2]")
    DOODLES_ARCHIVE = (By.ID, "archive-link-link")

    url = 'https://google.com/'

    def click_lucky_button(self):
        """"Поиск кнопки 'Мне повезёт!' и клик по ней"""
        self.find_element(self.I_AM_FEELING_LUCKY).click()
        
    def check_archive_on_page(self):
        """"Поиск ссылки на Doodles Archive и возвращение содержимого link text"""
        return self.find_element(self.DOODLES_ARCHIVE).text
