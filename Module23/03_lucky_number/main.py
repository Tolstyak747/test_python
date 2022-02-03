import random

n_ls = []
with open("result.txt", "w") as file:
    while sum(n_ls) < 777:
        a = random.randint(1, 13)
        print(a)
        n = int(input("Введите число: "))
        if a == 1:
            raise BaseException
        else:
            n_ls.append(n)
            file.write(str(n) + " ")


# в функциональном стиле
import os
import random

MAGIC_NUMBER = 777


def get_file_path(out_filename):
    return os.path.join(os.path.abspath('.'), out_filename)


def is_exception_raise():
    return random.randint(1, 13) == 7


def pre_init(file_path):
    try:
        os.remove(file_path)
    except OSError as ex:
        print(ex)
        print('Данный файл не может быть удален')


def main(out_filename):
    out_filepath = get_file_path(out_filename)
    # pre_init(out_filepath)

    with open(out_filepath, 'w') as out_fd:
        magic_sum = 0
        while magic_sum < MAGIC_NUMBER:
            try:
                input_number = int(input('Введите число: '))
                magic_sum += input_number
            except (ValueError, KeyboardInterrupt) as ex:
                print(ex)
                print('Возникли проблемы при вводе.')
                print('Попробуйте еще раз')

            if is_exception_raise():
                raise Exception('Вас постигла неудача!')

            print('Вы успешно выполнили условие для выхода из порочного цикла!')


main('out_file.txt')
