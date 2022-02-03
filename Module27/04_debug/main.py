from collections.abc import Callable


def debug(func: Callable) ->Callable:
    """Декоратор, который выводит все данные о функции"""
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        print("Вызывается '{}'".format(func.__name__))
        print("'{}' вернула значение '{}'".format(func.__name__, res))
        print(res)
        print()

    return wrap


@debug
def greeting(name, age=None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
