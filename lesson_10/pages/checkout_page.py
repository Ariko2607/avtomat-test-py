"""
Page Object для страницы оформления заказа.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Page Object для страницы оформления заказа SauceDemo.
    """

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        """
        Заполнить форму данными заказчика.

        Args:
            first_name: str - имя
            last_name: str - фамилия
            postal_code: str - почтовый индекс

        Returns:
            CheckoutPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        return self

    def continue_checkout(self):
        """
        Нажать кнопку Continue (продолжить оформление).

        Returns:
            CheckoutPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total(self):
        """
        Получить итоговую стоимость заказа.

        Returns:
            float: итоговая стоимость в виде числа (например, 58.29)
        """
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text
        return float(total_text.replace("Total: $", ""))
