#Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
#Создайте внутри функции пустой список same_words, который пополнится нужными словами.
#При помощи цикла for переберите предполагаемо подходящие слова.
#Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
#После цикла верните образованный функцией список same_words.
#Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.

def single_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words)

    for i in range(len(words)):
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i])
    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)