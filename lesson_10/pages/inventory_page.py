"""
Page Object для главной страницы магазина (каталог товаров).
"""

from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Page Object для страницы каталога товаров SauceDemo.
    """

    def __init__(self, driver):
        """
        Инициализация страницы каталога.

        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver

    def add_product_by_id(self, product_id):
        """
        Добавить товар в корзину по его ID.

        Args:
            product_id: str - ID кнопки добавления товара
                (например, "add-to-cart-sauce-labs-backpack")

        Returns:
            InventoryPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        self.driver.find_element(By.ID, product_id).click()
        return self

    def go_to_cart(self):
        """
        Перейти в корзину (нажать на иконку корзины).

        Returns:
            InventoryPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return self
