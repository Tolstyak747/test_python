from _collections_abc import Callable
import time


def deceleration(func: Callable) -> Callable:
    """Декоратор, который ждет n времени перед запуском основной функции."""

    def wrap(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)

    return wrap


@deceleration
def say_hello(name: str) -> None:
    print(f"{name}, категорически приветствую!")


say_hello("Tom")
