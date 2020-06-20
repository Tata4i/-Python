# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

print('Задача 1')
def del_func():
    x1 = int(input('Введите первое число: '))
    x2 = int(input('Введите второе число: '))
    while x2 == 0:
        print('Делить на 0 нельзя')
        x2 = int(input('Введите второе число: '))
    return (x1/x2)
print(del_func())


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

print('Задача 2')
def user (name, last_name, year_of_birth, city, email, phone):
    return (print(name + ' ' + last_name + ' ' + year_of_birth + ' ' + city +' ' + email +' '+ phone))

name1 = input('Имя: ')
last_name1 = input('Фамилия: ')
year_of_birth1 = input('Год рождения: ')
city1 = input('город: ')
email1 = input('email: ')
phone1 = input('номер телефона: ')
user (name = name1, last_name = last_name1, year_of_birth = year_of_birth1, city = city1, email = email1, phone = phone1)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

print('Задача 3')
def my_func(a1, a2, a3):
    if a1 >= a2:
        if a2 >= a3:
            summ = a1 + a2
        else:
            summ = a1 + a3
    else:
        if a1 >= a3:
            summ = a2 + a1
        else:
            summ = a2 + a3
    return (print(summ))

b1 = int(input('Введите первое число = '))
b2 = int(input('Введите первое число = '))
b3 = int(input('Введите первое число = '))
my_func(b1,b2,b3)



# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

print('Задача 4')
#
# #  Проверка, что Х действительное положительное число
def is_digitPos(xx):
    try:
        xx=float(xx)
        if float(xx) > 0:
            return True
        else:
            return False
    except:
        return False
#
# #  Проверка, что У целое отрицательное число

def is_digitNeg(xx):
    try:
        xx=float(xx)
        if float(xx) < 0:
            return True
        else:
            return False
    except:
        return False


# Основная функция возведения степень
def my_func(x, y):
    y = abs(float(y))
    i = 1
    z = 1
    while i <= y:
        z = z * float(x)
        i += 1
    return(print('Возведение в степень, способ номер 2', 1 / z))

x = input('Введите число Х = ')
y = input('Введите число Y = ')
# Проверка, что X целое положительное число
while is_digitPos(x) == False:
    x = input('Х должен быть положительным числом. Введите число Х = ')
# y = input('У должно быть отрицательным числом. Введите число Y = ')
while is_digitNeg(y) == False:
    y = input('Y должен быть отризательным числом. Введите число Y = ')

my_func(x,y)


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

print('Задача 5')
print('Ваш специальный символ = Q')
def proverka(y):
    i = 0
    a = 0
    while i < len(y):
        if y[i].isdigit() is True:
            i += 1
        else:
            return False
    return True

def summstrok():
    y = 'xx'
    qc = 0
    while proverka(y) is False and qc == 0:
        x = input('Введите строку чисел разделенную пробелами: ')
        y = x.split()
        qc = y.count ('Q')
        y = y[:y.index('Q')]
        if qc > 0:
            print('Символ Q - вы завершаете программу')
    i = 0
    summ = 0
    while i < len(y):
        summ = summ + int(y[i])
        i = i + 1

    return [summ,qc]

qc = 0
x = 0
while qc == 0:
    z = summstrok()
    x = x+z[0]
    print(x)
    qc = z[1]



# #
# de
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
#
# print('Задача номер 6')
# def int_func():
#     a = input('Введите слово из маленьких латинских букв: ')
#     return a.title()
#
# print(int_func())

# !!!!! нужно сделать проверку всех вводимых значений!!!!
