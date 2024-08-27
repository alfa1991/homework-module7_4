import os
import time

# Укажите путь к директории, которую нужно просканировать
directory = r'C:\Users\Ilgiz Agliullin\PycharmProjects\Homeworks\Works'


# Функция для форматирования времени в читаемый вид
def format_time(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


# Обход директории
for root, dirs, files in os.walk(directory):
    print(f'Обход директории: {root}')

    for file_name in files:
        # Полный путь к файлу
        file_path = os.path.join(root, file_name)

        # Получение времени последнего изменения
        last_modified_time = os.path.getmtime(file_path)
        formatted_time = format_time(last_modified_time)

        # Получение размера файла
        file_size = os.path.getsize(file_path)

        # Получение родительской директории
        parent_directory = os.path.dirname(file_path)

        # Вывод информации о файле
        print(f'Файл: {file_name}')
        print(f'  Полный путь: {file_path}')
        print(f'  Время последнего изменения: {formatted_time}')
        print(f'  Размер файла: {file_size} байт')
        print(f'  Родительская директория: {parent_directory}')
        print('-' * 40)
