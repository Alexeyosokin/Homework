#Задача "Всё не так уж просто":
#Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Используя этот список составьте второй список primes содержащий только простые числа.
#А так же третий список not_primes, содержащий все не простые числа.
#Выведите списки primes и not_primes на экран(в консоль).
#Пункты задачи:
#Создайте пустые списки primes и not_primes.
#При помощи цикла for переберите список numbers.
#Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
#Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
#В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
#Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)