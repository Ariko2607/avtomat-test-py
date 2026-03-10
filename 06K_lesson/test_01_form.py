import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission(driver):
    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types")
    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    # Нажимаем кнопку Submit
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    # Ждем появления результатов
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    # Проверяем, что поле Zip code подсвечено красным
    zip_code_field = driver.find_element(By.ID, "zip-code")
    zip_code_class = zip_code_field.get_attribute("class")
    assert "danger" in zip_code_class, f"Поле Zip code красный, но класс:{zip_code_class}"
    # Список полей, которые должны быть зелеными
    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    # Проверяем каждое поле на наличие класса "success"
    for field_name in green_fields:
        field = driver.find_element(By.ID, field_name)
        field_class = field.get_attribute("class")
        assert "success" in field_class, f"Поле {field_name} зеленый, но класс: {field_class}"


print("Все проверки пройдены успешно!")
