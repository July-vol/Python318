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
import sqlite3

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

# Практика 20.01.03.03.py
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

# Практика № 3 от 21.01.03.03.py

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


# Практика №4 от 27.01.03.03.py

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


# Практика №5 от 28.01.03.03.py
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

# Практика №6 от 03.02.03.03.py
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


# Практика №7 от 04.02 .03.03.py
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


# ////////////////// Практика 10.02.03.03.py//////////////////

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


# ///////////////Практика 17.02.03.03.py//////////////////
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

# ///////////////Практика 18.02.03.03.py////////////////// Ключами могут быть только неизменяемые типы данных. Ключами не
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

# \\\\\\\\\\ПРАКТИКА 24.02.03.03.py\\\\\\\\\\\\\\\\\\\\\\\

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

# \\\\\\\\\\ПРАКТИКА 02.03.03.03.py\\\\\\\\\\\\\\\\\\\\\\\
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

# \\\\\\\\\\ПРАКТИКА 03.03.03.03.py\\\\\\\\\\\\\\\\\\\\\\
# Локальный репозиторий -это  GIT
# Удаленный репозиторий -это GIHUB
# команды в gitbush
# git --version
# git --help -если мы не знаем команды, выдаст все.
# git init -создает пустой репозиторий, применяется 1 раз для репозитория
# git status - проверка в каком состоянии находится наш репозиторий
# git add .  -добавить файлы под веретённый контроль,
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
# print("ДЗ от 02.03.03.03.py")

# \\\\\\\\\\ПРАКТИКА 03.03.03.03.py\\\\\\\\\\\\\\\\\\\\\\
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
#
# def multiply(arg):
#     def decor(fn):
#         def wrap(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return wrap
#
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))
#
#
# def avg(fn):
#     def wrap(*args):
#         return fn(*args) / len(args)
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     return sum(args)
#
#
# print(summa(2, 3, 3, 4))

# \\\\\\\\\\ПРАКТИКА 17.03.py\\\\\\\\\\\\\\\\\\\\\\
# Строки
# print(10)
# print(bin(18))  # 0b10010 => 0b - двоичная система
# print(oct(18))  # 0o22 => 0o - восьмеричная
# print(hex(18))  # 0x12 => 0x - шестнадцатеричная
#
# print(0b10010 + 0o22)
# # print(0o22)
# print(0x12 + 0o22)

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)  # Python => Pytton
# print(e * 3)
# # print("y" in e)
# # print("l" in e)
# # print(e[1])
# # print(e[-1])
# # print(e[1:4])
# # print(e[::-1])
# e = e[:3] + 't' + e[4:]
# print(e)
#
# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
# print(r"C:\folder\\"[:-1])
# print(r"C:\folder" + "\\")
# print("C:\\folder\\")
#
# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# a = f"Меня зовут {name}. Мне {age} лет."
# print(a)
# print(f"Число: {round(12.2564, 2)}, {5 + 3}")
# print(f"Число: {12.2564:.2f}")
#
# x = 10
# y = 5
# print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

#
# s = """Строка
# символов"""
# print(s)
# s1 = '''Строка
# символов'''
# print(s1)
# s2 = ("Строка "
#       "символов")
# print(s2)

# def square(n):
#     """Принимает число n, возвращает число n"""
#     print("Hello")
#     return n ** 2
#
#
# print(square(5))
#
# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(sum.__doc__)
# print(len.__doc__)
# print(int.__doc__)
# print(type.__doc__)

# print(ord('a'))
# print(ord('й'))

# while True: n = input("-> ")
# if n != "-1":
# print(ord(n))
# else: break
#
#
# Дана строка: "Test string for me", сформируйте
# список, содержащий ASCII коды символов этой строки Вычислите среднее арифметическое (с точностью до целого)
# полученных кодов и допишите его в начало списка. Спросите у пользователя еще три символа(если пользователь ввел
# больше символов используйте первые3. Получите их в АSCII коды. Проверьте наличие каждого из этих кодов в списке,
# и если его нет -допишите в конец списка. Определите есть ли все элементы, равные последнему, и если да,
# то определите только их. отсортируйте список по убыванию
# ASCII коды: [84, 101, 115, 116, 32, 115, 116, 114, 105, 110, 103, 32, 102, 111, 114, 32, 109, 101]
# Среднее арифметическое [95, 84, 101, 115, 116, 32, 115, 116, 114, 105, 110, 103, 32, 102, 111, 114, 32, 109, 101]
# -> tes
# [95, 84, 101, 115, 116, 32, 115, 116, 114, 105, 110, 103, 32, 102, 111, 114, 32, 109, 101].

# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# \\\\\\\\\\ПРАКТИКА 23.03.py\\\\\\\\\\\\\\\\\\\\\\
# Даны два числа а =122, b= 97, где a и b  коды символов. Ваша задача -вывести все символы,
# ASCII - коды которых лежат между a и b включительно, в порядке возрастания их кодов.

# a = 122
# b = 97
# #
# # if a > b:
# #     for i in range(b, a + 1):
# #         print(chr(i), end=" ")
# # else:
# #     for i in range(a, b + 1):
# #         print(chr(i), end=" ")
# if b > a:
#     a, b = b, a  # a = 122, b = 97
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")
#
# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65

# from random import randint
#
# min_ascii = 33
# max_ascii = 126
# shortest = 6
# longest = 16
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):  # range(0, 6)
#         res += chr(randint(min_ascii, max_ascii))
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# Методы строк
#
# s = "hello, WORLD! I am learning Python."
# print(s)
# a = s.capitalize()
# print(a)  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.count('l'))
# print(s.lower().count('l'))
#
# print(s.count('h', 1, -4))
# print(s.count('h'))

# print(s.find("Python"))  # поиск подстроки в строке, возвращает индекс совпадения, если совпадение нет вернет "-1"
# print(s.index("Python"))  # поиск подстроки в строке, возвращает индекс совпадения, если совпадение нет вернет
# # исключение "ValueError"
#
# print(s.find("h", 1, -4))
# print(s.rfind("h1"))
# print(s.rindex("h1"))
# Задача №2 дана строка, состоящая ровно из двух слов,
# разделенных пробелом.Перестав те эти слова местами.
# Результат запишите в строку и выведите получившуюся строку

# st = input("Введите два слова через пробел: ")  # "один два"  " " -> 4
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
#
# print(second + " " + first)
#
#
# s = "hello, WORLD! I am learning Python."
# print(s)
#
# print(s.endswith("on."))  # заканчивается ли строка на заданную подстроку -> (True, False)
# print(s.startswith("I am", 14))  # начинается ли строка на заданной подстроки -> (True, False)
# print(s.find("I am"))

#
# a = input("Введите число: ")
# try:
#     a = int(a)
#     print(a ** 2)
# except ValueError:
#     print("Нужно ввести число")

# print('_123'.isdigit())  # состоит ли строка только из чисел
# print('123a'.isdigit())
#
# a = input("Введите число: ")
# b = 2
# if a.isdigit():
#     a = int(a)
#     print(a + b)
# else:
#     print(a + str(b))

