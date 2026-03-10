from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открываем браузер Firefox
driver = webdriver.Firefox()

try:
    # Переходим на страницу логина
    driver.get("http://the-internet.herokuapp.com/login")
    
    time.sleep(2)
    
    # Находим поле username и вводим tomsmith
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("Ввели username")
    
    # Находим поле password и вводим SuperSecretPassword!
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Ввели password")
    
    # Находим кнопку Login и нажимаем
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Нажали кнопку Login")
    
    time.sleep(2)
    
    # Находим зеленую плашку с сообщением
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    
    # Выводим текст плашки в консоль
    message_text = success_message.text
    print(f"\nСообщение с зеленой плашки: {message_text}")
    
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт")