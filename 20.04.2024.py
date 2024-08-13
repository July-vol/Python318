# Создайте класс для подсчета площади геометрических фигур. Класс должен представлять функциональность для подсчета
# площади треугольника по разным формулам, площади треугольника, площадь квадрата. Методы класса для подсчета площади
# должны быть реализованы с помощью статических методов Также класс должен считать  количество подсчетов площади и
# возвращать это значение с помощью статического метода.
# Площадь треугольника по формуле Герона(3, 4, 5): 6.0
# Площадь треугольника через основание и высоту(6, 7): 21.0
# Площадь квадрата (7): 49
# Площадь прямоугольника (2, 6): 12
# Количество подсчетов площади: 4

import math


class Area:
    count = 0

    @staticmethod
    def triangle_area_1(a, b, c):
        p = (a + b + c) / 2
        Area.count += 1
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def triangle_area_2(a, h):
        Area.count += 1
        return 0.5 * a * h

    @staticmethod
    def square_area_(a):
        Area.count += 1
        return a ** 2

    @staticmethod
    def rect_area_(a, b):
        Area.count += 1
        return a * b

    @staticmethod
    def get_count():
        return Area.count


print(f"Площадь треугольника по формуле Герона: {Area.triangle_area_1(3, 4, 5)}")
print(f"Площадь треугольника через основание и высоту: {Area.triangle_area_2(6, 7)}")
print(f"Площадь квадрата: {Area.square_area_(7)}")
print(f"Площадь прямоугольника: {Area.rect_area_(2, 6)}")
print(f"Количество подсчетов площади: {Area.get_count()}")
