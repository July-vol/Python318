# print("Hello")
# print("Привет!")

# first_name = "Nikolay"
# print("Hello, " + first_name + "!")
#
# a = 30
# b = "Hello"
# print(type(a))
# print(type(c))
# print(type(b))
#
# a = 5
# print(a, type(a)) # в круглых скобках названия переменной
# b = "Hello"
# print(a, type(a)) # int - целое число, float - вещественное число, записывается через точку 2.8
# print(str(a) + b) # преобразования типов

# a = b
# print(a, id(a))#5
#
# b = 4
# print(b, id(b)) #4
#
# a = b #4
# print(a, id(a))

# a = b = c = 4 # множественное присваивание - если мы хотим нескольким переменным одно значение
# print(a)  # выводятся друг под другом
# print(b)  # выводятся друг под другом
# print(c)  # выводятся друг под другом
# print(a, b, c)  # выводятся в одну строку

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# PI = 3,14
# print(PI)
# PI = 2 # нарушение соглашения программистов
# print(PI)


# a = 1
# b = 2
# print("a:", a)  # 2
# print("b:", b)  # 1
#
# a, b = b, a
# # c = a #c = 1
# # a = b #a = 2
# # b = c #b = 1
# print("a:", a)  # 2
# print("b:", b)  # 1

# print("Строка символов Строка символов Строка символов Строка символов\
# Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов Строка\
#  символов Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов\
#   Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов\
#    Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов\
#    Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов\
#     Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов Строка символов\
#      Строка символов Строка символов Строка символов Строка символов")
# print('Строка символов')

# print("Документ 'file.txt'\n находится по пути \rD:\\folder\\file.txt")  # /r -возврат кoретки на начало строки все
# # затирает, \n -перенос на другую строчку

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!"
# print(s3)  # "Hello, Python"
# print(s3 * 5)
# print("apple")

# print(625664464848484864648484844848484848484826265655)
# print(625664464848484864648484844848484848484826265655)
# print(6.25664464848484864648484844848484848484826265655)
# print(6.25664464848484864648484844848484848484826265655)
# print(6.25664464848484864648484844848484848484826265655)
# # выделить текст + cnt+D - копирует текст на эту же строку

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.получили вещественное число 3.0
# print(6 / 4)  # 1,5

# print(6 // 2)
# print(6 // 4)
# print(6 // 4)  # 3
# print(6 // 4)  # 1
#
# print(6 ** 3)
# print(6 % 4)

# Практика 20.01.2024
# number = (6 + 4) * (5 ** 2 + 7) # Хотим записать выражение, срабатывает правило приоритета: круглые скобки всегда
# # соблюдаются,
# # далее возведение в степень**, потом умножение*, деление/ и остаток от деления%, потом сложение и вычитание
# # срабатывает # слева, потом плюс справа.
# print(number)

# num = 10
# num += 5   # num = num +5
# print(num) #15
# num -= 3     # num = num -3
# print(num) #12

# Дано четырехзначное значение, нужно ввести его в обратной последовательности. Исходное число:9753,
# Обратное число 3579

# num = 4321  # разложить 432
# a = num % 10
# print('a:', a)  # 1
# num = num // 10
# # print(num)
# b = num % 10
# print('b:', b)  # 2
# num = num // 10
# # print(num)
# c = num % 10
# print('c:', c)  # 3
# num = num // 10
# # print(num)
# d = num % 10
# print('d:', d)
#
# print(a*1000+b*100+c*10+d)

# num = 4321  # 43
# print(num)
# res = num % 10 * 1000  # 1000
# num //= 10  # num = num // 10
# res += num % 10 * 100  # 200
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)
#
# num1 = "2.5"  # неявное преобразование типов невозможно
# num2 = 3
# # res = num1 + str(num2) # конкатенация (тип данных преобразования типа str
# # print(res)
# res = float(num1) + num2  # 5.5 (сложение)
# print(res)

# print(int(2.5))  # int отбросил дробную часть -2
# print(round(2.51))  # round(округление до целого числа -3
# print(round(2.51, 2))  # round(округление как вещественного числа, количество символов после точки
# # round -готовая функция
# a = 2.519
# b = round(a)
# print(b, type(b))
# c = round(a, 2)
# print(c, type(c))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")  # Преобразовали к строковому типу дынных age Числовое
# # значение
# print("Меня зовут ", name,". Мне ", age, "лет.", sep="", end=" \n ")  # sep" "-переопределяет поведение запятой,
# # end=" \n " чем заканчивается строка,
# # \n -перенос на другую строчку блок другого кода
# print("Hello")

# name = input("Введите имя: ")
# print("Hello,", name)

# num = int(input("Введите число"))          # int(input("Введите число"))     вложенные функции,
# сначала отрабатывается то что в скобках, потом строковое значение преобразится в значение , и только потом
# ополченное число сохраниться в переменную num power = int(input("Введите cтепень")) num = int(num) power = int(power)
# res = num ** power print("Число", num, "в степени", power, "равно:", res)
#
# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# num3 = int(input("Введите число: "))
# num4 = int(input("Введите число: "))
# sum1 = num1 + num2
# sum2 = num3 + num4
# print(round((sum1 / sum2), 2))


# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5 =6 сработало неявное преобразование данных True всегда преобразуется к 1
# print(b2 + 5)  # 0 + 5 = 5 сработало неявное преобразование данных False преобразовалось к 0
# там где мы ставим условие, переменная должна преобразоваться к булевом типу данных

# print(bool("python"))  # Любое значение будет преобразовываться к True- помимо пустой строки
# print(bool(""))  # если укажем пустую строку-bool("")= В единственном варианте получим False
# print(bool(" "))  # (" ") -пробельный символ даст значение True
# print(bool(" 452"))  # (" число") даст значение True
# print(bool("-452"))  # (" отрицательное число ") даст значение True
# print(bool("4.2"))  # вещественное число даст значение True
# print(bool("0"))  # (" ")   получим False
# print(bool("0.0"))  # ("0.0 ") вещественное число 0.0 получим False
# print(bool("False"))  # (" ")   получим False
# print(bool("None"))  # (" ")   получим False

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)

# print("привет" > "ПРИВЕТ") # 1087 > 1055 буква сравнивается по кодам символов

# print(2 < 4 < 9)  # True  && True  => True
# print(2 * 5 > 7 >= 4 + 3)  # True  >= True  => True
# print(3 * 3 >= 7 >= 2)  # False  && True  => True

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10,5   False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True : True  => True # логическое и and . если и слева и справа True,
# то выйдет True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True : False  => False #если есть хоть где-то False то выйдет
# False print(5 - 3 > 2 and 1 + 3 == 4)  # False : True  => False
# print(5 - 3 > 2 and 1 + 3 > 4)  # False : False  => False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True : True  => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True : False  => True
# print(5 - 3 > 2 or 1 + 3 == 4)  # False : True  => True
# print(5 - 3 > 2 or 1 + 3 > 4)  # False : False  => False # False : False  =>False # логическое or или- если и слева и
# # справа False, то выйдет False
#
# print(not 9 - 5)  # False
# print(not 9 - 9)  # True

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст"))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")
#
# a = 15
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# else:
#     print("b > a")

# if a > b:
#     print("a > b")
# else:
#     print("b > a")


# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a ==b or a==c or b==c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# day = int(input("Введите день недели(цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("Суббота")
#         if day == 7:
#             print("Воскресье")
#
# else:
#     print("Такого дня недели не существует")

# print("1 : да")
# print("2 : нет")
# ll = bool(input("вам 18 лет ?  : "))
# a = True
# b = False
# if ll != 1:
#   print("допуск не разрешен")
# else: ll =1
# print("добро пожаловать")
#
# a=int(input("Введите номер месяца" ))
# if 1<=a<=12:
#     if 1<=a<=2 or a==12:
#         print("Зима")
#     if 3<=a<=5:
#         print("Весна")
#     if 6<=a<=8:
#         print("Лето")
#     if 9<=a<=11:
#         print("Осень")
# else:
#     print("Такого месяца не существует")

# Практика № 3 от 21.01.2024

# crows = int(input('Введите число ворон на ветке: '))
# if 0 <= crows <= 9:
#     print("На ветке", end=" ")
#     if crows == 1:
#         print(crows, "ворона")
#     if 2 <= crows <= 4:
#         print(crows, "вороны")
#     if 5 <= crows <= 9 or crows == 0:
#         print(crows, "ворон")
# else:
#     print("Ошибка ввода данных") # print("На ветке нет ворон")

