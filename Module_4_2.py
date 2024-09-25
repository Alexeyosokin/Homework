#Самостоятельная работа по уроку "Пространство имен"
#Создайте новый проект в PyCharm
#Запустить созданный проект
#Моя задача:
#Создать новую функцию test_function
#Создать внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
#Вызвать функцию inner_function внутри функции test_function
#Попробывать вызывать inner_function вне функции test_function и посмотреть на результат выполнения программы

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
inner_function()
# при выводе появится ошибка имя "inner_function" не определено в глобальном пространстве имен