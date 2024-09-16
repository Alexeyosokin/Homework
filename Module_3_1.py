calls = 0
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
def count_calls ():
    global calls
    calls+=1
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
# Вывод результата
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)