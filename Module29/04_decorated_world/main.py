from collections.abc import Callable


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    def decorator(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(*arg_foo, **kwargs_foo):
        print("Переданные в арги и кварги в декоратор: {}{}".format(args, kwargs))
        res = func(*arg_foo, **kwargs_foo)
        return res

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


@decorated_decorator(100, 300, 500, "abc")
def say_hello(name):
    print("Привет, {}".format(name))


decorated_function("Юзер", 101)
print()
say_hello("Андрей")

# Принято
