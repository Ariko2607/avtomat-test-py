"""
Тесты для страницы калькулятора.
"""

import allure
import pytest
from selenium import webdriver
from pages import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для создания и закрытия драйвера Chrome.

    Yields:
        WebDriver: экземпляр веб-драйвера
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.story("Проверка арифметических операций")
@allure.title("Сложение 7 + 8 с задержкой")
@allure.description(
    "Тест проверяет, что калькулятор корректно складывает сумму 7 и 8 "
    "с учетом установленной задержки в 45 секунд. Ожидаемый результат: 15."
)
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("calculator", "positive")
def test_slow_calculator(driver):
    """
    Тест проверки сложения 7 + 8 = 15 с задержкой 45 секунд.
    """
    with allure.step("Создаём страницу калькулятора"):
        calculator = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        calculator.open()

    with allure.step("Установить задержку в 45 секунд"):
        calculator.set_delay("45")

    with allure.step("Ввести выражение 7 + 8"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Ожидаем начала отсчёта задержки в 45 секунд 15 сек. (с запасом времени)"):
        calculator.wait_for_result("15", timeout=46)

    with allure.step("Получаем результаты вычисления"):
        result = calculator.get_result()

    with allure.step("Проверяем, что результат равен 15"):
        assert result == "15", f"Ожидалось 15, получено {result}"
