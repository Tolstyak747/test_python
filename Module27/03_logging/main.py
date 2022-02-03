from collections.abc import Callable
import time


def print_to_screen(func: Callable) -> Callable:
    """Декоратор, который выводит имя и документацию функции"""
    def wrap(*args, **kwargs):
        print(f"{time.asctime()}\n{func.__name__} - {func.__doc__}")
        res = func(*args, **kwargs)
        print()
        return res
    return wrap


@print_to_screen
def say_hello(name: str) -> None:
    """Функция - приветствие!"""
    print(f"{name}, категорически приветствую!")


@print_to_screen
def say_goodbye(name: str) -> None:
    """Функция, которая прощается!"""
    print(f"{name}, всего доброго!")


say_hello("Tom")
say_goodbye("Tom")

#Первую часть задания понял, вторую -нет. нужно через модуль logging?