# password = "admin"
#
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#         case_: (
#             print("Такого значения не существует"))
#
# day = "воскресенье"
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница':
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует")

# a, b = 20, 30 print("a == b" if a == b else "a > b" if a > b else "b > a") #Вложенный цикл if, ограничений нет,
# но больше 3 вкладывать не рекомендуют

# a, b = 20, 0
# print('на ноль делить нельзя' if b == 0 else a / b)

# a = 5
# b = 0
# print(a / b) #На ноль делить нельзя

# try: переводится как попытаться выполнить этот код
# # exceptValueError переводится как исключение
# try:
#     n = int(input("Введите целое число"))
#     print(n * 2)
# except ValueError:
#     (print("Что-то пошло не так"))

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     (print("Нельзя вводить строки или Нельзя делить на ноль"))
# else:  # else отработает, когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # finally отработает в любом случае
#     print("Конец программы")

#
# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# /////ЦИКЛЫ///// либо for while -1 шаг цикла-это итерация

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i= i+1

# i = 10
# while i > 0:
#     print("i =", i)
#     # i -= 1  # i= i-1
#     i -= 2

# Написать программу, выводящую только четные числа из диапазона от 1 до 20

# i = 1
# while i <= 20:
#     if i % 2 == 0:  # вывести только четные числа
#         print("i =", i)
#     i += 1

# Написать программу, которая выводит на экран ряд из звездочек ("*"). Количество вводимых символов указывает
# пользователь. Укажите количество символов:7
# * * * * * * *
#
# n = int(input("Укажите количество символов: "))
#
# print(n * "*")  # 1 вариант
# i = 0  # 2 вариант-если нужно друг под другом
# while i < n:
#     print("*")
#     i += 1

# while n > 0: #3 вариант
#     print("*")
#     n -= 1
# print(n * "*\n")  # 4 вариант

# 5 вариант # Мы хотим чтобы пользователь ввел число +-+-+
# n = int(input("Укажите количество символов: "))
# print(n * "+-")
# print(n * "+" if n % 2 == 0 else n * "-")
# i = 0
# while i < n:
#     print("+" if i % 2 == 0 else "-", end="")
#     if i % 2 == 0:
#         print("+", end="")
# else:
#     print("-", end="")
# i += 1

# n = int(input("Введите начало диапазона: "))
# m = int(input("Введите конец диапазона: "))
# sum1 = 0
# while n <= m:
#     if n % 2 != 0:
#         sum1 += n
#     n += 1
# print(sum1)

# k = input("Введите целое число: ")
#
# while type(k) != int:
#     try:
#         k = int(k)
#     except ValueError:
#         print("Число не целое")
#         k = input("Введите целое число:")
#
# if k % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\n Цикл завершен!")

#
# n = 0
# while True:
#     print(n)
#     if n == 5:
#         break
#     n += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# sum1 = 1
# while True:
#     n = int(input("Введите число: "))
#
#     if n == 0:
#         break
#     sum1 *= n
# print(sum1)

# i = 0
# while i < 10:
#     # if i == 5:
#     #     break #если мы прервали break  то ниже код будет выполнятся
#     # if i == 8:
#     #     print(5 / 0)  # если мы прервали исключением программа дальше выполнятся не будет, до else мы не дошли
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)
# print("Код ниже")


# Практика №4 от 27.01.2024

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1
# Необходимо вывести на экран таблицу умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1
# Необходимо вывести на экран прямоугольник из символов "^":
# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="" )
#         j += 1
#     print()
#     i += 1
# Необходимо вывести на экран прямоугольник из чередующихся символов
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
# Необходимо вывести на экран прямоугольник из чередующихся символов по вертикали
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
# Необходимо вывести диагональ из *:
# с вложенным циклом
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1
# без  вложенного цикла
# i = 0
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1


# For i in collection #forработветтолько с коллекциями
# print(element)

# for i in "Hello!":  # for всегда использует i
#     print(i)
# for color in "red", "blue", "green":
#     print(color)
#

# print(range(9))  # диапазон от 0 до 9
# # range (start -начало, stop- конец, step -какой-то шаг) = вспомогательная функция не относится в чистом виде к for,
# # но может с for работать # start -0 step-1
# for i in range(0, 9, 2):
#     print(i, end=" ")
#
# print()
#
# i = 0
# while i < 9:
#     print(i, end=" ")
#     i -= 2


# print(range(9))
# for i in range(10, -1, -1):
#     print(i, end=" ")
#
# print()
#
# i = 10
# while i < 0:
#     print(i, end=" ")
#     i -= 1


# print(range(2, 9, 2))
# a = 9
# for i in range(0, a + 1, 1):
#     print(i, end=" ")
#
# print()
#
# i = 0
# while i <= 9:
#     print(i, end=" ")
#     i += 1

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# Ввести целые числа в диапазоне от 10 до 100 у которых есть две одинаковые цифры
# for i in range(10, 100):
#     # if i % 11 == 0:
#         if i // 10 == i % 10:
#             print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("конец цикла")


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("---")

# Задача: вывести прямоугольник из звездочек, ширину и высоту задает пользователь. Введите ширину прямоугольника:12,
# введите высоту прямоугольника 4.


# d = hp
# print(d)
#
# num = [i for i in range(30) if i % 2 ==0] print(num) class 'list' -Список, в Питоне есть такое понятие как список,
# но нет такого понятия как массив, потому что содержит в себе разные типы данных

# nums = [8, 3, 9, 4, 1, "Hello", True]
# print(nums)
# # print(type(nums))
# # print(nums[0])
# # print(nums[2])
# # print(nums[-1])
# # print(nums[6])
# # print(nums[-2])
# # print(nums[-7])
# nums[1] = 256
# nums[2] += 100
# print(nums)
# # for i in nums:
# #     print(i)
# print(len(nums))


# s = [1, 3, 5]
# print(s)
# print(type(s))
# s1 = list("Hello")
# print(s1)
# print(type(s1))
# s2 = s1 + s
# print(s2)
# s3 = s * 2  # (число должно быть целое-не вещественное)
# print(s3)

# n = list(range(2, 10, 3))
# print(n)


# a = [0 for i in range(5)]
# print(a)
#
# a1 = [i ** 2 for i in range(1, 25)]  # только 1 какое-то действие
# print(a1)

# a2 = [i * 3 for i in "Python"]  # только 1 какое-то действие
# print(a2)


# Практика №5 от 28.01.2024
# Задача №1
# длинная запись
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)  # [0,0]
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# короткая запись

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# Задача №2
# Посчитать в списке сумму всех отрицательных элементов (список вводит пользователь)

# sum1 = 0
# a = [int(input("->")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if a[i] < 0:
#         sum1 += a[i]
#         print(sum1)

# Задача №3

# s = list(range(10, 100, 10))
# print(s)
#
# for i in range(len(s)):
#     print(s[i], end=" ")
# print()
# for i in s:
#     print(i, end=" ")"

# Задача №4

# В списке на 20 элементов посчитать количество четных элементов и найти сумму нечетных элементов
# Список: [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
# Количество четных элементов: 10
# Сумма нечетных чисел: 300

# n = list(range(21, 41))
# print(n)
# count = s = 0  # 0 попадет в переменную s и в переменную count одновременно
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print(" Количество четных элементов списка:", count)
# print("Сумма нечетных чисел:", s)

# Задача №5

# Дан список чисел. Введите все элементы списка, которые больше предыдущего элемента. Введите элементы списка.
# n = 6
# -> 2
# -> 9
# -> 4
# -> 6
# -> 3
# -> 5
#
# 9 6 5

# n = list(range(21, 41, 3))
# a = 2
# print(n[a])
# print(n[a - 1])

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])

# Задача №6

# Необходимо найти среднее арифметическое всех ненулевых элементов введенного списка
# n = 5
# -> 6
# -> 3
# -> 0
# -> 8
# -> 2
# Среднее арифметическое:4.75

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
#
# s = count = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#         count += 1
# print(s/count)

