from collections.abc import Callable

user_permissions = ['admin']


def check_permission(user: str, us_per="".join(user_permissions)) -> Callable:
    def check(func: Callable) -> Callable:
        """Декоратор - проверка возможностей пользователя"""

        def wrapper(*args, **kwargs):
            # TODO У нас все-таки список прав дан, а в user может храниться только одно из них
            #   Поэтому предлагаю использовать оператор in вместо ==
            if user == us_per:
                res = func(*args, **kwargs)
                return res
            else:
                raise PermissionError("У пользователя недостаточно прав, чтобы выполнить функцию {func}".format(
                    func=func.__name__
                ))

        return wrapper

    return check


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission("user_1")
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

# Принято