#
# print("abc123Ф!".isalnum())  # состоит ли строка только из букв и цифр
# print("ABCabc".isalpha())  # состоит ли строка только из букв


# print("abc123!@#".islower())  # определяет, являются ли буквенные символы строки в нижнем регистре
# print("ACV123!@#".isupper())  # определяет, являются ли буквенные символы строки в верхнем регистре

# print('py'.center(10))
# print('py'.center(11, "-"))
# print('py'.center(1))

#
# print("     p   y     ".lstrip())
# print("     py     ".rstrip())
# print("     py     ".strip())
#
# print("https://www.python.org".lstrip("/:pths"))
# print("https://www.python.orgw".strip("/:pthsw"))
# print("https://www.python.orgw".lstrip("/:pths").rstrip("w"))
#
# s = "hello, Python! I am learning Python. Python"
# print(s.replace("Python", "Java", 2))  # поиск и замена

# s = ""
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '2']))  # объединяет итерируемый объект в строку через символ разделитель
#
# print(":".join("Hello"))

# print("a b c".split())
# print("www.python.org".split(".", 1))
# print("www.python.org".rsplit(".", 1))

# Регулярные выражения

# import re


# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения с шаблоном
# print(re.search(reg, s))  # возвращает первое совпадение с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # поиск по шаблону в начале строки
# print(re.split(reg, s, 3))  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, "!", s, 1))  # поиск и замена

# s = r"Я ищу совпадения в 2024 году. И я и^х найду в 2 счё_та. [1938765]. Hel-lo."
# # reg = r"[204]"
# # reg = r"[2-4]"
# # reg = r"[А-яЁё]"
# # reg = r"[A-Za-z9.[\]-]"
# # reg = r"[^0-9]"
# reg = r"[12][09][0-9][0-9]"  # 20[00] 19[00]
# print(re.findall(reg, s))
# print(ord("Ё"))  # 1025
# print(ord("А"))  # 1040
# print(ord("Я"))  # 1071
# print(ord("а"))  # 1072
# print(ord("я"))  # 1103
# print(ord("ё"))  # 1105
# print(chr(96))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:59. Минуты, в диапазоне от 00 до 59. 2021-06-15T04:09."
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, st))

# s = r"Я ищу совпадения в 2024 году. И я их найду в 2 счё_та. Hel-lo 20000000"
# reg = r"\d"  # [0-9]
# reg = r"\D"  # [^0-9]
# reg = r"\s"  # [ ]
# reg = r"\S"  # [^ ]
# reg = r"\w"  # [0-9A-zА-я_]
# reg = r"\W"  # [^0-9A-zА-я_]
# reg = r"\AИ я"
# reg = r"году.\Z"
# reg = r"\Bния"
# reg = r"\w+"
# reg = r"\d+"
# reg = r"20*"
# # print(re.findall(reg, s))
# кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения

# d = "Цифры: 7, +17, --42, 0013, 0.3456"
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# st = "05-06-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", st))
# # Дата рождения: 05-06-1987 => Дата рождения: 05.06.1987
# print("Дата рождения:", re.sub(r"-", ".", re.sub(r"\s#.*", "", st)))

# st = "author=Пушкин А.C.; title  = Евгений Онегин, price =200; year= 1831"
# # pattern = r"\w+\s*=\s*[\w\s.]+"
# pattern = r"\w+\s*=\s*[^;,]+"
# print(re.findall(pattern, st))

# s1 = "12 сентября 2024 года 4567897"
# reg1 = r"\d{2,4}"
# print(re.findall(reg1, s1))


# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+\.$"
# print(re.findall(reg, s))

# def valid_login(name):
#     return re.findall("^[A-Za-z0-9_-]{3,16}$", name)
#
#
# print(valid_login("Python_master"))
# print(valid_login("Python"))


# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello World"
# print(re.findall(r"\w\+", text, re.DEBUG))


# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счё_та."
# reg = "я"
# print(re.findall(reg, s, re.IGNORECASE))

# text = """one # Комментарий two"""
#
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # part 1
# @         # @
# [a-z.-]+  # part 2
# """, "test@mail.ru", re.VERBOSE))
# import geometry
# import re


# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))  # [<body>, </body>]


# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# s1 = "12 сентября 2024 года 4567897"
# reg1 = r"\d{3,}?"
# # reg1 = r"\d{3}"
# print(re.findall(reg1, s1))

# s = "Петр и Виталий отлично учатся!"
# reg = r"Ольга|Виталий"
# print(re.findall(reg, s))


# s = "int = 4, float = 4.0f, double = 8.0, float"
# # reg = r"int\s*=\s*[.\w+]*|float\s*=\s*[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*[.\w+]*"
# reg = r"((?:int|float)\s*=\s*(?:[.\w+]*))"
# print(re.findall(reg, s))
# print(re.search(reg, s))

# (?:...) - обозначает, что эта группирующая скобка является не сохраняющей

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# a = "31-03-1921"
# pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19\d\d|20[0-9][0-9])"
# print(re.findall(pattern, a))
# print(re.search(pattern, a).group(2))
# m = re.search(pattern, a)
# print(m[0])
# print(m[1])
# print(m[2])
# print(m[3])


# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."  # 23.10.2024
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex-98.ru.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):  # 0
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # стек: 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))  # 5
# elevator(n1)

#
# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25
#
# def to_str(n, base):  # n = 15
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # convert[15] => 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] => 'E'
#
#
# print(to_str(17, 16))

# def count_items(item_list):  # ['Adam', ['Bob', ['Chat', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], "Ann"]
#     count = 0  # 10
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# names = ['Adam', ['Bob', ['Chat', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], "Ann"]
# print(names)
# print(len(names))
# # print(isinstance(names, list))
# # print(isinstance(names[0], list))
# # print(isinstance(names[1][1][0], list))
# print(count_items(names))
#
#
# def remove(text):  # text = ""
#     if not text:  # text = ""
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # "HelloWorld"
#
#
# print(remove(" Hello\nWorld "))

# f = open("test.txt", "r")
# f = open(r"C:\Users\Пользователь\Desktop\Обучение курсы\318\test.txt", "r")
# print(f)
# print(*f)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)
# # f.close()
# print(f.closed)

# f = open("test.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()
#
# f = open("test.txt", "r")
# print(f.read())
# f.close()


# f = open("test1.txt", "r")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open("test1.txt", "r")
# print(f.readlines(26))
# print("count =", len(f.readlines()))
# f.close()


# f = open("test1.txt", "r")
# for line in f:
#     print(line)
# f.close()


# f = open("test1.txt", "r")
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print("count =", count)

# f = open("xyz.txt", "w")
# f.write("Hello\nWorld!!!!")
# f.close()

# f = open("xyz1.txt", "a")
# f.write("\nNew text")
# f.close()
#
# line = ['This is line 1\n', 'This is line 2\n']
# f = open("xyz.txt", "w")
# f.writelines(line)
# f.close()

#
# lst = [i for i in range(1, 20)]
# print(lst)
#
# f = open("xyz.txt", "w")
# for index in lst:
#     f.write(str(index))
# f.close()


