# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (
# красный, желтый, зеленый  ). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

print('Задача 1')
import time
import turtle


class TrafficLight():
    # Аттрибуты класса
    t = turtle.Turtle()

    def __init__(self):
        self.color = ['R','Y','G']
        self.t.color('yellow')
        self.t.circle(50)
        self.t.penup()
        self.t.goto(0, 100)
        self.t.pendown()
        self.t.color('red')
        self.t.circle(50)
        self.t.penup()
        self.t.goto(0, -100)
        self.t.pendown()
        self.t.color('green')
        self.t.circle(50)
    # Методы класса
    def coloring(self, x,y,z,color):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.color(color)
        self.t.begin_fill()
        self.t.circle(z)
        self.t.end_fill()


    def running (self):

        self.color[0]
        self.coloring(0,100,50,'red')
        time.sleep(7)
        self.coloring(0,100,48,'white')
        self.coloring(0, 0,50, 'yellow')
        time.sleep(2)
        self.coloring(0, 0,48, 'white')
        self.coloring(0, -100,50, 'green')
        time.sleep(4)
        self.coloring(0, -100, 48,'white')


a = TrafficLight()
i = 0
while i < 5:
    a.running()
    i +=1



# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

print('Задача 2')


class Road:
    # атрибуты класса
    massa_1m2_1sm = 25
    tolshina_polotna = 5
    massa1 = 0

    # методы класса
    def __init__(self, length, width):
        self._length = length
        self._width = width
        print("Ввести данные длина и ширина")

    def massa(self):
        massa1 = self._width * self._length * self.massa_1m2_1sm * self.tolshina_polotna/1000
        return print(massa1,'тонн')

x = Road(20,5000)
x.massa()

# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
#

class Worker:
    def __init__(self, name, surname, position, x, y):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': x, 'премия': y}

class Position(Worker):
    def get_full_name(self):
        print('Полное имя сотрудника: ', self.name + ' ' + self.surname)

    def get_total_income(self):
        print('Доход с учетом премии = ', self._income['оклад'] + self._income['премия'])

x = Position('Иван', 'Петров', 'строитель',50000, 15000)
x.get_full_name()
x.get_total_income()
x = Position('Сергей', 'Комаров', 'водитель',40000, 18000)
x.get_full_name()
x.get_total_income()

# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
print('Задача 4')
class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина', self.name ,'поехала')
    def stop(self):
        print('Машина', self.name ,'остановилась')
    def turn(self,direction):
        if direction == 0:
            print('Машина', self.name, 'повернула на ', 'налево ')
        else:
            print('Машина', self.name,'повернула на ', 'направо')


class TownCar(Car):
    def show_speed(self):
        print('Городская машина:', self.name, 'Скорость:', self.speed, 'цвет: ', self.color, ' Это не полицейская машина')
        if self.speed > 60:
            print('Превышение скорости на ',   self.speed - 60)
        else:
            print('Скорость машины', self.name,' = ', self.speed)

class WorkCar(Car):
    def show_speed(self):
        print(' Рабочая машина:', self.name, 'Скорость:', self.speed, 'цвет: ',self.color, ' Это не полицейская машина')
        if self.speed > 40:
            print('Превышение скорости на ', self.speed - 40)
        else:
            print('Скорость машины', self.name, ' = ', self.speed)

class SportCar(Car):
    print('Cпортивный автомобиль')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        print('Городская машина:', self.name, 'Скорость:', self.speed, 'цвет: ', self.color,' Это полицейская машина')

x = TownCar(80, 'красная', 'Mazda', True)
x.go()
x.show_speed()
x.turn(30)
x.stop()
y = WorkCar(60, 'синий', 'BMW', False)
y.show_speed()
z = PoliceCar(30,'бело-синяя','Бобик')
z.go()
print('Скорость машины',z.name,z.speed)
z.turn(0)
z.stop()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

print('Задача 5 - Канцеоярские принадлежности')
class Stationery:
    def __init__(self, title = 'рисуем'):
        self.title = title
    def draw(self):
        print('Начинаем рисовать')

class Pen(Stationery):

    def draw(self):
        print('Сейчас мы рисуем', self.title)

class Pencil(Stationery):
    def draw(self):
        print('Сейчас мы рисуем', self.title)

class Hendle(Stationery):
    def draw(self):
        print('Сейчас мы рисуем', self.title)

y = Stationery()
y.draw()
x = Pen('ручкой')
x.draw()
z = Pencil('карандашом')
z.draw()
y = Hendle('маркером')
y.draw()