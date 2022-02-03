import os
from collections.abc import Iterable


def get_pyfiles(directory: str) -> list:
    """Создаем список из файлов с расширением .ру"""
    ls = []
    for elem in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, elem)):
            full = os.path.join(directory, elem)
            ls.append(isfile(full))
    return ls


def isfile(path: str) -> str:
    """Проверка файла под наши требования"""
    for elem in os.listdir(path):
        full = os.path.join(path, elem)
        if os.path.isfile(full) and full.endswith(".py"):
            return full
        elif os.path.isdir(full):
            isfile(full)


def count_lines(f_list: list) -> Iterable:
    """Функция-генератор, которая показывает кол-во строк в каждом файле"""
    for file in f_list:
        count = 0
        with open(file, "r") as py_file:
            for i_line in py_file:
                if not i_line.startswith("#"):
                    count += 1
            yield count


work_dir = os.path.abspath(r"C:\Users\хакер\PycharmProjects\python_babasik\python_basic\Module15")
rez = get_pyfiles(work_dir)
data = count_lines(rez)
for item in data:
    print(item)
