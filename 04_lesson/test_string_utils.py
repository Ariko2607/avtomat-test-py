import pytest
from string_utils import StringUtils

utils = StringUtils()


# Тесты для метода capitalize


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("training", "Training"),                        # одно слово латиница
    ("обучение", "Обучение"),                        # одно слово кириллица
    ("обучение начинается", "Обучение начинается"),  # текст с пробелом
    ("злой. добрый", "Злой. добрый"),         # заглавная буква после точки
    ("поехали в китай", "Поехали в китай"),   # страны с большой буквы
    ("меня зовут коля", "Меня зовут коля"),   # ФИО с большой буквы
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),  # строка с цифрами
    ("", ""),              # пустая строка
    ("   ", "   "),        # строка из пробелов
    ("пРивет", "Привет"),  # вторая заглавная буква
])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected


# Тесты для метода trim


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),     # латиница с пробеломпробелами в начале
    ("   скайпро", "скайпро"),   # кириллица с пробелами в начале
    ("   БОЛЬШОЙ", "БОЛЬШОЙ"),   # слово в верхнем регистре
    ("  пробелы  ", "пробелы  "),  # пробелы после слова
    ("нет пробела", "нет пробела")  # нет пробелов
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                # пустая строка
    ("    ", ""),            # строка только с пробелами
])
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) == expected


# Тесты для метода contains


@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),  # символ в верхнем регистре
    ("SkyPro", "Pro", True),  # часть слова
    ("Hello", "e", True),  # символ в нижнем регистре
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", False),  # символ осуттвующий в строке 
    ("", "a", False),     # символ в пустой строке
    ("Hello", "", True),   # пустой символ считается найденным?
])
def test_contains_negative(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


# Тесты для метода delete_symbol

@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("banana", "a", "bnn"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative_testc
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("", "a", ""),
    ("hello", "", "hello"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
