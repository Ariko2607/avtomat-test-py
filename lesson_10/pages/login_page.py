"""
Page Object для страницы авторизации интернет-магазина SauceDemo.
"""

from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object для страницы авторизации SauceDemo.
    URL: https://www.saucedemo.com/
    """

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver

    def login(self, username, password):
        """
        Выполнить авторизацию с указанными учетными данными.

        Args:
            username: str - имя пользователя (например, "standard_user")
            password: str - пароль (например, "secret_sauce")

        Returns:
            LoginPage: текущий экземпляр страницы (для цепочки вызовов)
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return self
