"""
Тесты для интернет-магазина SauceDemo.
"""

import allure
import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера Firefox.

    Yields:
        WebDriver: экземпляр веб-драйвера
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Интернет-магазин SauceDemo")
@allure.story("Оформление заказа")
@allure.title("Проверка итоговой стоимости заказа")
@allure.description(
    "Тест проверяет, что итоговая стоимость заказа из трех товаров "
    "(Sauce Labs Backpack, Bolt T-Shirt, Onesie) составляет $58.29. "
    "Ввод Логина и Пароля"
)
@allure.severity(allure.severity_level.BLOCKER)
@allure.tag("shop", "cart", "checkout", "positive")
def test_saucedemo_purchase(driver):
    """
    Тест проверки итоговой стоимости заказа.
    """
    with allure.step("Открываем главную страницу магазина"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Создаём страницу, где можно ввести логин и пароль, и выполнить вход в аккаунт"):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Создаём страницу каталога с товарами и добовляем их в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_by_id("add-to-cart-sauce-labs-backpack")
        inventory_page.add_product_by_id("add-to-cart-sauce-labs-bolt-t-shirt")
        inventory_page.add_product_by_id("add-to-cart-sauce-labs-onesie")

    with allure.step("Переходим в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Создаём страницу корзины и нажимаем Checkout - оформить заказ"):
        cart_page = CartPage(driver)
        cart_page.checkout()

    with allure.step("Заполняем данные о заказчике, Имя, Фамилия и ИНДКС"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Анастасия", "Александрова", "123456")

    with allure.step("Нажать кнопку Continue - продолжить"):
        checkout_page.continue_checkout()

    with allure.step("Получаем итоговую сумму заказа"):
        total = checkout_page.get_total()

    with allure.step("Проверяем, что итоговая сумма равна $58.29"):
        expected_total = 58.29
        assert total == expected_total, (
            f"Ожидалось ${expected_total}, получено ${total}"
        )

    with allure.step("Вывести сообщение об успешном прохождении теста"):
        print(f"Итоговая сумма: ${total} - тест пройден!")