# Задача №7
# Взять список и поменять первый и второй элемент в списке местами
# a = [7, 9, 2, 1, 17]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Cрез - список, у которого мы можем передать от 1 до 3 параметров, как минимум должно быть одно двоеточие
# s = [5, 9, 3, 7, 1, 8]
# print(s, id(s))
# print(s[1:3])
# print(s[:3])
# print(s[3:])
# print(s[:])
# print(s[3:1:-1])
# print(s[0:5:1])
# print(s[3:1:-1])
# print(s[5:0:-1])
# print(s[::-1], id(s[::-1]))
# print(s[6:22], id(s[6:22]))

# Задача №8
# Создать срезы списка
# [1, 2, 3, 4, 5, 6, 7]
# lst = list(range(1, 8))
# print(lst[:])
# print((lst[::-1]))
# print(lst[1::2])
# print(lst[::1])
# print(lst[6::])
# print(lst[-1::])
# print(lst[3::4])
# print(lst[4::])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "Hello"
# # print(st)
# # print(st[::-1])
#
# a = 54, 56, 78, 99
# # print(a)
# # print(a[:])
# for i in a:
#     print(i)

# Методы списков: append, dir(list)
# Задача №9
# s = [9, 5, 6, 3, 7, 4]
# print(s)
# s.append(8)  # Добавляет элемент в конец списка
# # s.append("add")
# print(s)
# s.extend([8, 2, 20, 1, 2])  # Добавляет набор элементов в конец списка
# # s.extend("add")
# print(s)
# s.insert(3, 100)  # Добавляет элемент (второй параметр) по заданному индексу(первый параметр)
# print(s)
# insert -может добавить куда угодно, кроме последнего индекса

# Задача №10

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# s = []
# n = int(input("Введите кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 2 == 0:
#         s.append(x)
#     # s.insert(0, x) [1, 5, 9]
# print(s)

# Задача №11
# Программа должна просить пользователя заданное количество раз ввести число кратное 3, проверять
# действительно ли оно кратно 3. Если да, то добавлять в список, если нет то выводить пользователю на экране
# *введенное пользователем число* не делится на 3 без остатка.
# Количество элементов списка: 6
# Введите число кратное 3: 9
# Введите число кратное 3: 3
# Введите число кратное 3: 5
# 5 не делится на 3 без остатка.
# Введите число кратное 3: 8
# 8 не делится на 3 без остатка.
# Введите число кратное 3: 12
# Введите число кратное 3: 1
# 1 не делится на 3 без остатка.
# [9, 3, 12]

# s = []
# n = int(input("Кол-во элементов списка:"))
#
# for num in range(n):
#     x = int(input("Введите число кратное 3:"))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         # if x % 3 != 0:
#         print(x, "не делится на 3 без остатка")
# #     else:
# #         s.append(x)
# print(s)

# Задача №12
# Найти элементы, которые присутствуют в обоих списках
#
# a = [5, 9, 2, 1, 4, 3]
# d = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]
#
# for i in a: # 4
#     for j in d: # 1
#         # if i in c:
#         # continue # Прерывает текущую итерацию цикла, но продолжает цикл дальше
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# s = []
# for el in a:
#     if el in d and el not in s:
#         s.append(el)  # [ 2, 1, 4, 3]
# print(s)

# Задача №13
# # Напишите функцию, которая создает комбинацию двух списков таким образом:
# # [1, 2, 3] (+) [11, 22, 33]->[1, 11,2, 22,3,33]
# # Результат
# # [1, 11, 2, 22, 3, 33]
# a = [1, 2, 3, 33, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# # if len(b) > len(a):
# #     for i in range(len(a)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(a), len(b)):
# #         c.append(b[i])
# # else:
# #     for i in range(len(b)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(a), len(b)):
# #         c.append(a[i])
# print(c)

# Задача №13
# Метод Remove

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# t = a.remove(9)  # удаляет элемент по значению
# print(a)
# last = a.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# print(last)
# second = a.pop(0)  # удаляет элемент по индексу
# print(second)
# print(a)
# a.clear()  # либо удаляет все элементы из списка либо очищает список
# print(a)
# num = a.count(9)  # Количество заданных значений в списке
# print(num)
# ind = a.index(19)  # Возвращает индекс элементов по заданному значению
# print(ind)
# ind2 = a.index(9, 2, -1)  # Возвращает индекс элементов по заданному значению
# print(ind2)
# num = 4
# if num in a:
#     print(a.index(num))

# Задача №14
# Метод Reverse
# a = [7, 9, 2, 9, 1, 17, 9]
# a.reverse()
# print(a)

# Задача №15
# Метод Copy
# a = [7, 9, 2, 9, 1, 17, 9]
# b = a.copy()  # Копирует список, чтобы переменные не ссылались на 1 ячейку в памяти
#
# print("a =", a)
# print("b =", b)
# a.append(4)
# b.append(120)
# print("a =", a)
# print("b =", b)

# Практика №6 от 03.02.2024
# Задача №14
# Метод "Sort"
# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# a.sort(reverse=True)  # сортировка элементов списка по возрастания
# print(a)

# s = ["Виталий", "Сергей", "Анна", "Антон", "Александр"]
# print(s)
# # s.sort(key=len, reverse=True)  # сортировка элементов списка по алгоритму заданной функции
# # print(s)
# # print(len(s))
# # print(len(s[0]))
#
# lst = sorted(s, key=len, reverse=True)
# print(lst)
# print(s)

# Генерация случайных данных
# Перед импортом (модулем) нельзя ничего ставить !!!!
# import random


# print(random.random())
# print(random.randint(2, 9))  #9 Включительно
# print(random.randrange(3, 9, 2)) #9 не включительно
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5), 2))

#
# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# # random.shuffle(s)
# print(random.choice(s))  # Возвращает случайным образом 1 элемент
# print(random.choices(s, k=3))  # Возвращает случайным образом  элемент в виде списке по параметру к


# lst = [random.randint(0, 100) for i in range(10)]  # Генерирование списка  из случайных чисел
# print(lst)


# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# print(len(s))  # функция нахождения длинны списка
# print(sum(s))  # функция нахождения с суммы чисел списка
# print(max(s))
# print(min(s))


# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# print("Max:", max(lst))
# s = sorted(lst, reverse=True)
# print(s)

# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# mux = max(lst)
# print("Max:", max(lst))
# list.remove(mux)
# list.insert(0, mux)
# print(lst)

# x = list("1a2b3c4d")
# print(x)
# print("a" not in x)
# print("I" not in x)
# s = "c1"
# if s in x:
#     print("Такой элемент в списке присутствует")
# else:
#     print("Такой элемент в списке отсутствует")

# lst = []
# if not lst == 0: # lst == [] #len(lst) == 0
#     print("Cписок пустой")
# print(bool(lst))

# n1 = int(input("Введите размер 1 списка: "))
# n2 = int(input("Введите размер 2 списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# # c = []
# # c = a + b
# # print(c)
# # c = []
# # for i in range(len(a)):
# #     if a[i] not in c:
# #         c.append(a[i])
# # for i in range(len(b)):
# #     if b[i] not in c:
# #         c.append(b[i])
# # print(c)
# # c = []
# # for i in range(len(a)):
# #     if a[i] in b and a[i] not in c:
# #         c.append(a[i])
# # print(c)
#
# c = [min(a), min(b), max(a),max(b)]
# print(c)

# Задача
# Заполнить список уникальными случайными числами

# n1 = int(input("Введите размер списка: "))
# # a = [random.randint(0,10)for i in range(n1)]
# a = []n
# while len(a) != n1:
#     n = random.randrange(n1)  # от 0 до 10
#     if not in a:
#         a.append(n)
# print(a)

# Вложенный список
# m = [
#     [1, 2, 3, 4, 55],  #
#     [5, 6, 7, 8, 33, 34],  #
#     [9, 10, 11, 12]
# ]
# # print(m)
# print(m, end="\n\n")
#
# # print(len(m))
# # print(m[1][2])
# # s = ["Hello", "World"]
# # print(s[1][2])
#
# for row in range(len(m)):  # 0 1 2
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()

# Задача №4 Возвести каждый элемент матрицы в квадрат
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# for row in m:
#     for x in row:
#         print(x ** 2, end="\t\t")
#     print()
#
# w, h = 5, 3
# matrix = [[random.randint(1, 20) for x in range(w)] for y in range(h)]
# matrix = [[0 for x in range(w)] for y in range(h)]
# matrix = []
# for y in range(h):  # 3
#     new_row = []
#     for x in range(w):
#         new_row.append(0)  # new_row = [0,0,0,0]
#         matrix.append(new_row)
#
# for row in matrix:
#     for x in row:
#         print(x ** 2, end="\t\t")
#     print()
#
# for x, y, z in [[1, 2, 5], [3, 2, 4], [5, 5, 6], [7, 4, 8]]:
#     print(z, ") ", x, " + ", y, " = ", x + y, sep="")
#     # print(x[2], ") ", x[0], " + ", x[1], " = ", x[0] + x[1], sep="")


