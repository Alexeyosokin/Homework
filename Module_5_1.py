#Создать класс House
#Вунтри класса House определить метод __init__, в который передаю название и кол-во этажей.
#Внутри метода __init__ создаю атрибуты объекта self.name и self.number_of_floors, присвоить им переданные значения
#Создать метод go_to с параметром new_floor и написать логику внутри него на основе описания задачи
#Создать объект класса House с произвольным названием и количеством этажей
#Вызвать метод go_to у этого объекта с произвольным числом
class House:
    def __init__(self, name, number_of_floors):
        # Инициализируем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка на допустимость этажа
        if 0 < new_floor <= self.number_of_floors:
            # Вывод последовательности чисел от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Сообщение об ошибке
            print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)  # Вывод: 1, 2, 3, 4, 5
h2.go_to(10)  # Вывод: "Такого этажа не существует"