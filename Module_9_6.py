# Домашнее задание по теме "Генераторы"

# Напишите функцию-генератор all_variants(text).
def all_variants(text):
    # Опишите логику работы внутри функции all_variants.
    for x in range(len(text)):
        for r in range(len(text) - x):
            yield text[x:r + x + 1]


# Вызовите функцию all_variants и выполните итерации.

a = all_variants("abc")
for i in a:
    print(i)