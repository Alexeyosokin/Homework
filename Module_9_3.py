# Домашнее задание - создать 2 генераторных сборки:

# 1
first = ['Strings', 'Student', 'Computers']
# 2
second = ['Строка', 'Урбан', 'Компьютер']

# Списковые словарные сборки которыее:
# высчитывает разницу длин строк из списков first и second
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))

# содержит результаты сравнения длин строк в одинаковых позициях из списков first и second
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результата
print(list(first_result))
print(list(second_result))