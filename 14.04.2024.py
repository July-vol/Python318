# Создать класс Person с двумя разными закрытыми свойствами: Имя и возраст. С использованием
# декоратoра @property, создать возможность изменения этих свойств, а также возможность их удалеия.
#

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть строкой")
        else:
            self.__name = new_name
            print()

    @name.setter
    def name(self, old):
        if not isinstance(old, int):
            raise TypeError("Возраст  должен быть числом")
        else:
            self.__old = old
            print()

    @name.deleter
    def name(self):
        del self.__name


p = Person('Irina', 26)
print(p.__dict__)
p.name = "Igor"
p.old = 31
print(p.name)
print(p.old)
