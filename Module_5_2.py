#Задача "Магические здания"
#Необходимо дополнить класс House следующими специальными методами
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 < new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
            else:
                print('Такого этажа не существует')
#len__(self) - должен возвращать кол-во этажей здания self.number_of_floors
    def __len__(self):
        return self.number_of_floors
#str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"


h1 = House('ЖК Березки', 10)
h2 = House('ЖК Москворецкий', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))