#Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

#Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
#Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print('1.Функция с параметрами по умолчанию:')
print_params()  # 1
print_params(b=25)
print_params(c=[1, 2, 3])

#Создайте список values_list с тремя элементами разных типов.
#Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
print()
print('2.Распаковка параметров:')
values_list = ('Ugansk', 123, True)
print_params(*values_list)
values_dict = {'a': 'text', 'b': False, 'c': 33}
print_params(**values_dict)

#Создайте список values_list_2 с двумя элементами разных типов
#Проверьте, работает ли print_params(*values_list_2, 42)
print()
print('3.Распаковка + отдельные параметры:')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)