# Практика №7 от 04.02 .2024
# Любые математические исчисления находятся в методе - math
# import math
#
# num1 = math.sqrt(4)
# num2 = math.pi
# num3 = math.ceil(2.2)  # Делает округление в большую сторону не зависимо от дробной части
# num4 = math.floor(3.4)  # Делает округление в боль сторону не зависимо от дробной части
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# # когда мы импорту можем дать 2 имя (псевдоним)
#
# import math as m
# num3 = m.ceil(3.25)
# num4 = m.floor(3.4)
#
# print(num3)
# print(num4)


# from math import *

# num3 = ceil(3.25)
# num4 = floor(3.4)
#
# print(num3)
# print(num4)

# Ограничение на количество в модуле импорта нет
# from math import ceil, floor
#
# num3 = ceil(3.25)
# num4 = floor(3.4)
#
# print(num3)
# print(num4)

# from math import ceil as c, floor as f
#
# num3 = c(3.25)
# num4 = f(3.4)
#
# print(num3)
# print(num4)

# Задача №1
# Пользователь вводит радиус окружности. Найдите длину окружности
# Введите радиус окружности: 9
# Длинна окружности: 56,55

# from math import pi
# radius = int(input(" Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * radius, 2))
#
# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
# second = time.time()
# print(second)
# s = 1713709474
# local_time = time.ctime(s)
# print(local_time)
#
# res = time.localtime()
# print(res)
# print("0" + str(res.tm_mday)if res.tm_mday < 10 else "", ".", res.tm_mon, ".", res.tm_year, sep="")
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(s)))
# print(time.strftime("Сегодня: %B %d, %Y, %A"))

# start = time.time()
# pause = 5
# print("Программа запущена...")
# time.sleep(pause)
# print("Пауза была", pause, "секунд")
# finish =time.time()
# res = finish - start
# print(res)

# start = time.monotonic() # делает подсчет времени более точно
# pause = 5
# print("Программа запущена...")
# time.sleep(pause)
# print("Пауза была", pause, "секунд")
# finish =time.monotonic()
# res = finish - start
# print(res)

# ////ФУНКЦИИ///// Функция это программный код, который можно вынести в отдельный блок так называемую функцию,
# и вызывать ее неограниченное количество раз с использованием разных параметров. функция будет вызываться там,
# где мы к ней обратились. Бывает обычная и лямда выражение. используется слово def -от слова defound
# -определять.Функия находится выше, че мы ее вызываем

#
#
# def hello(name, age):
#     print("Мне", age, "Меня зовут", name)
#
#
# hello("Irina", 28)
# hello("Igor", 19)

# def get_sum(a, b):
#     print("Сумма: ", end="")
#     return a + b
# n = 2
# m = 5
# print(get_sum(n, m))
# res = get_sum(n, m)
# print(res)
# print(res + 5 - 2)
# c =3
# d = 5
# get_sum(c, d)

# def maximum(one, two):  # Функция нахождения максимального числа
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 6))  # 9
# print(maximum(9, 16))  # 16


# Задача №2
# Написать функцию нахождения разности, если а > b  a < b, а и b Пользователь вводит с клавиатуры
# а = 5
# b = 9
# Результат: 15

# a = int(input("Введите 1 число: "))
# b = int(input("Введите 2 число "))
#
# def raznost(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
# print("Результат:", raznost(a, b))

# Задача №3
# Вывести  куб всех чисел от 1 до 10 (функция, которая принимает один параметр и возвращает значение)

# 1 в кубе = 1
# 2 в кубе = 8
# 3 в кубе = 27
# 4 в кубе = 64
# 5 в кубе = 125
# 6 в кубе = 216
# 7 в кубе = 343
# 8 в кубе = 512
# 9 в кубе = 729
# 10 в кубе = 1000

# def cub(a):
#     return a * a * a
#
# for i in range(0, 11):
#     print(i, "в кубе =", cub(i))
#

# Задача №4 Напишите функцию change(lst), которая  принимает список и меняет местами  его первый и последний элемент.
# В исходном списке минимум 2 элемента. Исходные данные: [1, 2, 3] [9, 12, 33, 54, 105] ['с', 'л', 'о',
# 'н'] Результат: [3, 2, 1] 105, 12, 33, 54, 9] ['н', 'л', 'о',  'с']

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]  # последний индекс в нашем списке [2],берем универсальный [-1]
#     end = lst.pop()  # Удалили последний элемент из списка
#     start = lst.pop(0)  # Удалили первый элемент из списка
#     lst.insert(0, end)  # Добавляем элемент в начало списка
#     lst.append(start) # Добавляем элемент в конец списка
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# print(maximum(9, 6))  # 9 True
# print(maximum(9, 16))  # 16 False
#
# if maximum(9, 16):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")


# /////////Проверка надежности пароля/////////

# def check_password(password):
#     has_lower = False
#     has_upper = False
#     has_num = False
#
#     for ch in password:
#         if "a" <= ch <= "z":  # 97<= 50 <= 122
#             has_lower = True
#         if 'A' <= ch <= "Z":
#             has_upper = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_lower and has_upper and has_num:
#         return True  # else: можно не писать  return -отрабатывает вместо else
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это не надежный пароль")


# ////////////////// Практика 10.02.2024//////////////////

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))  # 1, 5, 2, 1 = 9
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))  # 1, 5, 0, 2 = 9

# Задача № 1
# Написать функцию,которая имеет количество символов = 20  и символ '-' в качестве аргументов по умолчанию
# и выводит на экран набор произвольных символов заданной длины. ------------------------

# def set_param(c=20, s="-"):
#     print(s * c, end="")
#     print()
#
#
# set_param()
# set_param(7)
# set_param(20, "#")
# set_param(s="#") # s="#" - именованный параметр
# set_param(15, "+")
# set_param(s="*", c=10)

# Задача №2
# Написать функцию, принимающую некоторое целое число вычисляющую по умолчанию сумму его четных цифр.
# Предусмотреть возможность изменения поведения функции таким образом,
# чтобы она также могла вычислять сумму нечетных чисел
# Тестовые значения:
# 9874023б, even_sum=14,add_sum = 19
# 38271, even_sum =, add_sum = 11
# 123456789, even_sum 20, add_sum = 25

# Сумма четных циф
# 14
# 10
# 20
# Сумма нечетных цифр:
# 19
# 11
# 25
#
# def digits_sum(n, even=True):  # even=False
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         # print(cur_digit)
#         if even and cur_digit % 2 == 0:  # even=True
#             s += cur_digit
#         if not even and cur_digit % 2: #even=False
#             s += cur_digit
#         n //= 10  # n=n//10
#     return s
#
#
# print("Сумма четных цифр")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
#
# print("Сумма нечетных цифр")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name: ", name, "\nAge", age)
#
#
# display_info("Irina", 23)
# display_info(23, "Irina")
# display_info(age=23, name="Irina")
# # display_info("Igor", age=23, name="Irina")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)  # True
# print(lt1 is lt2) # оператор is ссылаются ли 2 переменные  на 1 и от же адрес в памяти данных -lt1,lt2 -нет
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)  # оператор is ссылаются ли 2 переменные  на 1 и от же адрес в памяти данных - a, b -да
# a = a + "_new"
# print(a)
# print(id(a))
# print(id(b))
# Не могут разные строки быть в однй и той же ячейке памяти.
# Также и переменным как только мы присваиваем переменной другое число,
# она сразу ссылается на другую ячейку памяти
# Если мы изменять будем что-то в списке, то адрес списка останется тот же самый

# lt1 = [1, 20, 3]
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))
# lt1[1] = 50
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))


# //////типы данных///////
# Неизменяемый типы данных - int, str, float, bool, tuple
# Изменяемый тип данных - list

# Кортеж(tuple) -Неизменяемый список

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())  # 72 104
# print(tpl.__sizeof__())  # 48 48
# print(tpl[2])
# print(type(tpl))

