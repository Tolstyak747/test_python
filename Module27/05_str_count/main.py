from collections.abc import Callable


def counter(func: Callable) -> Callable:
    """Декоратор, подсчитывающий кол-во вызовов функции"""
    def wrap(*args, **kwargs):
        wrap.counter += 1
        print("Кол-во вызовов функции {} - {}".format(func.__name__, wrap.counter))
        func(*args, **kwargs)
        print()

    wrap.counter = 0
    return wrap


@counter
def say_hello(name: str) -> None:
    """Функция - приветствие!"""
    print(f"{name}, категорически приветствую!")


say_hello("Tom")
say_hello("Tom")
say_hello("Tom")
say_hello("Tom")
say_hello("Tom")
