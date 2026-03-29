"""
Page Object для страницы корзины.
"""

from selenium.webdriver.common.by import By


class CartPage:
    """
    Page Object для страницы корзины SauceDemo.
    """

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver

    def checkout(self):
        """
        Нажать кнопку Checkout (оформить заказ).

        Returns:
            CartPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        self.driver.find_element(By.ID, "checkout").click()
        return self
