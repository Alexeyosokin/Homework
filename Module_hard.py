# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать
# методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы
# взаимодействия (методы) - геттеры и сеттеры.
#
# Подробное ТЗ:
#
# Атрибуты класса Figure:
#   - sides_count = 0
#
# Каждый объект класса Figure должен обладать следующими атрибутами:
#
# Атрибуты(инкапсулированные):
#   - __sides(список сторон (целые числа)),
#   = __color(список цветов в формате RGB)
# Атрибуты(публичные):
#   - filled(закрашенный, bool)
#
# И методами:
#   - get_color, возвращает список RGB цветов.
#   - __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность
#     переданных значений перед установкой нового цвета. Корректным цвет:
#     все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
#   - set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие
#     значения, предварительно проверив их на корректность. Если введены некорректные данные,
#     то цвет остаётся прежним.
#   - __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если
#     все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех
#     остальных случаях.
#   - get_sides должен возвращать значение я атрибута __sides.
#   - __len__ должен возвращать периметр фигуры.
#   - set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
#     то не изменять, в противном случае - менять.
#
# Атрибуты класса Circle:
#   - sides_count = 1
#
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
#   - Все атрибуты и методы класса Figure
#   - __radius, рассчитать исходя из длины окружности (одной единственной стороны).
#   - get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
#
# Атрибуты класса Triangle:
#   - sides_count = 3
#
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
#   - Все атрибуты и методы класса Figure
#   - get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
#
# Атрибуты класса Cube:
#   - sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
#   - Все атрибуты и методы класса Figure.
#   - Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
#   - Метод get_volume, возвращает объём куба.


from math import pi as PI

class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__sides = sides        # список сторон (целые числа)
        self.__color = color        # (список цветов формате RGB)
        self.filled = None          # (закрашенный, bool)

    def __len__(self):              # должен возвращать периметр фигуры.
        if self.sides_count == 0:
            return 0
        else:
            sum = 0
            for item in self.__sides:
                sum += item
            return sum

    def __is_valid_color(self, color):  # принимает параметры r, g, b, который проверяет корректность
                                        # переданных значений перед установкой нового цвета.
                                        # Корректным цвет: все значения r, g и b - целые числа
                                        # в диапазоне от 0 до 255 (включительно).

        for item in color:
            if not isinstance(item, int) or item < 1 or item > 255:
                return False

        return True

    def set_color(self, *new_color): # принимает параметры r, g, b - числа и изменяет атрибут __color на
                                    # соответствующие значения, предварительно проверив их на корректность.
                                    # Если введены некорректные данные, то цвет остаётся прежним.

        if self.__is_valid_color(new_color):
            self.__color = list(new_color)

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, new_sides):  # принимает неограниченное кол-во сторон,
                                            # возвращает True, если все стороны целые положительные числа
                                            # и кол-во новых сторон совпадает с текущим, False - во всех
                                            # остальных случаях.

        if self.sides_count != len(new_sides):
            return False

        for item in new_sides:
            if not isinstance(item , int):
                return False

        return True

    def set_sides(self, *new_sides):  # должен принимать новые стороны, если их количество не равно
                                      # sides_count, то не изменять, в противном случае - менять.

        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):        # должен возвращать значение атрибута __sides
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):  # (Цвет, стороны)
        if len(sides) != 1:
            sides = [1]

        super().__init__(color, sides)
        self.__radius = self.get_sides()[0] / (2 * PI)      # рассчитать исходя из длины окружности
                                                            # (одной единственной стороны).

    def set_sides(self, new_sides):
        super().set_sides(new_sides)
        self.__radius = self.get_sides()[0] / (2 * PI)

    def get_square(self):       # `возвращает площадь круга (можно рассчитать как через длину,
                                # так и через радиус).

        return self.__radius ** 2 * PI

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):  # (Цвет, стороны)
        if len(sides) != 3:
            sides = [1] * 3

        super().__init__(color, sides)

    def get_square(self):       # возвращает площадь треугольника.(можно рассчитать по формуле Герона)
        sides = self.get_sides()
        p = (sides[0] + sides[1] + sides[2]) / 2
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):  # (Цвет, стороны)
        if len(sides) != 1:
            sides = [1]
        sides = sides * 12  # Переопределить __sides сделав список из 12 одинаковых сторон
                                 # (передаётся 1 сторона)

        super().__init__(color, sides)

    def get_volume(self):  #возвращает объём куба.
        return self.get_sides()[0] **3


def start():
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    triangle1 = Triangle((111, 70, 65), 6, 6, 6)
    cube1 = Cube((222, 35, 130), 8)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())

    triangle1.set_color(110, 132, 154)  # Изменится
    print(triangle1.get_color())

    cube1.set_color( 300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    triangle1.set_sides(12, 12, 12)  # Изменится
    print(triangle1.get_sides())

    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())

    # Проверка периметра
    print(len(circle1))
    print(circle1.get_square())

    print(len(triangle1))
    print(triangle1.get_square())

    # Проверка объёма (куба):
    print(len(cube1))
    print(cube1.get_volume())

if __name__ == '__main__':
    start()