# f = open("xyz.txt", "r")
# d = f.read()
# print(d)
# print(type(d))
# f.close()

#
# lst = [i for i in range(1, 20)]
# print(lst)
#
# f = open("xyz.txt", "w")
# f.write("\t".join(map(str, lst)))
# f.close()
#
#
# f = open("xyz.txt", "r")
# d = f.read()
# st = list(map(int, d.split("\t")))
# print(st)
# print(type(st[0]))
# f.close()

# #
# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open(file, "r")
# read_line = f.readlines()
# f.close()
#
# print(read_line)
# read_line[1] = "Hello world!\n"
# print(read_line)
#
#
# f = open(file, "w")
# f.writelines(read_line)
# f.close()
#
#
# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()

# f = open(file, "r")
# s = f.readlines()
# f.close()
# print(s)
#
# pos = int(input("pos = "))
# if 0 <= pos < len(s):
#     del s[pos]
# else:
#     print("Индекс введен неверно")
# print(s)
#
# f = open(file, "w")
# f.writelines(s)
# f.close()

# f = open("test.txt")
# print(f.read(3))
# print(f.tell())  # позиция условного курсора
# print(f.seek(1))  # перемещение условного курсора в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()


# f = open("test.txt", "r+")
# f.write("I am learning Python")  # "I a-new string-m learning Python"
# print(f.seek(3))
# f.write("-new string-")
# f.close()

# f = open("test.txt", "r+")
# f.write("I am learning Python")  # "I a-new string-ython"
# # print(f.seek(3))
# # f.write("-new string-")
# print(f.tell())
# print(f.read())
# f.close()

# with open('test.txt', "w") as f:
#     print(f.write('012\n34567\n89'))
# print(f.closed)

# with open('test.txt', "r") as f:
#     for line in f:
#         print(line[:2])


# def longest_words(file):
#     with open(file, "r") as text:  # , encoding="utf-8"
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         print(max_length)
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words('test.txt'))

# one = "one.txt"
# two = "two.txt"
# three = "three.txt"
#
# # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\n
# Строка №8\nСтрока №9\nСтрока №10\n"
# #
# # with open(one, 'w') as f:
# #     f.write(text)
#
# with open(one, "r") as fr, open(two, "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# one = "one.txt"
# two = "two.txt"
# three = "three.txt"

# with open(one, "r") as f1:
#     a = f1.readlines()
# print(a)
#
# with open(two, "r") as f2:
#     b = f2.readlines()
# print(b)
#
# c = a + b
# print(c)
#
# with open(three, "w") as f3:
#     f3.writelines(c)


# with open(one, "r") as f1, open(two, "r") as f2, open(three, "w") as f3:
#     a = f1.readlines()
#     b = f2.readlines()
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     print(a)
#     print(b)
#     print(c)
#     f3.writelines(c)

# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()

# f = open(file, 'r')
# read_line = f.readlines()
# f.close()
#
# print(read_line)
# pos1 = int(input("pos1 = "))
# pos2 = int(input("pos2 = "))
# if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):  # a, b = b, a
#     read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
# else:
#     print("Такой строки нет")
# print(read_line)
#
# f = open(file, "w")
# f.writelines(read_line)
# f.close()

# file = "text2.txt"
#
# f = open(file)
# line = 0
# for i in f:
#     line += 1
#     word = 0  # 5
#     flag = 0  # 1
#     for j in i:
#         if j != " " and flag == 0:
#             word += 1
#             flag = 1
#         elif j == " ":
#             flag = 0
#
#     print(i, len(i), "символов", word, "слов")
#
# print(line, "строки в документе")
# f.close()

# \\\\\\\\\\ПРАКТИКА 06.04.py\\\\\\\\\\\\\\\\\\\\\\

# Модуль OS и OS.PATH

# import os.path

# print(os.getcwd())  # путь к рабочей директории
# print(os.listdir())  # список директорий и файлов
# print(os.listdir(".."))
#
# os.mkdir("folder1")  # создать папку
# os.makedirs("nested1/nested2/nested3")  # создаст папку с промежуточными папками в пути
# os.remove("folder1/1.txt")  # удалить файл
# os.rmdir("folder1")  # удалить папку, но пустую

# os.rename("xyz1.txt", "test2.txt")
# os.rename("folder", "test")  # переименовывает файлы или папки

# os.rename("xyz.txt", "test/xy.txt")
# os.renames("two.txt", "text/t.txt")  # переименовывает файлы или папки и перемещает их по несуществующему пути,
# путем его создания

# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\tFiles:", files)
#
#
# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена")
#     print("-" * 50)
#
#
# remove_empty_dirs("nested1")

# print(os.path.split(r"C:\Users\Пользователь\Desktop\Обучение курсы\nested1\nested2\nested3\text.txt"))
# print(os.path.join(r"C:\Users\Пользователь\Desktop\Обучение курсы", "nested2", "text.txt"))

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, "w").close()
# #
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Текст для файла {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files1 in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(files1)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)


# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

#
# print(os.path.exists(r"C:\Users\Пользователь\Desktop\Обучение курсы\nested1\nested2\nested3\text.txt"))  #
# возвращает True если путь существует в # файловой системе
# import time
#
# path = "main.py"
# print(os.path.getsize(path) / 1024)  # размер файла 81693 байт (79.826171875 KB)
#
# print(os.path.getctime(path))  # время создания файла
# print(os.path.getatime(path))  # время последнего доступа к файлу
# print(os.path.getmtime(path))  # время последнего изменения файла (в секундах)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))


# /////ООП -объектно-ориентированное программирование////// -инкапсуляция -сокрытие каких-то данных-можно сделать
# защиту на правильность окрестности ввода исходных данных -наследование - это когда есть какой-то родительский класс,
# и мы можем наследоватся от него дочерним классом и получить за счет мeтодов все свойства родительского класса
# -полиморфизм -много форм у одного и того же объекта class Point: """Класс для представления координат точек на
# плоскости""" x = 1 y = 1
# Класс - указать ключевое слово-  class НазваниеКласса(и указать ключевое требование
# -каждая буква класса в верхнем регистре):
# свойства (поля, переменные)
# методы (функции)
# атрибуты = свойства и методы.
# создание экземпляра , который основан на этом классе(Экземпляров можно создавать сколько угодно)
# Больше в классе ничего не может быть
# #
# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 30
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
#
# p2 = Point()
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)
#
# print(id(Point))
# print(id(p1))
# print(id(p2))
#
# print(Point.__dict__)
# print(Point.__doc__)

#
# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# # Point.set_coord(p1, 2, 4)
# #
# p2 = Point()
# # # p2.x = 3
# # # p2.y = 7
# p2.set_coord(3, 7)

# Задача 1. Реализуйте класс"Человек". необходимо хранить в полях класса: имя, дату рождения,
# контактный телефон, страну, город, домашний адрес. Реализуйте методы класса для ввода данных,
# реализуйте доступ к отдельным полям через методв класса
# ========================================
# ********* Персональные данные **********
# Имя: Юля
# Дата рождения: 23.05.1986
# Номер телефона: 45-46-98
# Страна: Россия
# Город: Москва
# Домашний адрес: Чистопрудный бульвар, 1А


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.birthday = birthday
#         self.phone = phone
#         self.address = address
#         self.country = country
#         self.city = city
#         self.name = first_name
#
#     def set_name(self, name):  # устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#     def set_birthday(self, value):
#         self.birthday = value
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name())
# h1.set_birthday("25.05.1986")
# print(h1.get_birthday())

