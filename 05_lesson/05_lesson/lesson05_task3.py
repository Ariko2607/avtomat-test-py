from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Открываем браузер Firefox
driver = webdriver.Firefox()

try:
    # Переходим на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    time.sleep(2)
    
    # Находим поле ввода (это элемент <input type="number">)
    input_field = driver.find_element(By.TAG_NAME, "input")
    
    # Вводим текст 12345
    input_field.send_keys("12345")
    print("Ввели 12345")
    time.sleep(2)
    
    # Очищаем поле
    input_field.clear()
    print("Очистили поле")
    time.sleep(2)
    
    # Вводим текст 54321
    input_field.send_keys("54321")
    print("Ввели 54321")
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт")