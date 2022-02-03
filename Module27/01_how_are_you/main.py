from collections.abc import Callable


def how_are_you(func: Callable) -> Callable:
    """Декоратор, который мешает)"""
    def wrap(*args, **kwargs):
        question = input("Как твои дела? ")
        print("А у меня что-то не очень! Ладно, держи свою функцию.")
        return func(*args, **kwargs)
    return wrap


@how_are_you
def say_hello(name: str) -> None:
    """Функция - приветствие!"""
    print(f"{name}, категорически приветствую!")


say_hello("Tom")