# ///////Функция явного преобразования типов ////typle()/////
# a = 1, 5, 9, 7, 8 # (5,) 5, (1, 5, 9, 7, 8)
# print(a, type(a))
#
# # b = tuple("Hello")
# # # b = tuple(["Hello", "World"]) # Кортеж в круглых скобках
# # # не может передавать несколько аргументов,
# # # только через преобразование типов
# #
# # print(b, type(b))

# a = (5, 9, 7, 3, 4)
# print(a[1:3])
# print(a[-1])
# print(a[4])

# from random import randint
# tpl = tuple(i for i in range(5))
# tpl = tuple(input("-> ") for i in range(5))
# tpl = tuple(randint(1, 100) for i in range(5))
# print(tpl)


# Задача №3
# Заполните кортеж  из 10 элементов степенями двойки от 1 до 12
# (2,4,8,16,32,64,128,256,512,1024,2048,4096

# from random import randint
# tpl = tuple(2 ** i for i in range(1, 13))
# print(tpl)

# t1 = tuple("Hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
#
# print(t3)
# # print(t3 * 2)  # Будет всегда ошибка если умножаем не на целое число
# print(t3.count("l"))
# # print(t3.index("l", 4, -2))
# sym = "o"
# # if sym in t3:
# #     print(t3.index(sym))
# # else:
# #     print("Такого символа нет!")
# try:
#     print(t3.index("sym", 4, -2))
# except ValueError:
#     print("Такого символа нет в заданном диапазоне!")

# Задача №4
# Функция "slicer" на вход принимает кортеж и случайный элемент
# Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем
# и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе -вернуть простой кортеж. Если элемент встречается только 1 разб
# то вернуть кортеж, который начинается с него и идет до конца исходного
# Тесты:
# (1, 2, 3),8)
# (1, 8,3,4,8,8,9,2),8)
# (1,2,8,5,1,2,9),8)
# ()
# (8,3,4,8)
# (8,5,1,2,9)

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)# или +1
#             return tpl[first:second] # или+ 1
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()  # return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# //////Второй вариант с одной строкой  и двумя срезами
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()  # return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# Задача №5 //// Домашнее задание/////
# Заполните 1 кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от -5 до 0.
# Для заполнения кортежей числами напишите одну функцию.
# Объедините
#  кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа соunt() определите в нем количество нулей.
# Выведите на экран третий кортеж и количество нулей в нем.
#
# (1,3,3,5,4,4,4,4,2,0)
# (-2,-3,-3,0,-1,0,-2,0,-5,-1)
# (1,3,3,5,4,4,4,4,2,0,-2,-3,-3,0,-1,0,-2,0,-5,-1)
# 0 = 4

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["Hello", "world"])  # Изменить элемент кортежа нельзя,
# # а изменить объект в элементе(списке) кортежа можно,
# # при чем адрес ячейки останется тот же
# print(t, id(t))
# t[4][0] = "hi"
# t[4].append("new")
# print(t, id(t))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# print(x, y, z)
# ////более просто/////распаковка кортежа
# t = 1, 2, 3 # Круглые скобки можно не писать
# x, y, z = t  # Распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married  # Когда мы возвращаем больше одного значения,
#     # возвращаем на самом деле кортеж, в котором лежит больше 1 элемента
#
#
# # user = get_user()  # Вызываем функцию,и сохраняем значение в переменную, в которой хранится кортеж из трех клементов
# # более сокращенный вариант с распаковкой
# first_name, year, married = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(first_name, year, married)


# ///////////////Практика 17.02.2024//////////////////
#
# name = "Igor"
#
# if name:
#     print("Name:", name)
#     name = "Marina"
# else:
#     print("ELSE")
# print(name)

# name = "Igor"
#
# for i in range(5):
#     print(i, end=" ")
#     name = "Marina"
# print()
# print(name)

# name = "Igor"
# def func():
#     print("Hello")
#     name = "Marina"  # локальная переменная наала создаваться когда функция появилась,
#     # и перестала существовать, когда функция закончилась
#
#
# func()
# print(name)

# lst = [1, 2, 3, 4, 5]  # Преобразование списка  в кортеж, кортежа в список
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst2 = list(tpl)
# print(lst2)
#
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\n Страна: ", country_name,", население = ", country_population, cities, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep=" ")


# \\\\\\\\\\Множества/////////////////{Set} - непорядоченная коллекция,
# хранит только уникальные значения, -изменяемы тип данных через методы


# s = {"red", "blue", "green", "blue"}
# print(type(s))
# print(s)
# print(len(s))
#
# for i in s:
#     print

# a = {} словарь
# print(a,type(a))

# a = set("Hello")
# print(a, type(a))

# s = {x * x for x in range(10)}  # Генератор множеств
# s = {input("->") for x in range(3)}  # Генератор множеств
# s = {randint(20, 50) for x in range(10)}  # Генератор множеств
# print(s)

# s = {"red", "blue", "green"}
# print("green" in s)
# print("green" not in s)


# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # lt = [i for i in lst if 'a' in i]
# lt = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst]
# print(lt)

# for i in lst:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])

# s = {"red", "blue", "green"}
# print(s)
# s.add("black")  # один метод для добавления элемента во множества
# print(s)
# s.remove("black")  # Удаляет элемент по значению (KeyError)
# print(s)
# # s.remove("pink")  # KeyError
#
# color = "green"
# if color in s:
#     s.remove(color)
# print(s)
# s.discard("pink")  # Удаляет элемент по значению, не выбрасывает исключение, если элемента не существует
# print(s)

# color = s.pop()  # Удаляет первый элемент из множества
# print(s)
# print(color)
# s.clear()  # Очищает множество
# print(s)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a + b #Сложить между собой set множества не можем оператором +
# c = a.union(b)
# c = a | b
# a |= b
# c = a & b
# a &= b
# c = a - b
# a ^= b
# print(c)
# print(a)


# n = 5
# m = 6
# v = n + m
# print(v)
# n += m
# print(n)


# Задача №1
# Дан набор множеств: {1,2}, {3}, {4,5}, {3, 2, 6}, {6}, {7, 8}, {9,8}.
# Найти количество уникальных элементов во всех множествах.
# Найти минимальный и Максимальный элементы среди них.
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Unis elems count: 9
# min elem: 1
# max elem: 9

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6| s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# Задача №2.
# Найдите общие буквы в двух разных строках
# Введите первую строку: Hello
# Введите вторую строку: "How are you"
# Общими буквами являются:
# е о Н
#
# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# Задача №3.
# Марина, Женя и Света занимаются рисованием, а Костя, Женя и Илья - дополнительно посещают уроки музыки.
# Определите, сколько человек занимается только одним видом искусства, и выведите список их имен.
# Ученик, занимающийся в обоих кружках, решил бросить занятие рисованием.
# Произведите соответствующие измненения.

# Only one hobby: {'Sveta', 'Kostya', 'Ilya', 'Marina'}
# Both hobbies: {'Jenya'}
# Drawing: {'Sveta', 'Marina'}

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobbies = drawing & music
# print(both_hobbies)
# drawing = drawing - both_hobbies
# print(drawing)
#
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)
# print(a < b)
# print(a > b)
# print(a != b)

# a = [9, 8, 6, 5, 8, 7, 5, 5, 4, 4, 7, 7, 8, 7, 8, 7, 8, 9, 5, 4]
# print(a)
# s = set(a)
# print(s)
# a1 = list(s)
# print(a1) #только уникальные элементы

# s = frozenset("Hello")
# s = frozenset(["Hello", "World"]) #frozeset -поместить и получить неизменяемые данные
# s = frozenset([9, 8, 6, 5, 8, 4, 2])
# print(s)

# \\\\\\\\\\СЛОВАРИ(dic)///////////
# у словарей нет индексов, у словарей есть ключи, словари записываются с фигурными скобками{}

# # lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "there ": 3}
# lst[1] = 200
# d["two"] = 200
# print(lst)
# print(d["two"])

# d = {"one": 1, "two": 2}
# print(d, type(d))
#
# d1 = {"one": 1, "two": 2}
# print(d1, type(d1))
#
# d1 = dict
# var = {[1, 2, 3]}  # словарь преобразовываем в словарь
# print(d1, type(d1))
#
# d1 = dict(one=1, two=2) # в dict не можем передать какой-то список
# print(d1, type(d1))
#
# d2 = dict([("a", 1), ("b", 2)]) # в dict не можем передать какой-то список
# print(d2, type(d2))

