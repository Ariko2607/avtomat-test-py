import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # тест для проверки калькулятора с задержкой
    # создаем объект страницы
    calculator = CalculatorPage(driver)

    # открываем страницу
    calculator.open()

    # устанавливаем задержку 45 секунд
    calculator.set_delay("45")

    # Выполняем вычисление 7 + 8
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    # Ожидаем результат 15 (с запасом времени)
    calculator.wait_for_result("15", timeout=46)

    # Получаем результат и проверяем
    result = calculator.get_result()
    assert result == "15", f"Ожидалось 15, получено {result}"
