# Задача "Функциональное разнообразие":
import random

# Даны 2 строки:
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second))
print(list(map(lambda x, y: x == y, first, second)))

# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи:
def get_advanced_writer(file_name):

# Внутри этой функции, напишите ещё одну - write_everything(*data_set),
# где *data_set - параметр принимающий неограниченное количество данных любого типа.

    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice

# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
class MysticBall:
    def __init__(self, *words):
        self.words = words

# В этом классе также определите метод __call__
    # который будет случайным образом выбирать слово из words и возвращать его
    def __call__(self):
        return random.choice(self.words)

# Вывод результата
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Странно')
print(first_ball())
print(first_ball())
print(first_ball())