# ///////////////Практика 18.02.2024////////////////// Ключами могут быть только неизменяемые типы данных. Ключами не
# могут быть: списки, множества -set, и словарь в виде ключа. Значение может быть любой тип данных
#  В Питоне неявное преобразование бывает только с булевыми типами данных
#  больное место у словаря - несуществующий ключ
# Ключ в виде кортежей встречаются крайне редко, с булевыми значениями тоже. в основном тип числа или строки
# преобразование на замену значений работает только с булевыми типами данных
# Ключ остается первый, значение в словаре последнее.
# d = {0: "test.txt", "one": 45, (1, 2.3): "Кортеж", "Список": [2, 3, 6, 7], True: 1, False: 0, 1: "один"}
# print(d)
# key = 45 # удаление можем закрыть -if или try\except
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + str(key) + " нет в словаре")
# # if key in d:
# #     del d[key]
#
# print(d)

# # по умолчанию когда мы проходимся по словарю мы получаем ключ
# d["ne"] = "Новое значение"
# print(d)
# for key in d:  # Переменная в for это всегда ключ
#     print(key, ":", d[key])

#
# print(d)
# print("one" in d)  # Проверка существования словаря в ключе
# print("ne" in d)  # Проверка существования словаря в ключе -сли ключа нет, вернет просто значения True или False,
# # как показатель присутствует ключ в словаре или нет


# print(d)
# print(d[0])  # в словарях не индекс, а ключ, навести на переменную d будет подсвечивать тип данных dict
# print(d[1, 2.3])  # в словарях не индекс, а ключ, навести на переменную d будет подсвечивать тип данных dict
# print(d[False])  #
# print(d[1])  #
# print(d[True])  #

# Задача №1
# Дан словарь с числовыми значениями. Необходимо  их все перемножить и вынести на экран.
# {'x1':3, 'x2': 7, 'x3': 5, 'x4': -1}
# -105

# d = {
#     'x1': 3,
#     'x2': 7,
#     'x3': 5,
#     'x4': -1
# }
# a = 1
# for key in d:
#     a *= d[key]
#
# print(a)

# Задача №2
# Предложите пользователю ввести названия четырех овощей и сохраните их в словаре с числовыми индексами, начиная с 1.
# Выведите содержимое словаря  с указанием индексов и элементов.
# Спросите пользователя, какой элемент он хочет исключить,
# и удалите его из списка. Выведите содержимое словаря.

# -> картофель
# -> морковь
# -> баклажан
# -> лук
# {1: 'картофель', 2: 'морковь', 'баклажан', 'лук'}
# Какой элемент исключить: 3

# d = dict()  # {}
# d[1] = input('->')
# d[2] = input('->')
# d[3] = input('->')
# d[4] = input('->')


# d = {i: input('->') for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)


# Задача №3
# Написать программу, в которой хранятся данные о товарах, их количестве и цене.
# При запуске программы эта информация выводится на экран.
# дальше пользователю должно предлагаться вводить номера товаров и их новое количество.
# Изменение данных должно завершатся, Если пользователь вводит специально оговоренный символ (например, 0).
# После этого все данные о товарах должны снова выводится на экран.
# Core-i3-4330, 9 шт., по 4500 руб.,
# Core i5-4670, 3 шт., по 8500 руб.,
# AMD FX-6300, 6 шт., по 3700 руб.,
# Pentium G3220, 8 шт., по 2100 руб.,
# Core i5-3450, 5 шт., по 6400 руб.,1
#
# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], " руб.", sep="")

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# # for key in d.keys():
# # for key in d.values(): # хорошо сохраняет значения для цикла
# for key, value in d.items(): #Обращаясь кey и value получим ключи и значения
#     print(key, "->", value)
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
# print("D =", d, id(d))
# print("D2 =", d2, id(d2))
#
# d['b'] = 5
# d2['e'] = 7
# print("D =", d, id(d))
# print("D2 =",d2, id(d2))

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('b1', "Такого ключа не существует")  # метод get не выбрасывает исключение, он просто возвращает нам
# # значение none, что такого значения ключа не существует.
# # Но тут есть возможность вторым параметром передать либо текст, либо число
# # - например:"Такого ключа не существует"), вместо значения none
# print(value)
# item = d.setdefault('c', 5)
# print(item)
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('w', "Такого ключа не существует")
# print(item)
# print(d)
# item2 = d.popitem()  # Удаляет последний ключ и значение, и возвращает эти элементы в виде кортежа
# print(item2)
# print(d)
# d.clear()
# print(d)

# d = dict.fromkeys(['a'], ['b']), 100
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = [('r', 7), ('q', 9)] # Из списка кортежей словарь преобразоваться может
# # d2 = {'r': 7, 'q': 9}
# # print(list(d2.items()))
# # d.update(d2)
# # d3 = d.copy()
# # d3.update(d2)
# d |= d2
# print(d)


# Задача №4
# Дан словарь  {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}. Создать новый словарь,
# который будет содержать только  имя и зарплату сотрудника,а затем удалить эти значения их исходного словаря.
# {'age': 25, 'city': 'New York'}
# {'name': 'Kelly', 'salary': 8000}
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)

# Задача №5 *имя ключа переименовывается только через удаление метод "pop", по другому не получается
# Дан словарь  {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}. Переименовать ключ 'city' в 'location'
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New York'}
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print(d)
# d['location'] = d.pop('city')
# print(d)

# Задача №6
# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# print(d)
# # new_d = {key: value for key, value in d.items()}
# new_d = {key: value for key, value in d.items() if value <= 2}
# # Срезов в словарях нет. Можно вывести через условие, привязываясь именно к значению (value),
# # по словарю мы можем пройти как по коллекции, доходя до определенной итерации будет останавливать цикл
# print(new_d)

# Задача №7
# Создать следующий объем данных, представляющий объемы продаж по регионам, в виде двумерного словаря:
# Запросите у пользователя имя и регион. Выведите соответствующие данные. Запросите у пользователя имя и регион того
# значения, которые он хочет изменить, и позвольте скорректировать объем продаж. Выведите объемы продаж по всем
# регионам для имени, выбранного пользователя.
# John:
# N: 3056
# S: 8463
# E: 8441
# W: 2694

# Tom
# N: 4832
# S: 6786
# E: 4737
# W: 3612

# Anne
# N: 5239
# S: 4802
# E: 5820
# W: 1859


# Fiona
# N: 3904
# S: 3645
# E: 8821
# W: 2451

# Имя: Tom
# Регион: W
# 3612
# Новое значение: 7000
# {"N": 4832, "S": 6786, "E": 4737, "W": 7000}
#
# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
# # print(sales)
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y])
# person = (input("Имя: "))
# region = (input("Регион: "))
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# Домашнее задание
# Дан словарь:  {"emp1": {"name": "John", "salary":  7500}, "emp2": {"name": "Emma", "salary":  8000},
# "emp3": {"name": "Brad", "salary":  6500}}. Измените значение зарплаты Бреда с 6500 до 8500.
# {"name": "Brad", "salary":  6500}
# 6500
# emp1
# name: John
# salary: 7500

# emp2
# name: Emma
# salary: 8000

# emp
# name: Brad
# salary: 8500


# d = {
#     "emp1": {"name": "John", "salary":  7500},
#     "emp2": {"name": "Emma", "salary":  8000},
#     "emp3": {"name": "Brad", "salary":  6500},
# }
# print(d['emp3'])
# print(d['emp3']['salary'])
# d['emp3']['salary'] = 8500
#
# for i in d:
#     print(i)
#     for j in d[i]:
#         print("\t", j, ":", d[i][j])
# for i in d:
#     print(i)
#     for j, v in d[i].items():
#         print("\t", j, ":", v)

# \\\\\\\\\\ПРАКТИКА 24.02.2024\\\\\\\\\\\\\\\\\\\\\\\

# Готовая функция "zip", ограничений нет сколько элементов мы преобразовываем, главное в переменных чтобы было
# одинаковое количество элементов
#
# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = (2.9, 3.7, 9.2)
# # d = dict(zip(a, b))
# # d = list(zip(a, b))
# d = tuple(zip(a, b, c))
# print(d)

# one = {'name': "Igor", 'surname': "Doe", 'job': "Consultant"}
# two = {'name': "Irina", 'surname': "Smith", 'job': "Manager"}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)
# #

