# Домашнее задание по теме "Списковые, словарные сборки"

# Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк
first_result = [x for x in first_strings if len(x) >= 5]

# В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов
# (кортежей) одинаковой длины.

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

# В переменную third_result запишите словарь созданный при помощи сборки,
# где парой ключ-значение будет строка-длина строки.
combined_strings = first_strings + second_strings

# Условие записи пары в словарь - чётная длина строки.
third_result = {x: len(x) for x in combined_strings if len(x) % 2 == 0}

# Вывод результата
print(first_result)
print(second_result)
print(third_result)