"""
Page Object для страницы калькулятора.
Ссылка: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы калькулятора с задержкой.

    Содержит методы для взаимодействия с элементами калькулятора:
    - установка задержки
    - нажатие кнопок
    - получение результата
    - ожидание результата
    """

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")

    def open(self):
        """
        Открыть страницу калькулятора.

        Returns:
            CalculatorPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator"
        )
        return self

    def set_delay(self, seconds):
        """
        Установить задержку выполнения операций.

        Args:
            seconds: str | int - значение задержки в секундах

        Returns:
            CalculatorPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(seconds)
        return self

    def click_button(self, button_text):
        """
        Нажать на кнопку калькулятора по тексту на ней.

        Args:
            button_text: str - текст на кнопке (например, "7", "+", "=")

        Returns:
            CalculatorPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        )
        button.click()
        return self

    def get_result(self):
        """
        Получить результат вычисления с дисплея калькулятора.

        Returns:
            str: результат вычисления в виде строки
        """
        return self.driver.find_element(*self.result_display).text

    def wait_for_result(self, expected_value, timeout=46):
        """
        Ожидать появления ожидаемого результата на дисплее.

        Args:
            expected_value: str - ожидаемое значение результата
            timeout: int - максимальное время ожидания в секундах (по умолчанию 46)

        Returns:
            bool: True если результат появился в течение таймаута
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.result_display, expected_value
            )
        )
        return True
