from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    
    time.sleep(2)
    
    # Находим синюю кнопку по тексту (самый надежный способ)
    # У кнопки текст "Button with Dynamic ID"
    blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
    
    # Кликаем по кнопке
    blue_button.click()
    
    time.sleep(2)
    
    print("Клик по кнопке с динамическим ID выполнен успешно!")

finally:
    driver.quit()