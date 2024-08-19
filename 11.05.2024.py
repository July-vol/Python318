# Создать дескриптор класса Order, который задает имя товара, его цену и количество.
# В дескрипторе должна быть реализована проверка на ввод положительных значений цены и количества товара.
# Тест:
# Order('apple', 5, 10)
# 50

class Positive:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Введенное число должно быть положительным.')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Order:
    price = Positive()
    quantity = Positive()

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple_order = Order('apple', 5, 10)
print(apple_order.total())
