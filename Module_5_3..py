#Задача "Нужно больше этажей"
#Необходимо дополнить класс House следующими специальными методами
#__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other
#Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей
#__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self
#__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова)
class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.nFloors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor > self.nFloors:
            print('Такого этажа не существует!')
        else:
            if new_floor < 1:
                for f in range(1, new_floor-1, -1):
                    print('Спускаемся:', f)
            for f in range(1, new_floor+1):
                print('Поднимаемся:', f)

    def __len__(self):
        return self.nFloors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.nFloors}.'

    def __eq__(self, other):
        return self.nFloors == other.nFloors

    def __lt__(self, other):
        #(<)
        return self.nFloors < other.nFloors

    def __le__(self, other):
        #(<=)
        return self.nFloors <= other.nFloors

    def __gt__(self, other):
        #(>)
        return self.nFloors > other.nFloors

    def __ge__(self, other):
        #(>=)
        return self.nFloors >= other.nFloors

    def __ne__(self, other):
        #(!=)
        return self.nFloors != other.nFloors

    def __add__(self, value):
        self.nFloors += value
        return self

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other


def main():
    h1 = House('ЖК Березки', 10)
    h2 = House('ЖК Москворецкий', 20)

    print(h1)
    print(h2)

    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__


if __name__ == '__main__':
    main()
