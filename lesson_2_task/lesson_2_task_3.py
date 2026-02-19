# математика зло - для гуманитария
import math


def square(side):
    area = side * side
    
    # Если сторона была не целым числом, округляем результат вверх
    if not isinstance(side, int):
        area = math.ceil(area)
    
    return area


side1 = 5
side2 = 5.5
side3 = 3.2

print(f"Площадь квадрата со стороной {side1} = {square(side1)}")
print(f"Площадь квадрата со стороной {side2} = {square(side2)}")
print(f"Площадь квадрата со стороной {side3} = {square(side3)}")