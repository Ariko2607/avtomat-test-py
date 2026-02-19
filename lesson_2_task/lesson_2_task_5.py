def month_to_season(month):
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Неверный номер месяца, пожалуйста введите от 1 до 12"


try:
    month_number = int(input("Введите номер месяца от 1 до 12:"))
except ValueError:
    print("Ошибка: пожалуйста введите номер месяца от 1 до 12")
else:
    # Здесь можно вызвать функцию month_to_season и обработать корректный ввод
    season = month_to_season(month_number)
    print(season)