# Задача 2. Реализуйте класс"Person" c данными о сотруднике (имя, фамилия)
# и двумя методами. Первый должен вводить
# данные о сотруднике второй должен увеличивать уровень квалификации
# сотрудника на передаваемое количество едениц.
#
# class Person:
#     skill = 10  # статическое свойство
#
#     def __init__(self, name, surname):  # Инициализатор
#         self.name = name  # динамические свойства
#         self.surname = surname
#         print("Инициализатор Person")
#
#     def __del__(self):
#         print("Удаление экземпляра класса")
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
# # del p1
# p1 = 5
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0  # 3
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def get_coord(self):
#         print(self.__dict__)
#
#
# p1 = Point(5, 10)
# p1.get_coord()
#
# p2 = Point(3, 7)
# p2.get_coord()
#
# p3 = Point(8, 16)
# p3.get_coord()
#
# print(p1.count)
# print(p2.count)
# print(p3.count)
#
# print(Point.count)
#

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print(f"Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("TO-P3O")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# del droid3
# del droid1
# del droid2
#
# print("Численность роботов:", Robot.k)
#

# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y  # _Point__y
#
#     def __check_value(s):  # _Point__check_value
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить новые значения
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получаем значения
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата Y должна быть числом")
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# # p1.set_coord(100, "abc")
# # p1.set_coord(100, 500.5)
# print(p1.get_coord())
# # # print(p1.__x, p1.__y)
# # # p1.__x = 100
# # # p1.__y = "abc"
# # # print(p1.__x, p1.__y)
# # print(p1.__dict__)
# # # print(Point.__check_value())
# # print(Point.__dict__)
# p1.set_x(50)
# p1.set_y("abc")
# print(p1.__dict__)
#
# import geometry


#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(s):  # _Rectangle__check_value
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_width(self, value):
#         if Rectangle.__check_value(value):
#             self.__width = value
#
#     def set_length(self, value):
#         if Rectangle.__check_value(value):
#             self.__length = value
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(geometry.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# a = Rectangle(4, 12)
# a.set_length(3)
# a.set_width(9)
# print("Длина прямоугольника:", a.get_length())
# print("Ширина прямоугольника:", a.get_width())
# print("Площадь прямоугольника:", a.get_area())
# print("Периметр прямоугольника:", a.get_perimeter())
# print("Гипотенуза прямоугольника:", a.get_hypotenuse())
# a.draw()

# class Point:
#     __slots__ = "__x", "__y", "z"
#
#     def __init__(self, x, y, z):
#         self.__x = x
#         self.__y = y
#         self.z = z
#
#
# p1 = Point(5, 10, 15)
# # p1.z = 15
# # print(p1.__dict__)
# print(p1.z)
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#         print("__set_x")
#
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# # p1.x = 9
# print(p1.x)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     # x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = "aaa"
# # print(p1.x)
# print(p1.__dict__)

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.deleter
#     def kg(self):
#         print("Удаление свойства")
#         del self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 'десять'
# del weight.kg


# class Point:
#     __count = 0  # _Point__count
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point(5, 10)
# p2 = Point(5, 10)
# p3 = Point(5, 10)
#
# print(Point.get_count())
# print(p1.get_count())
# import geometry
# import random


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
#
#
# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a  # 3
#         if b > mx:  # 5 > 3
#             mx = b  # 5
#         if c > mx:  # 7 > 5
#             mx = c  # 7
#         if d > mx:  # 9 > 7
#             mx = d  # 9
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         mul = 1
#         for i in range(1, n + 1):
#             mul *= i
#         return mul
#
#
# print("Максимальное число:", Numbers.max(3, 5, 7, 9))
# print("Минимальное число:", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое:", Numbers.average(3, 5, 7, 9))
# print("Факториал числа:", Numbers.factorial(5))
# 5! = 1 * 2 * 3 * 4 * 5


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))  # [21, 12, 2023]
#         date = cls(day, month, year)  # date = Date(21, 12, 2023)
#         return date
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#
# dates = [
#     "23.10.2024",
#     "21/12/2023",
#     "01.01.2022",
#     "12.31.2021"
# ]
#
# for i in dates:
#     if Date.is_date_valid(i):
#         date = Date.from_string(i)
#         print(date.string_to_db())
#     else:
#         print(f"Неправильная дата или формат строки с датой")

# date1 = Date.from_string("23.10.2024")
# print(date1.string_to_db())

# date2 = Date.from_string("21/12/2023")
# print(date2.string_to_db())

# data = Date(23, 10, 2024)

# string_date = "23.10.2024"
#   # [23, 10, 2024]
#   # Date(23, 10, 2024)
# print(date.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print(f"Остаток средств с текущего счета {self.value} был переведен на правопреемника")
#         self.value = 0
#         self.print_balance()
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению, у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         # if isinstance(new_name, str):
#         #     self.__name = new_name
#         # else:
#         #     print("Имя должно быть строкой")
#         if not isinstance(new_name, str):
#             raise TypeError("Имя должно быть строкой")
#         else:
#             self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# p = Person('Irina', 26)
# print(p.__dict__)
# p.name = "Igor"
# p.old = 31
# print(p.name)
# print(p.old)

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков-Петров', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))  # Волков-ПетровИгорьНиколаевич
#         # print(letters)
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# print(p1.fio)
# p1.old = 30
# p1.password = '0987 654321'
# p1.weight = 50.5
# print(p1.__dict__)

# Наследование

# class Point:  # class Point(object)
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# print(issubclass(Point, object))  # True

#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self) -> None:
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color} {self.get_width()}")
#
#
# # class Rect(Prop):
# #     def draw_rect(self) -> None:
# #         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()
#
# print(line._sp)


# class Figure:
#     def __init__(self, color):
#         self.color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         if value < 0:
#             raise ValueError(f"Значение {value} должно быть положительным числом")
#         self.__width = value
#
#     def area(self):
#         print(f"Прямоугольник {self.color}. Площадь: ", end="")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print("Создать защиту, чтобы прямоугольник существовал")
# rect.width = -30
# print(rect.area())

# import geometry
#
#
# class Area:
#     count = 0
#
#     @staticmethod
#     def triangle_area_1(a, b, c):
#         p = (a + b + c) / 2
#         Area.count += 1
#         return geometry.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area_2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
# print(f"Площадь треугольника по формуле Герона: {Area.triangle_area_1(3, 4, 5)}")
# print(f"Площадь треугольника по формуле Герона: {Area.triangle_area_1(4, 5, 8)}")
# print(f"Площадь треугольника через основание и высоту: {Area.triangle_area_2(6, 7)}")
# print(f"Площадь квадрата: {Area.square_area(7)}")
# print(f"Площадь квадрата: {Area.square_area(8)}")
# print(f"Площадь квадрата: {Area.square_area(9)}")
# print(f"Площадь прямоугольника: {Area.rect_area(2, 6)}")
# print(f"Количество подсчетов пощади: {Area.get_count()}")

