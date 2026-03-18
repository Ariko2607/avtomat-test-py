import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_saucedemo_purchase(driver):
    # Открываем сайт
    driver.get("https://www.saucedemo.com/")

    # Создаем объект страницы авторизации и логинимся
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Создаем объект страницы товаров
    inventory_page = InventoryPage(driver)
    # Добавляем товары по их ID
    inventory_page.add_product_by_id("add-to-cart-sauce-labs-backpack")
    inventory_page.add_product_by_id("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_product_by_id("add-to-cart-sauce-labs-onesie")
    # Переходим в корзину
    inventory_page.go_to_cart()

    # Создаем объект страницы корзины
    cart_page = CartPage(driver)
    cart_page.checkout()

    # Создаем объект страницы оформления заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Анастасия", "Александрова", "123456")
    checkout_page.continue_checkout()

    # Получаем итоговую сумму
    total = checkout_page.get_total()

    # Проверка суммы
    expected_total = 58.29
    assert total == expected_total, f"Ожидалось ${expected_total}, получено $"
    print(f"Итоговая сумма: ${total} - тест пройден!")
