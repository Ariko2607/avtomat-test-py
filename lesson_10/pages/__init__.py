"""
Пакет с Page Object классами для тестирования.
"""

from .calculator_page import CalculatorPage
from .login_page import LoginPage
from .inventory_page import InventoryPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage

__all__ = [
    "CalculatorPage",
    "LoginPage",
    "InventoryPage",
    "CartPage",
    "CheckoutPage",
]