import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_saucedemo_purchase(driver):
    # Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")
    
    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Ждем загрузки страницы с товарами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    
    # Добавляем товары в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    
    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Ждем загрузки корзины
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
    
    # Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()
    
    # Заполняем форму своими данными
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Анастасия")
    driver.find_element(By.ID, "last-name").send_keys("Александрова")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    
    # Нажимаем Continue
    driver.find_element(By.ID, "continue").click()
    
    # Ждем загрузки страницы с итогом
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    
    # Извлекаем число из строки вида "Total: $58.29"
    total_value = float(total_text.replace("Total: $", ""))
    
    # Проверяем итоговую сумму
    expected_total = 58.29
    assert total_value == expected_total, (
     f"Ожидалось ${expected_total}, получено ${total_value}")
    print(f"Итоговая сумма: ${total_value} - тест пройден!")
