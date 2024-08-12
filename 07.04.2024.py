# Реализуйте класс "Автомобиль". Необходимо хранить в полях класса
# название модели, год выпуска, производителя,мощность двигателя, цвет,
# цену. Реализуйте методы класса для ввода данных, вывода данныз,\
# реализуйте доступ к отдельным полям через методы класса.


class Auto:
    model = "name"
    release = "0000"
    manufacturer = "manufacturer"
    power = "power"
    color = "color"
    price = "0000000000"

    def __init__(self):
        self.model = None

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.release}\nПроизводитель: {self.manufacturer}\n"
              f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, model, release, manufacturer, power, color, price):
        self.model = model
        self.release = release
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price


h1 = Auto()
h1.print_info()
h1.input_info("Х7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
h1.print_info()
