# Домашнее задание по теме "Декораторы"
# объявление функции декоратора is_prime
def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        # условие проверки числа на простое / составное и вывод на консоль
        if all((x % i) != 0 for i in range(2, int(x ** 0.5)+1)):
            print('Простое')
        else:
            print('Составное')
        # возврат результата func(*args)
        return x
    # возврат функции wrapper
    return wrapper

# обращение к функции декоратору
@is_prime
# объявление функции sum_three принимающая любое количество числовых аргументов
# и производящая их суммирование
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res


result = sum_three(2, 3, 6)
print(result)