# Домашнее задание по теме "Try и Except"
# Задание "Программистам всё можно":

def add_everything_up(a, b):
    try:
        result = round(a + b, 3)
    except TypeError:
        result = str(a) + str(b)
    return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))