# lt = [('Dec', 12), ('Jan', 1), ('Feb', 2)] # благодаря zip произошла распаковка кортежа,  а "*"  дала избавится от
# # квадратных скобок
# a, b = zip(*lt)
# print(a)
# print(b)

# a = [1, 2, 3]
# b = [* a, 4, 5, 6] #Добавили спиcок "а" в список "в", а * помогла избавится от квадратных скобок
# print(b)
# print(len(b))
#
# first = {'one': 1, 'two': 2}
# second = {'there': 3, 'four': 4}
# print({**first, **second})  # 'one': 1, 'two': 2,'there': 3, 'four': 4 - получили 1 словарь из двух
# for k, v in {**first, **second}.items():
#     print(k, "=>", v)

# colors = ['red', 'green', 'blue']
# # i = 1
# # for color in colors:
# #     print(i, ")", color)
# #     i += 1
# # for num, val in enumerate(colors, 1):  # функция автоматической нумерации enumerate, start=1 - с какой цифры начать
# #     # нумерацию
# #     print(num, ")", val, sep="")

# Задача №1
# Пользователь вводит данные о количестве студентов, их фамилии, имена и балл дл каждого.
# Программа должна определить средний бал и вывести фамилии и имена студентов, чей балл выше среднего.
# Количество студентов: 5
# 1-й студент: Игорь
# Балл: 12
# 2-й студент: Валентин
# Балл: 7
# 3-й студент: Виктор
# Балл: 4
# 4-й студент: Григорий
# Балл: 9
# 5-й студент: Дмитрий
# Балл:6
# Средний балл: 8. Студенты с балом выше среднего:
# Игорь
# Григорий
#
# studs = {}
# n = int(input("Количество студентов: "))
# # s = 0
#
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[name] = point
#     # s += point
# s = sum(studs.values())  # values -по какому параметру передать значения, скакого элемента мы начинаем считать. если
# # это словарь  то нам нужен  values
# avg = s / n
# print(studs)
# print(s)
# print("Средний балл: ", avg)
#
# for i in studs:  # i - это имена
#     if studs[i] > avg:  # балл среднего арифметического
#         print(i)  # i - это имена
#
# for k, v in studs.items():  # i - это имена
#     if v > avg:  # балл среднего арифметического
#         print(k)  # i - это имена

# вызов функции с большим количеством параметров/ если поставить звездочку
# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7, 8, 'abc'))
# print(func()

# def summa(*params):
#     print(params)
#     print(*params)
#     res = 0
#     for n in params:
#         res += n
#         return res
#
#
# print(summa(1, 2, 3))
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))

# Задача №2 Написать функцию, которая принимает произвольное число чисел  и вычисляет их среднее арифметическое и
# возвращает только те числа, которые меньше полученного среднего арифметического тестовые примеры: 1, 2, 3, 4, 5, 6,
# 7, 8, 9
# 3, 6, 1, 9, 5
#
# 5.0
# [1, 2, 3, 4,]
# 4.8
# [3, 1]


# def ch(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     res = []
#     for num in args:
#         if num < avg:
#             res.append(num)
#     return avg
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))
# s = 1, 2, 3, 4, 5, 6, 7, 8, 9
# print(type(s))

# def func(a, *args):
#     return a, *args
#
#
# print(func(5))
# print(func(1, 2, 3, 5, 'abc'))

# def print_scores(student, *scores):
#     print("Student name:", student, end=", Оценки")
#     for score in scores:
#         print(score, end=" ")
#         print()
#

# print_scores("Jonathan", 100, 95, 88, 92, 99, 84)
# print_scores("Rick", 96, 30, 33, 64)

# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(one="один"))

# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Irina", surname="Sharma", age=22)
#
# intro(name="Igor", surname="Wood", email="igor@mail.ru", country="Russia", age=22, phone=9876543210)

# def func(a, b, *args, y=0, x=9, **kwargs):
#     return a, b, args, kwargs, y, x
#
#
# print(func(5, 1, 2, 3, 4, 5, 6, 7, 8, n=9, m=10, y=100))

# Задача №3
# Создайте функцию, которая принимает неограниченное количество параметров "ключ: значение"
# и обновляет созданный словарь my_dict, состоящий всего из одного элемента"one" со значением "first"
# Словарь должен обновляться  при каждом вызове функции:
# db(k1=22, k2 =31, k3=11, k4=91)
# db(name="Bob", age=31,weight=61, eyes_color="grey")
# my_dict={'one':'first', k1=22, k2 =31, k3=11, k4=91,name="Bob", age=31,weight=61, eyes_color="grey'}
#
# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# print("my_dict=", my_dict)
# db(k1=22, k2=31, k3=11, k4=91)
# print("my_dict=", my_dict)
# db(name="Bob", age=31, weight=61, eyes_color="grey")
# print("my_dict=", my_dict)

# name = "Tom"  # Глобальная переменная
# surname = ""

# def hi():
#     # global name, surname
#     name = "Sam"
#     surname = "Johnson" # Локальная переменная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)


# в Python console:
# import builtins
# dir(builtins)

# sum = 5
# lst[5, 6, 7, 8, 9]
# print(sum(lst))
#
# print = 'hello'
#
#
# print("Python")

# \\\\\\\\\\ПРАКТИКА 02.03.2024\\\\\\\\\\\\\\\\\\\\\\\
#
# def add(a):
#     x = 2
#
#     def outer():
#         x = 3
#         print("x =", x)
#         return a + x
#
#     return outer()
#
#
# print(add(5))
#      ****************
# x = 25
# 
# 
# def fn():
#     global t
#     a = 30
#     t = a
# 
#     def inner():
#         nonlocal a
#         a = 35
#         print("a =", a)
# 
#     inner()
#     t = a
# 
# 
# fn()
# c = x + t
# print(c)
#                       *********************
#
# x = 5
#
#
# def fn1():
#     x = 25  #
#
#     def fh2():
#         x = 33  # 4
#
#         def fn3():
#             nonlocal x
#             x = 55  # 6
#
#         fn3()  # 5
#         print("fn2.x", x)
#
#     fn2()  # 3
#     print("fn1.x", x)
#
#
# fn1()  # 1
# print(x)
#
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # 1,7


# Замыкание - функция
# возвращает другую функцию,
# но не вызывает ее
#
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
#
# item2 = outer(6)
# print(item1(10))
# print(outer(7)(10))
# def func(a):
#     return a * 2

#
# x = func(5)
# print(x)


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         return a, b, c
#
#     return func2()
#
#
# func = func1()
# print(func)

# Задача №1. #Написать функцию,
# ведущую подсчет количество посещений указанного города.
# Функция должна принимать в качестве аргумента название города,
# и возвращать некоторую внутреннюю функцию, которая каждый раз при её вызове будет увеличивать счётчик посещений на 1.
# При решении задачи используйте нелокальную область видимости.
# Москва 1
# Москва 2
# Сочи 1
# Сочи 2
# Москва 3

#
# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
#
# res1()
# res1()
# res1()

# Лямда выражение-это анонимная функция,
# ее называют либо лямбда-функция,
# либо лямда-выражение, у них нет названий, обычно используют,
# когда не нужно использовать большой функционал функции.

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(10, 20))
# #или:
# def func(x,y):
#     return  x + y
# func = lambda x,y : x +y
# print(func(1,2))

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
#
# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7, 8))
# print((lambda *args: args)(1, 2, 3))


# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for t in c:
#     print(t("abc_"))
# В c -хранится не лямбда-выражение(одно не сожем разместить -выдаст ошибку),
# а кортеж (несколько функций) дает поместить без ошибок.

#
# def inc1(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func = inc1(10)
# print(func(5))
#
#
# def inc2(n):
#     return lambda x: n + x
#
#
# func2 = inc2(10)
# print(func2(5))
#
# inc3 = (lambda n: (lambda x: n + x))
#
# func3 = inc3(10)
# print(func3(5))
#
# print((lambda n: (lambda x: n + x))(10)(5))

# Задача №1. #Создать лямбда-выражение для вычисления суммы трех чисел
# с использованием вложенных лямда-выражений
# sum3 (2)(4)(6) = 12

# print((lambda n:(lambda x:(lambda z: n + x + z)))(2)(4)(6))

