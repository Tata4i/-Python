# # 1. Поработайте с переменными, создайте несколько, выведите на экран,
# # запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
# name = input('Как вас зовут? ')
# age = int(input('сколько вам лет? '))
# dateBirth = input('Когда ваш день рождения? ')
# print('Вас зовут ',name, 'и вам сейчас', age)
#
# # 2. Пользователь вводит время в секундах.
# # Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# # Используйте форматирование строк.
# hour = 00
# min = 00
# sec = int(input('Введите время в секундах: '))
# hour = sec // (60*60)
# min = (sec - hour*60*60) // 60
# sec = sec - hour*60*60 - min*60
# print(hour ,':', min,':',sec,'.')
#
# # 3. Узнайте у пользователя число n.
# # Найдите сумму чисел n + nn + nnn.
# # Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#
# n = int(input('Введите любое число = ' ))
# n_str = str(n)
# print(n_str)
# nn_str = n_str +  n_str
# print(nn_str)
# nnn_str = nn_str + n_str
# print(nnn_str)
# sum = int(n_str) + int(nn_str) + int(nnn_str)
# print(sum)
#
# # 4. Пользователь вводит целое положительное число.
# # Найдите самую большую цифру в числе.
# # Для решения используйте цикл while и арифметические операции.
#
# n = int(input('Введите целое положительное число = ' ))
# x = 0
# z = 0
# while n <= 0:
#     print('Нужно ввести целое положителное число')
#     n = int(input('Введите целое положительное число = '))
# while n // 10 > 0:
#     x = n % 10
#     n = n // 10
#     if x >= z:
#         z = x
# else:
#     print(z)
#
# # 5. Запросите у пользователя значения выручки и издержек фирмы.
# # Определите, с каким финансовым результатом работает фирма
# # (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# # Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# # вычислите рентабельность выручки (соотношение прибыли к выручке).
# # Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
# fin_res = 0
# profit = int(input('Введите значение вашей выручки: '))
# costs = int(input('Введите знаение ваших издержек: '))
# fin_res = profit - costs
# if fin_res > 0:
#     print('Вы работаете с прибылью = ', fin_res)
#     print('Рентабельность выручки = ', fin_res/profit)
#     fte = int(input('Введите количество сотрудников = '))
#     print('Прибыль фирмы в расчете на 1 сотрудника = ', fin_res/fte)
# else:
#     fin_res = 0 - fin_res
#     print('Вы работаете с убытками = ', fin_res)
#
# # 6. Спортсмен занимается ежедневными пробежками.
# # В первый день его результат составил a километров.
# # Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# # Требуется определить номер дня,
# # на который общий результат спортсмена составить не менее b километров.
# # Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# # Например: a = 2, b = 3.
# # Результат:
# # 1-й день: 2
# # 2-й день: 2,2
# # 3-й день: 2,42
# # 4-й день: 2,66
# # 5-й день: 2,93
# # 6-й день: 3,22
# #
# # # Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
#
# a = int(input('Введите колиество километров a = '))
# b = int(input('Введите колиество километров b = '))
# x = 1
# while b - a > 0:
#     a = a + 0.1*a
#     x = x + 1
#     print(x,' день:', a)
# else:
#     print('На', x, 'день спортсмен достиг результата = ', b,'километров')

#
# # Lesson_2
#
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

i = 0
moi_spisok = ['red', 'green', 'true', 1, 5]
x = len(moi_spisok)
print('Количество элемнтов в списке = ', x)
while i <= x:
    print ('Тип элемента ', i, '=', type (moi_spisok[i]))
    i = i+1

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
#
x = []
i = 0
y = input('Заполните, пожалуйста, список: ')
x = y.split(' ')
print(x)
z = int(len(x))
print(z // 2)
if z % 2 == 0:
    while i < z:
        a = x[i]
        x[i]= x[i+1]
        x[i+1] = a
        i=i+2
    print('Получился список', x)
else:
    i=0
    while i < z-1:
        a = x[i]
        x[i] = x[i + 1]
        x[i + 1] = a
        i = i + 2
    print('Получился список', x)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
x = int(input('Введите месяц (число от 1 до 12), пожалуйста:  '))
months = ['Январь', 'Февраль','Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Cентябрь','Октябрь', 'Ноябрь', 'Декабрь']
print(months[x-1])
god={'Зима': [12,1,2], 'Весна': [3,4,5], 'Лето': [6,7,8], 'Осень': [9,10,11]}
for i in god:
    if x in god [i]:
        print('Месяц', x, '-', months[x-1], 'относится к времени года: ', i)

# 4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

x = input('Введите строку из нескольких слов, разделенных пробелами: ')
y = x.split(' ')
print (y)
i = 0
z = len(y)
print (z)
while i < z:
    i = i + 1
    print (i, y[i-1][:9])




# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


my_list = [7,5,3,3,2]
i = 0
y = len(my_list)
x = int(input('Введите число  '))
while i < y:
    if x > my_list[i]:
        my_list.insert(i,x)
        print(my_list)
        break
    i=i+1


# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
import pprint
b = {}
a = ['Название товара', 'Цена','Количество','Единица измерения']
d = []
k = 1
for i in a:
    x = input('Введите ' + i + '  ')
    b.update({i:x})
c = (k,b)
d.append(c)
z = input ('Хотите ввести еще товар? Напишите да или нет: ')
while z == 'да':
    b = {}
    k = k + 1
    for i in a:
        x = input('Введите ' + i + '  ')
        b.update({i:x})
    c = (k, b)
    d.append(c)
    z = input ('Хотите ввести еще товар? Напишите да или нет: ')
else:
   print('Словарь готов', d)

for i in d:
    print (i)


