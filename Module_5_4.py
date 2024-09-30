#Задача "История строительства"
#Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов"
#В классе House создать атрибут houses_history = [], который будет хранить названия созданных объектов
#Дополнить метод __new__ так, чтобы:
#Название объекта добавлялось в список cls.houses_history
#Название строения можно взять из args по индексу
#Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"
#Создать несколько объектов класса House и проверить работу методов __del__ и __new__, а также значение атрибута houses_history.
class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Березки', 10)
print(House.houses_history)
h2 = House('ЖК Москворецкий', 20)
print(House.houses_history)
h3 = House('ЖК Дружный', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)