# /////////Практика 21.04.2024///////////////
# Наследование от встроенных типов

# class Vector(list):  # [1, 2, 3] => "1 2 3"
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# v.append(4)
# print(v)
# print(type(v))


# Перегрузка методов

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"x = {self.x}, y = {self.y}"
#
#     def set_coord(self, x=None, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(10, 20)
# print(p1)
# p1.set_coord(1, 3)
# print(p1)
# p1.set_coord(5)
# print(p1)
# p1.set_coord(y=30)
# print(p1)
# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# class Ellipse(Prop):
#     # def draw(self):
#     #     print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color} {self._width}")
#     ...
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

# from geometry import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть реализован метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())


# Абстрактный класс - это класс, который содержит хотя бы один абстрактный метод

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod  # абстрактный метод
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()


# q = Chess()  # экземпляр абстрактного класса создать нельзя

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def draw(self):
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print('*' * 30)
# for elem in d:
#     elem.print_value()
#     elem.draw()
#
#
# print('*' * 30)
# for elem in e:
#     elem.print_value()
#     elem.draw()


# Интерфейс

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Display_1")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("Display_2")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# Вложенные классы

# def outer():
#     x = 5
#
#     def inner():
#         y = 10
#         print(x)
#
#     inner()
#     print(y)
#
#
# outer()
#
#
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print("outer_method")
#
#     def instance_method(self):
#         print("instance_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод во сложенном классе", MyOuter.age, self.obj.name)
#             MyOuter.outer_method()
#             self.obj.instance_method()
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внутренний", out)
# # inner = MyOuter.MyInner("внутренний")
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end="")
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = 'i7'
#             self.ram = 16
#
#         def show(self):
#             print(f" => {self.brand}, {self.cpu}, {self.ram}")
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
#
# s1.show()
# s2.show()

# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#         self.id = "657"
#
#     def show(self):
#         print("Name:", self.name)
#         print("Id:", self.id)
#         print("*" * 20)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name, self.intern.id)
#         print("*" * 20)
#
#     class Head:
#         def __init__(self):
#             self.name = "Boss"
#             self.id = "789"
#
#         def show(self):
#             print("Name:", self.name)
#             print("Id:", self.id)
#             print("*" * 20)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# # d1 = Employee.Intern()
# # d2 = Employee.Head()
#
# d1.show()
# d2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Window"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = [Cat("Пушок")]
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7)
# print(len(p))
# p1 = Point(4, 6, 8)
# print(len(p1))
#
#
# list()


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# print(p1.x, p1.y)
# p1.z = 30
# print(p1.z)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# p2 = Point2D(10, 20)
# print("pt1 =", p1.__sizeof__())
# print("pt2 =", p2.__sizeof__() + p2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = ('z',)
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20)
# pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
#
#
# a = 3, 5
# print(type(a))

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is slipping")
#
#     def show(self):
#         print("Animal")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#     def show(self):
#         print("Pet")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.bark()
# dog.sleep()
# dog.play()
# dog.show()

# class A:
#     def __init__(self):
#         print("Инициализатор класса A")


# class AA:
#     def __init__(self):
#         print("Инициализатор класса AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     # def __init__(self):
#     #     print("Инициализатор класса D")
#     pass
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)


# class A:
#     def __init__(self):
#         print("Инициализатор класса A")
#
#
# class B(A):
#     def __init__(self):
#         # C.__init__(self)
#         super().__init__()
#         print("Инициализатор класса B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     # def __init__(self):
#     #     C.__init__(self)
#     #     B.__init__(self)
#     #     print("Инициализатор класса D")
#     pass
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         self._sp = sp
#         self._ep = ep
#         # Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)  #
# l1.draw()


# Миксины

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         MixinLog.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()


# Перегрузка операторов
# + - * / // %
# ==, >, <, >=, <=
# []

# Число секунд в одном дне: 24 * 60 * 60 = 86400

# class Clock:
#     __DAY = 86400  # Число секунд в дне
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec - other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec == other.sec
#
#     # def __ne__(self, other):
#     #     return not self.__eq__(other)
#     #     # if not isinstance(other, Clock):
#     #     #     raise ArithmeticError("Правый операнд должен быть типом Clock")
#     #     # return self.sec != other.sec
#
#
# c1 = Clock(100)
# c2 = Clock(100)
# print(c1.get_format_time())
# print(c2.get_format_time())
# # c3 = c1 + c2
# # print(c3.get_format_time())
# # c4 = c1 + c2 + c3
# # print(c4.get_format_time())
# # c5 = c4 - c2
# # print(c5.get_format_time())
# # if c1 == c2:
# #     print("Время равно")
# # else:
# #     print("Время разное")
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время равно")

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]  # range(0, 1) - range(0, 5)
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Else", 5, "F")
# cat3 = Cat("Murzic", 3, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# # print(cat1 + cat2)
# print(cat1 + cat2)


# class Student:
#     def __init__(self, name, *args):
#         self.name = name
#         self.marks = list(args)  # [5, 5, 3, 4, 5]
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 => 6
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#         # self.marks[key] = None
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# a = [5, 5, 3, 4, 5]
# # ch = [None] * 5
# # print(ch)
# a.extend([None] * 5)
# print(a)


# class Clock:
#     __DAY = 86400  # Число секунд в дне
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return self.sec // 3600 % 24
#         if item == "min":
#             return self.sec // 60 % 60
#         if item == "sec":
#             return self.sec % 60
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
#
# c1["hour"] = 15
# c1["min"] = 25
# c1["sec"] = 42
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimeter())

# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @abstractmethod
#     def info(self):
#         print(f"Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     @abstractmethod
#     def make_sound(self):
#         ...
#
#
# class Cat(Animal):
#     def info(self):
#         print(f"Я кот.", end=" ")
#         super().info()
#
#     def make_sound(self):
#         print(f"{self.name} мяукает.")
#
#
# class Dog(Animal):
#     def info(self):
#         print(f"Я собака.", end=" ")
#         super().info()
#
#     def make_sound(self):
#         print(f"{self.name} гавкает.")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.surname} {self.name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, group, rating):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{ self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, speciality, skill):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.skill = skill
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.skill}", end="")
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, speciality, group, rating, topic):
#         super().__init__(surname, name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end="")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()

# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c1()
# c1()

# def string_strip(chars):
#     def call(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return call
#
#
# s1 = string_strip("?:!.; ")
# print(s1(" ? Hello World! ; "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, string):  # *args, **kwargs
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(self.__chars)
#
#
# s2 = StringStrip("?:!.; ")
# print(s2(" ? Hello World! ; "))
#
#
# class StringStrip1:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s3 = StringStrip1("?:!.; ")
# print(s3(" ? Hello World! ; "))


# def my_decorator(fn):
#     def wrap():
#         print("Перед вызовом функции")
#         fn()
#         print("После вызова функции")
#     return wrap
#
#
# @my_decorator
# def func():
#     print("func")
#
#
# func()


