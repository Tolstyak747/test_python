import os.path


def save(text):
    dirs = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел): ").split(" ")
    path_to_dirs = os.path.abspath(os.path.join(os.path.sep))

    for i in dirs:
        path_to_dirs = os.path.join(path_to_dirs, i)

    file_name = input("Введите имя файла: ")
    file_name += ".txt"
    return path_to_dirs, file_name


def write_file(file, text):
    with open(file, "w") as f:
        f.write(text)



text = input("Введите текст: ")

path, name = save(text)
complete_name = os.path.abspath(os.path.join(path, name))


if not os.path.exists(path):
    print("Неверно указан путь!")
else:
    if os.path.isfile(complete_name):
        print("Уже есть!")
        question = input("Хотите перезаписать? ").lower()
        if question == "да":
            write_file(complete_name, text)
            print("Файл успешно перезаписан!")
        else:
            print("На нет и суда нет)")
    else:
        write_file(complete_name, text)
        print("Файл успешно сохранен!")

# зачет
