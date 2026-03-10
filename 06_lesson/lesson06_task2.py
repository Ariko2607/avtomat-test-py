from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/textinput")
    # Ждем появления поля ввода и вводим текст
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
    )
    input_field.send_keys("SkyPro")
    # Ждем появления кнопки и нажимаем её
    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()
    # Ждем, когда текст кнопки обновится
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"),
                                         "SkyPro"))
    # Получаем текст кнопки
    button_text = button.text
    print(button_text)


finally:
    driver.quit()
