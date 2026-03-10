# Создать функцию которая принимает год/число и возращает True/False
def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"


# Выбираем любой год для проверки
year = 1900
# Вызываем функцию и сохраняем результат в переменную
result = is_year_leap(year)
# Выводим результат
print(f"год {year}: {result}")

# Проверим несколько годов и выведем списком
years_to_check = [2020, 2008, 2023, 2009, 1902, 2000]

for year in years_to_check:
    result = is_year_leap(year)
    print(f"год {year}: {result}")

# попросим спросить какой год мы хотим проверить
year = int(input("Введите год: "))
result = is_year_leap(year)
print(f"год {year}: {result}")