from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime


def show_path_info(directory):
    '''выводит информацию о всех файлах в указанной директории'''
    for root, dirs, files in walk(directory):
        for file in files:
            filepath = join(root, file)
            filetime = getmtime(filepath)
            formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
            filesize = getsize(filepath)
            parent_dir = dirname(filepath)
            # parent_dir = root  # то же самое
            print(f'Обнаружен файл: {file},',
                  f'Путь: {filepath},',
                  f'Размер: {filesize} байт,',
                  f'Время изменения: {formatted_time},',
                  f'Родительская директория: {parent_dir}')


if __name__ == '__main__':
    show_path_info('.')