app = {}


def callback(route):
    def decorator(func):
        app[route] = func

        # TODO Обертка ничего не делает, потому можно было ее не создавать
        #   Т.е. можно было просто сделать return func
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res

        return wrapper

    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')

if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# Принято