# Класс как декоратор

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self):
#         print("Перед вызовом функции")
#         self.fn()
#         print("После вызова функции")
#
#
# @MyDecorator
# def func1():
#     print("func")
#
#
# func1()


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, a, b):
#         res = self.fn(a, b)
#         print("Перед вызовом функции\n" + str(res) + "\nПосле вызова функции")
#         return res
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 5) * 2)


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 3))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("-" * 40)
#         print("*args", args)
#         print("**kwargs", kwargs)
#         return self.func(*args, **kwargs)
#
#
# @Power
# def mult(a, b):
#     return a * b
#
#
# @Power
# def mult1(a, b, c):
#     return a + b - c
#
#
# print(mult(2, 3))
# print(mult1(2, 3, 4))
# print(mult1(2, c=3, b=4))

# def outer(arg):
#     def my_decorator(fn):
#         def wrap():
#             print(f"Перед вызовом функции, выведем {arg}")
#             fn()
#             print("После вызова функции")
#         return wrap
#     return my_decorator
#
#
# @outer("test")
# def func():
#     print("func")
#
#
# func()

# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             print(f"Перед вызовом функции {self.arg}")
#             fn(a, b)
#             print("После вызова функции")
#         return wrap
#
#
# @MyDecorator("test")
# def func1(a, b):
#     print(a, b)
#
#
# func1(2, 5)


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             return fn(a, b) ** self.arg
#         return wrap
#
#
# @Power(5)
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 2))


# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     def get_perimeter(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод get_perimeter()")
#
#     def get_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод get_area()")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#     def info(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод info()")
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         self.side = side
#         super().__init__(color)
#
#     def get_perimeter(self):
#         return self.side * 4
#
#     def get_area(self):
#         return self.side * self.side
#
#     def draw(self):
#         return ("*  " * self.side + "\n") * self.side
#
#     def info(self):
#         print(f"=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}\nПериметр: {self.get_perimeter()}"
#               f"\nПлощадь: {self.get_area()}\n{self.draw()}")
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         self.length = length
#         self.width = width
#         super().__init__(color)
#
#     def get_perimeter(self):
#         return (self.length + self.width) * 2
#
#     def get_area(self):
#         return self.length * self.width
#
#     def draw(self):
#         return ("*  " * self.width + "\n") * self.length
#
#     def info(self):
#         print(f"=== Прямоугольник ===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}\nПериметр:"
#               f" {self.get_perimeter()}\nПлощадь: {self.get_area()}\n{self.draw()}")
#
#
# class Triangle(Shape):
#     def __init__(self, side_x, side_y, side_z, color):
#         self.side_x = side_x
#         self.side_y = side_y
#         self.side_z = side_z
#         super().__init__(color)
#
#     def get_perimeter(self):
#         return (self.side_x + self.side_y + self.side_z) / 2
#
#     def get_area(self):
#         p = self.get_perimeter()
#         return round(geometry.sqrt(p * (p - self.side_x) * (p - self.side_y) * (p - self.side_z)), 2)
#
#     def draw(self):
#         row = []
#         for n in range(self.side_y):
#             row.append("   " * n + "*  " * (self.side_x - 2 * n) + "   " * n)
#         # row.sort()
#         # return "\n".join(row)
#         return "\n".join(sorted(row))
#
#     def info(self):
#         print(f"=== Треугольник ===\nСторона 1: {self.side_x}\nСторона 2: {self.side_y}\nСторона 3: "
#               f"{self.side_z}\nЦвет: {self.color}\nПериметр:"
#               f" {self.get_perimeter()}\nПлощадь: {self.get_area()}\n{self.draw()}")
#
#
# figs = [Square(3, "red"), Rectangle(3, 7, "green"), Triangle(11, 6, 6, "yellow")]
#
# for g in figs:
#     g.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass()")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# class String:
#     def __init__(self, value):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__surname = value
#
#
# p = Person("Ivan", "Petrov")
# p.name.set("Petr")
# print(p.name.get())


# Дескриптор
# __get__()
# __set()
# __delete__()
# __set_name__()


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         # print(instance)
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     first_name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, first_name, surname):
#         self.first_name = first_name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# p.surname = "Sidorov"
# print(p.first_name)
# print(p.surname)
#
# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise ValueError(f"Координата {coord} должно быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.__name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.__name]
#         return getattr(instance, self.__name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.__name] = value
#         setattr(instance, self.__name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# print(p1.x)

# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst.append(9)
# print(lst, lst.get_length())

# Создание модулей

# import geometry
# import random
# import math


# import geometry.rect
# import geometry.sq
# import geometry.trian
#
# r1 = geometry.rect.Rectangle(1, 2)
# r2 = geometry.rect.Rectangle(3, 4)
#
# s1 = geometry.sq.Square(10)
# s2 = geometry.sq.Square(20)
#
# t1 = geometry.trian.Triangle(1, 2, 3)
# t2 = geometry.trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimeter())

# from geometry import rect, sq, trian


# geometry.rect

# from geometry import *

# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimeter())
#
#
# if __name__ == '__main__':
#     run()


# from car import electrocar
# from car.electrocar import ElectroCar
#
# # e_car = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
# e_car = ElectroCar("Tesla", "T", 2018, 99000)
# e_car.show_car()
# e_car.description_battery()

# Упаковка данных (сериализация)
# Распаковка данных (десериализация)

# marshal  (.pyc)
# pickle
# json

# import pickle


# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "груши"],
#     "овощи": ("морковь",),
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, "rb") as f:
#     shop_list_2 = pickle.load(f)
#
# print(shop_list_2)

# class Test:
#     num = 35
#     string = "Привет"
#     lst = [1, 2, 3]
#     tpl = (25, 98)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\nСписок: {Test.lst}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
# # print(obj)
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# new_obj = pickle.loads(my_obj)
# print(new_obj)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# # print(item1)  # 35 test 4
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3)
#
#
# import json
#
# data = {
#     'name': 'Ольга',
#     'age': 20,
#     20: None,
#     1: True,
#     False: 0,
#     'hobbies': ('running', 'singing'),
#     'children': {
#         'first_name': ['Алиса', 'Боб'],
#         'age': [6, 12]
#     }
# }
#
# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent=4)
#
# with open("data_file.json", "r") as f:
#     data2 = json.load(f)
#
# print(data2)
#
# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))
#
# data3 = json.loads(json_string)
# print(data3)
# print(type(data3))
#
# x = {"name": "Виктор"}
# a = json.dumps(x)
# print(a)
# b = json.dumps(x, ensure_ascii=False)
# print(b)
# print(json.loads(a))
#
# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         "tel": tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons1.json'))
#     except FileNotFoundError:
#         data = {}
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)
#
#
# for i in range(5):
#     write_json(gen_person())

