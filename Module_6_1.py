# родительский класс 1
class Animal:

    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def __str__(self):
        s = f'Животное: {self.name} '
        if self.alive:
            s += '(живое, '
            if self.fed:
                s += 'накормленное)'
            else:
                s += 'голодное)'
        else:
            s += '(мертвое)'
        return s

# родительский класс 2
class Plant:

    edible = False

    def __init__(self, name):
        self.name = name

'''
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
'''

# дочерний класс 1:
class Mammal(Animal):

    #def __init__(self, name):
    #    self.name = name

    def eat(self, food: Plant):
        if food.edible:
            print(f'Млекопитающее "{self.name}" съело "{food.name}".')
            self.fed = True
        else:
            print(f'Млекопитающее "{self.name}" не стало есть "{food.name}".')
            self.alive = False


# дочерний класс 2:
class Predator(Animal):

    def eat(self, food: Plant):
        if food.edible:
            print(f'Хищник "{self.name}" съел "{food.name}".')
            self.fed = True
        else:
            print(f'Хищник "{self.name}" не стал есть "{food.name}".')
            self.alive = False

# дочерний класс 3:
class Fruit(Plant):

    edible = True

    def __init__(self, name):
        self.name = name

    def __str__(self):
        s = f'Растение: {self.name} '
        if Fruit.edible:
            s += '(съедобное)'
        else:
            s += '(несъедобное)'
        return s

# дочерний класс 4:
class Flower(Plant):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        s = f'Растение: {self.name} '
        if Flower.edible: # <- вот здесь не уверен!
            s += '(съедобное)'
        else:
            s += '(несъедобное)'
        return s

def main_from_example():
    #Выполняемый код(для проверки):
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

def main():
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1)
    print(a2)
    print(p1)
    print(p2)

    a1.eat(p1)
    a2.eat(p2)

    print(a1)
    print(a2)

if __name__ == '__main__':
    main()
