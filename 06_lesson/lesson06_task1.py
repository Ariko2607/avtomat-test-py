from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/ajax")
    # Ждем, когда кнопка станет кликабельной, и нажимаем её
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton"))
    )
    button.click()
    # Ждем появления зеленой плашки с результатом
    green_badge = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    # Получаем текст из плашки
    text = green_badge.text
    print(text)
finally:
    # Закрываем браузер
    driver.quit()
