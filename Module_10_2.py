#Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами
#Атрибут name - имя рыцаря. (str)
#Атрибут power - сила рыцаря. (int)
#Создайте класс Knight с соответствующими описанию свойствами
#Создайте и запустите 2 потока на основе класса Knight
#Выведите на экран строку об окончании битв

from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int, enem_num: int = 100):
        super().__init__()
        self.name = name  # имя рыцаря
        self.power = power  # сила рыцаря
        self.enem_num = enem_num  # количество врагов

    def run(self):
        print(f'{self.name}, на нас напали!')
        day_num = 0
        while self.enem_num > 0:
            sleep(1)
            day_num += 1
            self.enem_num -= self.power
            print(f'{self.name} сражается {day_num} день(дня)...,',
                  f'осталось {self.enem_num} воинов.')
        print(f'{self.name} одержал победу спустя {day_num} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')