# import json
#
# data = {}
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f"{self.country}: {self.capital}"
#
#     @staticmethod
#     def load_data(filename):
#         try:
#             date = json.load(open(filename))
#         except FileNotFoundError:
#             date = {}
#         finally:
#             return date
#
#     @staticmethod
#     def add_country(filename):
#         country_name = input("Введите название страны(заглавной буквы): ")
#         capital_name = input("Введите название столицы(с заглавной буквы): ")
#         # try:
#         #     date = json.load(open(filename))
#         # except FileNotFoundError:
#         #     date = {}
#         date = CountryCapital.load_data(filename)
#
#         date[country_name] = capital_name
#         with open(filename, "w") as f:
#             json.dump(date, f, indent=2)
#
#     @staticmethod
#     def load_from_file(filename):
#         with open(filename, "r") as f:
#             print(json.load(f))
#
#     @staticmethod
#     def delete_country(filename):
#         del_country = input("Введите название страны: ")
#
#         # try:
#         #     date = json.load(open(filename))
#         # except FileNotFoundError:
#         #     date = {}
#         date = CountryCapital.load_data(filename)
#
#         if del_country in date:
#             del date[del_country]
#
#             with open(filename, "w") as f:
#                 json.dump(date, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(filename):
#         country = input("Введите название страны: ")
#
#         # try:
#         #     date = json.load(open(filename))
#         # except FileNotFoundError:
#         #     date = {}
#         date = CountryCapital.load_data(filename)
#
#         if country in date:
#             print(f"Страна {country} столица {date[country]} есть в словаре")
#         else:
#             print(f"Страны {country} нет в словаре")
#
#     @staticmethod
#     def edit_data(filename):
#         country = input("Введите страну для корректировки: ")
#         new_capital = input("Введите новое название столицы: ")
#
#         # try:
#         #     date = json.load(open(filename))
#         # except FileNotFoundError:
#         #     date = {}
#         date = CountryCapital.load_data(filename)
#
#         if country in date:
#             date[country] = new_capital
#             with open(filename, "w") as f:
#                 json.dump(date, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#
# file = 'list_capital.json'
# index = ''
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - "
#                   "редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")
# #
# import requests
# import json

# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(response.text)
# # print(type(response.text))
# todos = json.loads(response.text)
# print(todos)
# print(type(todos[0]))
#
# todos_by_user = {}  # {1: 3, 2: 1}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1  # todos_by_user[1] += 1 =>  todos_by_user[1] = todos_by_user[1] + 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1  # todos_by_user[1] = 1
#
# print(todos_by_user)  # {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}
#
# top_user = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_user)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]
#
# max_complete = top_user[0][1]
# print(max_complete)  # 12
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < max_complete:  # 11 < 12
#         break
#     users.append(str(user))
#
# print(users)  # [5, 10]
# # users = ["5"]
# max_users = " and ".join(users)
# s = "s" if len(users) > 1 else ""
# print(f"User{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(tod):
#     is_completed = tod["completed"]
#     has_max_count = str(tod["userId"]) in users
#     return is_completed and has_max_count
#
#
# with open("filtered_data.json", "w") as f:
#     filtered = list(filter(keep, todos))
#
# json.dump(filtered, f, indent=2)

#

#
# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Год рождения {row[2]}")
#         count += 1
#
#
# with open("data.csv") as f:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Год рождения {row['Год рождения']}")
#         count += 1
#
# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраста"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Маша", 11, 18])
#
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("data_new.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
#
# with open("student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})

#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)
#
# fieldnames = ['hostname', 'location', 'model', 'vendor']
# print(list(data[0].keys()))  # ['hostname', 'location', 'model', 'vendor']
#
# from bs4 import BeautifulSoup
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="row")
# row = soup.find("div", {"class": "row"})
# row = soup.find_all("div", class_="row")[1].find("div", class_="name").text
# row = soup.find_all("div", {"data-set": "salary"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)
# \\\\\\Практика 25.05.2024\\\\\\\\\Парсинг сайтов
#
# from bs4 import BeautifulSoup
#
#
# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
#
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# from bs4 import BeautifulSoup
# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group(0)
#     print(res)
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)
#
# import requests
#
#
# r = requests.get("https://ru.wordpress.org/")
# # print(r)
# # print(r.status_code)
# # print(r.headers)
# # print(r.content)
# print(r.text)


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()
#
# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("div", class_="entry")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
#
# import csv
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def main():
#     for i in range(2, 3):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("div", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3", class_="entry-title").text
#         except AttributeError:
#             name = ""
#
#         try:
#             url = el.find("h3", class_="entry-title").find('a')["href"]
#         except AttributeError:
#             url = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except AttributeError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# if __name__ == '__main__':
#     main()
#

# from parsers import Parser


# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# /////Базы данных СУБД 2.06.2024\\\\\\\\\\\\\\\\\\\\

# # #
# import sqlite3
#
#
# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()
#
# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(       #CREATE TABLE IF NOT EXISTSсоздать таблицу если она еще не существует
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date BLOB)""")

# cur.execute("DROP TABLE users") #удаление таблицы
#SQL запросы
#SQL- как структурированны язык запросов,у него есть свой синтаксис

# Ключево слово SELECT  [ALL (знаяение по умолчанию, без разницы напишем или нет)| DISTINCT(только все уникальные значения ,] * | столбец [, столбец_N]
#FROM таблица_1
# SELECT *
#FROM T1

#Оператор- WHERE условие идет 3 после SELECT
# FROM T1
# WHERE:
#
# Операторы сравнения :=, ==, <>, !=, >=, <=
# Оператор and , or
# Выражение [NOT] BETWEEN начальное _Значение AND конечное
# Выражение [NOT] LIKE  шаблон_строки:
#         % - любое количество символов
#         _ - любое одиночному символу
# Выражение [NOT] GLOB Регулярное_выражение
#         * - любое количество символов
#         ? - соответствует одиному символу
#         . - любое одиночный символ
#         [символы, начальны-конечный символ] - один из перечисленых заданных символов[abc]
#         [начальный символ -конечный символ] - один из диапазона [a-z0-9]
#         [^......] - любой симвро кроме заданных  [^0-9]
#         IS [NOT] NULL -позволяет выбрать все строки NULL(значение является пустым)
#ORDER BY столбец_1 | номер столбца[ASC|DESC]  [,столбец_N]
# LIMIT количество строк OFFSET -смещение строк
#LIMIT [смещение, ] количество строк

#
# import sqlite3
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#
# cur.execute("""CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT "+79090000000",
# age INTEGER CHECK(age > 0 AND age < 100),
# email TEXT UNIQUE
# )""")
# переименовать таблицу
# cur.execute("""
# ALTER TABLE person
# RENAME TO person_table;
# """)

# добавить поле в таблицу
# cur.execute("""
# ALTER TABLE person_table
# ADD COLUMN address NOT NULL DEFAULT "Москва"
# """)
#
# удалить столбец
# cur.execute("""
# ALTER TABLE person_table
# DROP COLUMN address
# """)

# # переименование поля
# cur.execute("""
# ALTER TABLE person_table
# RENAME COLUMN address TO home_address
# """)
#
# удаление таблицы
# cur.execute("""
# DROP TABLE person_table
# """)


# практика от 08.06.24
# Есть три команды для редактирования данных в таблице:

