from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/classattr")
    
    # Даем странице загрузиться
    time.sleep(2)
    
    # Находим синюю кнопку по CSS-классу
    # У кнопки класс "btn-primary"
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    
    # Кликаем по кнопке
    blue_button.click()
    
    # Ждем немного, чтобы увидеть результат
    time.sleep(2)
    
    print("Клик по синей кнопке выполнен успешно!")

finally:
    # Закрываем браузер
    driver.quit()