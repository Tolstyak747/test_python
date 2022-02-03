import os


def gen_files_path(file, path=r"D:") -> str:
    for root, dirs, files in os.walk(path):
        for name in files:
            fullname = os.path.join(root, name)
            yield fullname
            if name == file:
                return


gen = gen_files_path("Scan.dll")

for i in gen:
    print(i)

#Если я правильно понял задание, то мы создаем функцию, туда указываем файл, и потом начинаем искать этот файл, по пути выводя на экран пути всех файлов пока не наткнемся на наш файл.


# TODO поняли правильно. Только вот заканчивать иетрации надо через вызов исключения StopIteration
import os
from typing import Iterator


def root_path() -> str:
    return os.path.abspath(os.sep)


def gen_files_path(search_folder_name: str, root_dir: str = None) -> Iterator[str]:
    if root_dir is None:
        root_dir = root_path()

    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isfile(item_path):
            yield item_path
        if os.path.isdir(item_path):
            folder_name = os.path.basename(item_path)
            if folder_name == search_folder_name:
                print(f'Искомая директория {folder_name} найдена {item_path}')
                raise StopIteration
            for file_path in gen_files_path(search_folder_name, item_path):
                yield file_path


def main():
    """
    Проход по каталогу с решениями
    И поиск текущей директории

    :return:
    """

    current_folder = os.path.basename(os.path.abspath('./'))

    for file_path in gen_files_path(current_folder):
        print(file_path)


main()
