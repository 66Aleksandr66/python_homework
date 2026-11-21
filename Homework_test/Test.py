import csv


class Dog:
    def __init__(self, name, age):        # заполняет данные новой собаки
        self.name = name
        self.age = age

    def call_dog(self):                   # метод: зовёт ЭТУ собаку
        print(f"Come here, {self.name}!")

    def speak(self):                      # метод: лает
        print("bark bark bark")

dog1 = Dog("Spot", 2)                     # создали собаку, сработал __init__
dog1.call_dog()                           # self = dog1 → Come here, Spot!
dog1.speak()                              # bark bark bark
print(f"dog1's name is {dog1.name}.")     # атрибут через точку

dog2 = Dog("Wally", 4)
dog2.call_dog()                           # self = dog2 → Come here, Wally!
dog2.age += 1                             # меняем атрибут: 4 → 5
print(dog2.age)                           # 5

class Cars:
    _total_km = 0
    def __init__(self, brand, mileage):
        self.brand = brand
        self.mileage = mileage
    def drive(self,km):
        self.mileage += km
        Cars._total_km += km
        print(f"{self.brand} проехала {km}, пробег теперь {self.mileage}")
    @classmethod
    def get_total_km(cls):
        return cls._total_km
car1 = Cars("Honda", 75000)
car2 = Cars("Lada", 55755)
car1.drive(100)
car1.drive(250)
print(Cars.get_total_km())

class BigDog(Dog):
    def fetch(self):
        print("Got it")
    def speak(self):
        print("woof woof woof")
dog1 = Dog("Spot", 2)
dog3 = BigDog("Butch", 3)

dog1.speak()   # bark bark bark   — версия Dog
dog3.speak()   # Woof Woof Woof   — версия BigDog

class BigDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age)   # пусть Dog заполнит name и age
        self.weight = weight          # своё — заполняем сами
def print_name(a):
    print(a)
#
# print_name("ccsdcdsc")

#
# def make_tea():
#     print("Завариваю чай")
#
# def make_tea_full():            # новая функция
#     print("Кипячу воду")        # что-то ДО
#     make_tea()                  # вызываем исходную функцию
#     print("Готово!")            # что-то ПОСЛЕ
#
# def with_steps(func):           # func — параметр, сюда придёт ЛЮБАЯ функция
#     print("Кипячу воду")        # ДО
#     func()                      # вызываем то, что пришло в func
#     print("Готово!")            # ПОСЛЕ
#
# # with_steps(make_tea)            # передаём make_tea БЕЗ скобок
#
# def with_steps(func):           # ДЕКОРАТОР: принимает функцию
#     def wrapper():              # ОБЁРТКА: новая функция, создаём внутри
#         print("Кипячу воду")    #   ДО
#         func()                  #   вызов ИСХОДНОЙ функции из параметра func
#         print("Готово!")        #   ПОСЛЕ
#     return wrapper              # отдаём обёртку, БЕЗ скобок (не вызываем)
# def make_tea():
#     print("Завариваю чай")
#
# # new_tea = with_steps(make_tea)  # упаковали: в new_tea лежит wrapper
# # new_tea()                       # вызвали обёртку
#
# # def make_tea():
# #     print("Завариваю чай")
# #
# # make_tea = with_steps(make_tea)  # make_tea теперь указывает на wrapper
#
# @with_steps                       # = make_tea = with_steps(make_tea)
# def make_tea():
#     print("Завариваю чай")
# make_tea()
#
# def repeat_with_prefix(prefix, num_repeats):       # ФАБРИКА: настройки
#     def decorator(func):                           # ДЕКОРАТОР: функция
#         def wrapper(*args, **kwargs):              # ОБЁРТКА: аргументы
#             for _ in range(num_repeats):           #   повторить num_repeats раз
#                 result = func(*args, **kwargs)     #   вызвать исходную функцию
#                 print(f"{prefix} {result}")        #   напечатать с префиксом
#         return wrapper
#     return decorator
#
# @repeat_with_prefix(">>", 3)                       # greet = repeat_with_prefix(">>", 3)(greet)
# def greet(name):
#     return f"Hello, {name}!"
#
# greet("Amanda")


# def my_decorator(func):
#     def wrapper():
#         print("Hello!")
#         func()
#         print("World!")
#     return wrapper
# @my_decorator
# def print_name():
#     print("John")
#
# print_name()


with open("../csv/employees.csv", 'r', newline='') as employees_table:
    employees = list(csv.reader(employees_table))
    first_indx = employees[0].index("first_name")
    last_indx = employees[0].index("last_name")
full_name = [row[first_indx] + ' ' + row[last_indx] for row in employees[1:]]
filter_list = [x for x in full_name if 'e' in x]
print(full_name)
print(filter_list)
    # for i in reader:
    #     print(i[1], i[2], sep =' ')
