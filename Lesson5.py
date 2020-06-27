# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
print('Задача 1')
f = open('text1.txt', 'w')
print('введите данные')
str_list = []
x = 1
while x!='':
    x = input()
    f.writelines(str(x) + '\n')
f.close()

# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
from typing import List
print('Задача 2')
f = open('task2.txt', 'r')
content = f.readlines()
x = content
len_str = []
print(content)
print('В вашем файле количество строк = ', len(x))
i = 0
print('Выводим обычным циклом')
while i < len(x):
    x[i] = str(x[i])
    a = x[i].split()
    print('В строке', i+1, 'содержится', len(a),'слова')
    i = i + 1
len_str = [len(y.split()) for y in x]
print('Выводим генератором')
print(len_str)
f.close()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

print('Задача 3')
f = open('task3.txt', 'r')
x = f.readlines()
print(x)
# print(type(x))
quanstrok = len(x)
# print(quanstrok)
i = 0
s = 0
print('Сотрудники, имеющи зарплату меньше 20000 руб:')
while i < len(x):
    x[i] = str(x[i])
    x[i] = x[i].split()
    if float(x[i][1]) < 20000:
        print(x[i][0])
    s = float(x[i][1]) + s
    i += 1
print('Средняя величина дохода всех сотрудников = ', round(s/quanstrok,2))
f.close()

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#
print('Задача 4')

f = open('test4.txt', 'r', encoding='utf-8')
d = open('test4.1.txt', 'w', encoding='utf-8')
x = f.readlines()
print(x)
# print(type(x))
i = 0
from translate import Translator
translator= Translator(from_lang="en",to_lang="ru")
a = ' '
while i < len(x):
    x[i] = x[i].split()
    # print(len(x[i]))
    x[i][0] = translator.translate(x[i][0])
    print(x[i])
    x[i] = a.join(x[i])+'\n'
    d.writelines(x[i])
    i += 1
f.close()

# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
print('Задача 5')
f = open('test5.txt', 'w')

from random import randint
# Составляем исходный список из 10 элементов
my_list = ''
for i in range(1, 10):
    my_list = my_list + str(randint(0,100)) + " "
f.writelines(my_list)
print('Исходный список = ', my_list)
f.close()
f = open('test5.txt', 'r')
s = 0
x = f.readlines()
x = x[0].rstrip()
x = x.split(' ')
for i in x:
    s = s + int(i)
print('Сумма числе в файле = ', s)
f.close()

# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и
# лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
print('Задача 6')
f = open('test6.txt', 'r')
x = f.readlines()
print(x)
a = {}
k = 0
s = 0
for i in x:
    z = i.split(':')
    s = 0
    # print('Ищу цифры',i)
    # num_list = []
    num = ''
    for sym in i:
        if sym.isdigit():
            num = num + sym
        else:
            if num != '':
                s = int(num) + s
                # num_list.append(int(num))
                num = ''
    if num != '':
        # num_list.append(int(num))
        s = s + int(num)
    a.update({z[0]:s})
print('Ваш словарь = ', a)
f.close()

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

print('Задача 7')

f = open('test7.txt', 'r')
a = {}
x = f.readlines()
print(x)
q = len(x)
print(q)
profit = 0
total_profit = 0
avg_profit = 0
i = 0
for i in x:
    i = i.split()
    # print(i)
    profit = float(i[2]) - float(i[3])
    a.update({i[0]: profit})
    print(profit)
    if profit > 0:
        total_profit = total_profit + profit
a['average profit'] = round(total_profit,2)/q
print(a)
# print('Средняя прибыль всех компаний = ', round(total_profit,2)/q)
import json
with open("test7.json", "w") as testjson:
    json.dump(a, testjson)
f.close()