# 1. INSERT  - добавление данных в таблицу
# INSERT INTO имя_таблицы [(столбец_1, столбец_N)]
# VALUES(столбец_1, столбец_N)
 #Например:
# INSERT INTO T1
# VALUES(16, "Юшина", "Секретарь", 2, 1500)

# (если нужно поменять порядок столбцов, то в первой строке в () указать порядок)
# INSERT INTO T1 (ID, Doljnost, Orab,ZP, FName)
# VALUES(17, "Охранники", 1, 2500, "Юшина")
# (если нужно если нужно указывать не все поля  в () указать порядок)
# INSERT INTO T1 (ID, FName)
# VALUES(29, "Николаев")
# INSERT INTO имя_таблицы [(столбец_1, столбец_N)]
# SELECT(столбец_1, столбец_N)
# FROM имя_таблицы (из которой берем данные)
# WHERE

# 2. UPDATE - редактирование данных в таблице
# SET столбец_1 = значение_1,столбец_N = значение_N
# WHERE условие

# 3. DELETE удаление данных из таблицы
# ибо по условию либо все данные
# DELETE FROM имя_таблицы
# WHERE (условие)

# import sqlite3
#
# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     SELECT *
#     FROM T1
#     LIMIT 2, 5
#     """)
#
#     # for i in cur:
#     #     print(i)
#
#     res = cur.fetchone()
#     print(res)
#
#     res2 = cur.fetchmany(4)
#     print(res2)
#
#     res3 = cur.fetchall()
#     print(res3)

#\\\\\\ПРАКТИКА 09.06.2024....\\\\\\\\\
# Логическая база данных
# Физическая база данных
# cur.execute("INSERT INTO toys VALUES(1, 'Самолет', 10, 1500)")
# cur.execute("INSERT INTO toys VALUES(2, 'Мяч', 25, 500)")
# cur.execute("INSERT INTO toys VALUES(3, 'Кукла', 15, 1000)")
# cur.execute("INSERT INTO toys VALUES(4, 'Пистолет', 20, 3500)")
# cur.execute("INSERT INTO toys VALUES(5, 'Чебурашка', 35, 700)")
# cur.execute("INSERT INTO toys VALUES(6, 'Грузовик', 27, 5400)")
# cur.execute("INSERT INTO toys VALUES(7, 'Танк', 50, 2700)")
# cur.execute("INSERT INTO toys VALUES(8, 'Чайный сервиз', 18, 2000)")
# cur.execute("INSERT INTO toys VALUES(9, 'Колобок', 65, 900)")
# cur.execute("INSERT INTO toys VALUES(10, 'Бабочка, 48, 500)")
# ('Dog', 5400),
# ('Pig', 2700),
# ('Caps', 2000),
# ('Flower', 900),
# ('Bird', 500)
#
# import sqlite3
#
# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 36000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
#
# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list)
#
# for car in cars_list:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
#
# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")
#
# con.commit()
# con.close()
#
#
# import sqlite3
#
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()
# #
# import sqlite3
#
# with sqlite3.connect("toy.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS toys(
#         toys_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         Nametoy TEXT,
#         Count TEXT
#         price INTEGER
#     )
#     """)

# import sqlite3
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     # last_row_id = cur.lastrowid
#     # buy_car_id = 2
#     # cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchone()
#     # print(rows)
#     #
#     # rows1 = cur.fetchmany(5)
#     # print(rows1)
#
#     # rows2 = cur.fetchall()
#     # print(rows2)
#
#     for res in cur:
#         # print(res[0], "->", res[1])
#         print(res["model"], "->", res["price"])
#
#
# import sqlite3
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     )""")
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)
#
# import sqlite3
#
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)
#
#
# with sqlite3.connect("car_project.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)
#
# ORM (Object-Relational Mapping) - реляционное сопоставление объектов
# SQLAlchemy ORM


# import os
#
# from sqlalchemy import and_, or_, not_, desc, func
#
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
#
# from models.lesson import Lesson, association_table
# from models.student import Student
# from models.group import Group
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
#     # print(session.query(Lesson).all())
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson):
#     #     print(it.lesson_title)
#     # print("*" * 60)
#     #
#     # print(session.query(Lesson).count())
#     # print("*" * 60)
#     #
#     # print(session.query(Lesson).first())
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson).filter(Lesson.id >= 3):
#     #     print(it.lesson_title)
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
#     #     print(it.lesson_title)
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
#     #     print(it.lesson_title)
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('М%'))):
#     #     print(it.lesson_title)
#     # print("*" * 60)
#     #
#     # print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
#     # print("*" * 60)
#     #
#     # print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
#     # print("*" * 60)
#     #
#     # print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all())
#     # print("*" * 60)
#     #
#     # print(session.query(Student).filter(Student.age.between(16, 17)).all())
#     # print("*" * 60)
#     #
#     # print(session.query(Student).filter(not_(Student.age.between(17, 24))).all())
#     # print("*" * 60)
#     #
#     # for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student).order_by(desc(Student.surname)):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-9'):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(
#     #         Group.group_name).having(func.count(Student.surname) < 25):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student.age).filter(Student.age < 20).distinct():
#     #     print(it)
#     # print("*" * 60)
#
#     # for it in session.query(Lesson):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # i = session.query(Lesson).first()
#     # i.lesson_title = "Информатика"
#     # session.add(i)
#     # session.commit()
#
#     for it in session.query(Lesson):
#         print(it)
#     print("*" * 60)
#
#     # session.add(Lesson(lesson_title="Математика"))
#     # session.commit()
#
#     i = session.query(Lesson).filter(Lesson.lesson_titl e == "Математика").first()
#     session.delete(i)
#     session.commit()
#
#     for it in session.query(Lesson):
#         print(it)
#     print("*" * 60)

# Шаблонизатор (Jinja)

# from jinja2 import Template

# name = "Игорь"
# age = 25
# per = {'name': "Игорь", 'age': 25}
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}.")
# msg = tm.render(p=per)
# # msg = tm.render(n=name, a=age)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# per = Person("Игорь", 25)
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Сочи'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Ярославль'},
#     {'id': 5, 'city': 'Смоленск'},
# ]
#
# link = """<select name="cities">
#     {% for c in cities -%}
#         {% if c.id > 3 -%}
#             <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#         {% elif c.city == "Москва" %}
#             <option>{{ c['city'] }}</option>
#         {% else -%}
#             {{ c['city'] }}
#         {% endif -%}
#     {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#
# # tpl = "Сумма: {{ cs | sum(attribute='price') }}"
# # tpl = "{{ cs | max(attribute='price') }}"
# # tpl = "{{ (cs | min(attribute='price')).model }}"
# # tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)
#
# print(cars)

# Макроопределение

# html = """
# {% macro input_func(name, value, type="text", size=40) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ input_func('name', 'Введите имя') }}</p>
# <p>{{ input_func('psw', 'Пароль',  'password') }}</p>
# <p>{{ input_func('email', 'Электронная почта', 'email') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render(users=persons, title="About Jinja")
#
# print(msg)

# import time
# import math
#
#
# tm = math.floor(time.time())
# print(tm)
