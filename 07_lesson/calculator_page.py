from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    # Page Object для страницы калькулятора

    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")

    def open(self):
        # открыть страницу калькулятора
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator")

    def set_delay(self, seconds):
        # установить задержку в секундах
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(seconds)

    def click_button(self, button_text):
        # нажать на кнопку калькулятора по тексту
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def get_result(self):
        # получить результат вычислений
        return self.driver.find_element(*self.result_display).text

    def wait_for_result(self, expected_value, timeout=46):
        # появления ожидаемого результата
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.result_display, expected_value)
        )