# print((lambda n: (lambda x: (lambda z: n + x + z)))(10)(5)(1))
# print((lambda a: (lambda b: (lambda c: a + b + c)))(10)(5)(1))


# def func(i):
#     return i[1]
#
#
# d = {'a': 15, 'c': 10, 'b': 5}
# # lst = sorted(d.items(), key=lambda i: i[1])  # [('a', 15), ('b', 5), ('c', 10)]
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# print(dict(lst))

# Задача №1.
# Дан список игроков команды,
# при чем для каждого игрока указаны его имя, фамилия и игровой рейтинг
# (по шкале от 1 до 10, где 10 наибольший балл).
# Отсортируйте список игроков по фамилии,
# а затем по их рейтингу от лучшего к худшему и наоборот.
# Решите задачу с использованием лямда-функций.
#

# players = [
#     {"name": "Антон", "last_name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last_name": "Бодня", "rating": 10},
#     {"name": "Федор", "last_name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last_name": "Семенов", "rating": 6},
# ]
#
# res = sorted(players, key=lambda item: item["last_name"])
# print(res)
# res1 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res1)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[1](8, 3))
# print(a[2](8, 3))
# print(a[0](8, 3))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[6]()


# задача 2
# создать лямбда-выражение для нахождения фигур:
# площадь окружности радиуса 2:12.566370614359172
# площадь прямоугольника размером:10*13:130
# площадь трапеции для а=7,b=5,h=3:18.0

# from math import pi
#
# area = {
#     "Circle:": lambda radius: pi * radius * radius,
#     "Rectangle:": lambda a, b: a * b,
#     "Trapezoid:": lambda a, b, h: a + b * h / 2
# }
# print("Площадь окружности:", area["Circle:"](2))
#
# print("Площадь прямоугольника:", area["Rectangle:"](10, 13))
#
# print("Площадь трапеции:", area["Trapezoid:"](7, 5, 3))
# # в лямбда-выражении можно использовать
# print((lambda a, b: a if a > b else b)(5, 10))
#
# print((lambda a, b: a if a > b else b)(15, 10))

# Написать функцию, вычисляющую площадь
# прямоугольного параллелепипеда с ребрами a, b и c.
# Данная функция должна содержать внутри себя еще одну функцию,
# вычисляющую площадь прямоугольника. Решить задачу для случаев,
# когда общая площадь определена, как глобальная и как локальная переменная.
# Внести изменения в функции таким образом, чтобы общая площадь
# могла использоваться как нелокальная переменная, тестовые значения: 2,4,6
# 5, 8, 2
# 1, 6, 8
#
# 88
# 132
# 124
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# \\\\\\\\\\ПРАКТИКА 03.03.2024\\\\\\\\\\\\\\\\\\\\\\
# Локальный репозиторий -это  GIT
# Удаленный репозиторий -это GIHUB
# команды в gitbush
# git --version
# git --help -если мы не знаем команды, выдаст все.
# git init -создает пустой репозиторий, применяется 1 раз для репозитория
# git status - проверка в каком состоянии находится наш репозиторий
# git add -добавить файлы под веретённый контроль,
# Чтобы гид контролировал файлы - A или --all -добавятся все файлы находящиеся в папках и подпаках
# main.py - только указанный документ
# . - добавляет все файлы из текущей папки
# print("Вносим изменения")
# в git добавить изменения: git add main.py
# проверим в git status-должно быть все зеленое
# #постоянная настройка
# git config --global user.name
# "Julion"

# git config --global user.email''

# git commit -m "first commit" = контрольная точка нашего репозитория
# .gitignore - создается в папке new file в пайчарм
# git branch -на какой ветке находимся
# git branch "cat" - cоздание ветки
# git checkout master -возвращение на предыдущую ветку
# git branch -D cat -удаление ветки
# git branch "readme"
# создание файла  - readme.md
# master > readme > создали файл на ветке readme
# -на ветке master файл readme.md  -не существует
# -как слить информацию с ветки readme
# на ветку master -необходимо указать git merge   и указать
# ветку с которой пытаемся слить первичную ветку -readme
# git branch "cat" cоздание ветки
#  branch master -возвращение на предыдущую ветку
# git branch -D cat
# git branch -D readme
# readme.md
## Первый репозиторий количество решеток имеет от 1 до 6,
# меняется шрифт, описывается техническая документация
# git merge readme -слияние веток
# git log -посмотреть все репозитории, история комитов

# The key fingerprint is:s
# GIT and на git hub
## Первый репозиторий
# win + r> control > откроется control
# panel либо больше иконки, либо малые иконки -credential menedger_
# диспетчер учетных записей-учетные данные виндовс
# добавить общие учетные записи
#  В правом верхнем углу github нажать на + новый репозиторий - имя - публичный, создать , вставить в гит БАШ

# git push -u origin master
# git remote add origin https://github.com/July-vol/Python318.git
# выложить данные на GitHub
# 0) git status
# 1) git add .
# 3) git commit -m "название коммитa"
# 4)git push -переносит данные с локального репозитория на удаленный репозиторий

#
# print("Данные переносим на GitHub")
#
# print("ДЗ от 02.03.2024")

# \\\\\\\\\\ПРАКТИКА 03.03.2024\\\\\\\\\\\\\\\\\\\\\\
# map(func, iterable),  filter(func, iterable) - уже готовые циклы
# Полный вариант:
#
# def mult(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
#
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)

# Если из функции возвращается больше 1 элемента, то это возвращается кортеж
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = dict(map(lambda x, y: (x, y), num, st))
# print(res)


# ////// Задача № 1./////// Найти поэлементно сумму чисел двух списков:# l1 = [1, 2, 3]
# # l2 = [4, 5, 6]
# [5, 7, 9]


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)
# map -изменяет все элементы, а  filter -нет
# def func(s):
#     return len(s) == 3
#
#
# t = ('abcd', 'abc', 'asdfg', 'def', 'ert', '')  # 'abcdabcdabcd'
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))  # t2 = ('abc', 'def', 'ert')(s -принимаемый аргумент функции(можно
# # поменять на любой)
# t2 = tuple(filter(func, t))  # t2 = ('abc', 'def', 'ert')
# print(t2)

# b = [60, 90, 68, 59, 76, 60, 88, 74, 81, 65] res = list(filter(lambda s: s > 75, b)) print(res) ////// Задача №
# 2.///////  Сгенерировать список  из десяти элементов случайным образом. Из полученного списка чисед выбрать только
# те, которые находятся в диапазоне  от 10 до 20  (включительно). [11, 6, 8, 15, 25, 6, 20, 22, 38, 15]
# [11, 15, 20, 15]
# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
#
# lst2 = list(filter(lambda t: 10 <= t <= 20, lst))
# print(lst2)


# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)
#
# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def inner():
#         print("*" * 48)
#         # print("Code before")
#         func()
#         # print("Code after")
#         print("=" * 48)
#
#     return inner
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# # @my_decorator - декоратор
# def func_test():  # декорирующая функция
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()
# hello()

# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print("*" * 40)
#         func()
#         print("=" * 40)
#
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0  # 3
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()

#
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print("Меня зовут", name, surname)
#
#
# print_full_name("Ирина", "Ветрова")
#
#
# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")
#


# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# @decor("Произведение:", "*")
# def mul(a, b):
#     print(a * b)
#
#
# n = 5
# m = 2
# summa(n, m)
# sub(n, m)
# mul(n, m)

def multiply(arg):
    def decor(fn):
        def wrap(*args, **kwargs):
            return arg * fn(*args, **kwargs)

        return wrap
    return decor


@multiply(3)
def return_num(num):
    return num


print(return_num(5))

def avg(fn):
    def wrap(*args):
        return fn(*args) / len(args)

    return wrap


@avg
def summa(*args):
    return sum(args)


print(summa(2, 3, 3, 4))

# Строки

# print(10)
# print(bin(18))  # 0b10010 => 0b - двоичная система
# print(oct(18))  # 0o22 => 0o - восьмиричная
# print(hex(18))  # 0x12 => 0x - шестнадцатеричная
#
# print(0b10010 + 0o22)
# print(0o22)
# print(0x12 + 0o22)

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)  # Python => Pytton
# # print(e * 3)
# # print("y" in e)
# # print("l" in e)
# # print(e[1])
# # print(e[-1])
# # print(e[1:4])
# # print(e[::-1])
# e = e[:3] + 't' + e[4:]
# print(e)
