# Домашнее задание
# Напишите и запустите программу. которая выводит строку  "Hello world!"
# Напишите программу, которая на входе получает имя пользователя,
# cохраняет его в переменную user_name и выводит строку  "Hello {user_name}!"
# Напишите программу, которая на входе получает 2 числа, производит с ними
# арифметическую операцию(на ваше усмотрение), и выводит “Результат = {результат}”.

# print('"Hello world!"')
#
# user_name = input("Please enter user name: ")
# print(f"Hello,{user_name}!")
#
# number1 = int(input("Please, enter any first number: "))
# number2 = int(input("Please, enter any second number: "))
# print(f"Result = {number1} / {number2}")
# print(f"Result = {number1/number2}")

# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

# healf= int(input("Please enter your healf point: "))
# if healf <= 0:
#     print (f"False")
# else:
#     print (f"True")

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”,
# а иначе - “Нечетное”

# number = int(input("Введите число для проверки на четность: "))
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без остатка
# на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, он также считается
# високосным (1200, 2000)

# year = int(input("Введите год для проверки високосность"))
# if year % 4 != 0:
#     print('Год не високосный')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('Год високосный')
#     else:
#         print('Год не високосный')
# else:
#     print('Год високосный')
#
# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений
# нужно ввести с помощью input()
#
# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное
# арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# my_list[2]
# print(my_list[2])
# #
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# total = 0
# for num in list_1:
#     try:
#         total += num
#     except TypeError:
#         print(f"Элемент {num} не является числом")
# print(f"Сумма чисел в списке: {total}")

#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# for item in list_1:
#     if isinstance(item, str) and 'a' in item:
#         print(item)

# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
# lst = ['cat', 'dog', 'horse', 'cow']
# print(tuple(lst))

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input("Введите список членов первой семьи через запятую: ").split(',')
# family_2 = input("Введите список членов второй семьи через запятую: ").split(',')
# if len(family_1) > len(family_2):
#     print(f"Семья {family_1} больше")
# elif len(family_2) > len(family_1):
#     print(f"Семья {family_2} больше")
# else:
#     print("Equal")
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение


# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# total = sum(my_dictionary.values())
# print(total)

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# Set = [1, 2, 3, 4, 5, 3, 2, 1]
# Set = set([1, 2, 3, 4, 5, 3, 2, 1])
# print(Set)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# a = set(set1)
# b = set(set2)
# #      - найдите значения, которые встречаются в обоих множествах
# print(a&b)
# #      - найдите значения, которые не встречаются в обоих множествах
# print(a^b)
# #      - проверьте являются ли эти множества подмножествами друг друга
# print(a<b)

# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
from math import sqrt
def square (a):
    return (4*a,a**2,a*sqrt(2))
print(square(a=2))
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение.
#      Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# def func(**kwargs):
#     for key, value in kwargs.items()
#         print(f"{key}: {value}")
# func(name='John', last_name='Smith', age=35, position='web developer')
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
# содержащий только положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# list2=list(filter(lambda a: a>=0, my_list))
# print(list2)
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# my_list = [20, -3, 15, 2, -1, -21]
# import functools
# print (functools.reduce(lambda a, b : a * b, my_list))
# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
