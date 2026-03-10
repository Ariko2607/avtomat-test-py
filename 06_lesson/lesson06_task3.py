from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images")
    # Ждем, когда загрузятся ВСЕ 4 картинки
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "landscape")))
    print("Все картинки загружены")
    # Теперь находим 3-ю картинку по её ID
    third_image = driver.find_element(By.ID, "award")
    # Получаем значение атрибута src
    src_value = third_image.get_attribute("src")
    # Выводим в консоль
    print(f"src 3-й картинки: {src_value}")

finally:
    # Закрываем браузер
    driver.quit()
