""""Базовый класс с методами для работы на страницах"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """"Модель страницы"""

    def __init__(self, driver):
        """"Инициализация вебдрайвера и часто используемых классов вебдрайвера"""
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 60)
        self._action = ActionChains(self.driver)

    def find_element(self, locator):
        """"Поиск элемента по локатору"""
        return self._wait.until(EC.presence_of_element_located(locator), message='Элемент не найден')

    def find_elements(self, locator):
        """"Поиск элементов по локатору"""
        return self._wait.until(EC.presence_of_all_elements_located(locator), message='Элемент не найден')

    def wait_page_loading(self, page_name=None):
        """"Ожидание загрузки страницы"""
        self._wait.until(EC.presence_of_element_located(((By.CSS_SELECTOR, 'div'))), message=f'Страница {page_name} не загрузилась')

    def go_to_site(self):
        """"Переход на сайт из класса потомка"""
        return self.driver.get(self.url)

    def go_to_link(self, link: str):
        """"Переход на сайт"""
        return self.driver.get(link)

    def go_to_main_window(self):
        """"Переключение на первое окно браузера"""
        self.driver.switch_to.window(self.driver.window_handles[0])

    def go_to_opened_window(self):
        """"Переключение на второе окно браузера"""
        self.driver.switch_to.window(self.driver.window_handles[1])

    def go_to_chosen_window(self, num: int):
        """"Переключение на выбранное окно браузера"""
        self.driver.switch_to.window(self.driver.window_handles[num])

    def current_url(self):
        """"Возвращает текущий url"""
        return self.driver.current_url

    # Иногда нужен для клика в внутри Docker
    def javascript_click(self, element):
        """"Клик через JS"""
        self.driver.execute_script("arguments[0].click();", element)

    def javascript_scroll_to(self, element):
        """"Скролл к элементу через JS"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to(self, element):
        """"Скролл к элементу через ActionChains"""
        self._action.scroll_to_element(element)
        