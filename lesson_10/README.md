# Lesson 10: Allure Reports для PageObject тестов

## Описание проекта

В этом проекте реализованы автоматические тесты для:
- Калькулятора (https://bonigarcia.dev/selenium-webdriver-java/slow-calculator)
- Интернет-магазина SauceDemo (https://www.saucedemo.com/)

Тесты написаны с использованием паттерна PageObject и покрыты Allure-отчетами.

## Структура проекта
lesson_10/
├── pages/ # Page Object классы
│ ├── init.py
│ ├── calculator_page.py # Страница калькулятора
│ ├── login_page.py # Страница авторизации
│ ├── inventory_page.py # Страница каталога
│ ├── cart_page.py # Страница корзины
│ └── checkout_page.py # Страница оформления заказа
├── tests/ # Тесты
│ ├── init.py
│ ├── test_calculator.py # Тесты калькулятора
│ └── test_shop.py # Тесты магазина
└── README.md # Документация

## Запуск тестов
Запуск всех тестов с формированием Allure-отчета
   # Запуск тестов и сохранение результатов
 pytest tests/ --alluredir=allure-results
   # Генерация HTML-отчета
 allure generate allure-results -o allure-report --clean
   # Открытие отчета в браузере
 allure open allure-report

## Запуск конкретного теста
   # Только тесты калькулятора
 pytest tests/test_calculator.py --alluredir=allure-results
   # Только тесты магазина
 pytest tests/test_shop.py --alluredir=allure-results

## Требования
* Python 3.8+
* Chrome и ChromeDriver (для тестов калькулятора)
* Firefox и GeckoDriver (для тестов магазина)
* Allure Commandline

## Установка Allure Commandline
# macOS:
- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Windows (через Scoop):
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
- Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
- scoop install allure


## Запуск тестов и формирование отчета

# Переходим в папку lesson_10
cd lesson_10

# Запуск тестов с сохранением результатов
pytest tests/ --alluredir=allure-results

# Генерация отчета
allure serve allure-result

# Открытие отчета
allure open allure-report