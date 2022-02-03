import math

def calculating_math_func(data, cashe={}):
    while data in cashe:
        break
    else:
        cashe[data] = math.factorial(data)
        calculating_math_func(data)
    return (cashe.get(data) / (data ** 3)) ** 10

while True:
    data = int(input("Введите число: "))
    print(calculating_math_func(data))

# мой вариант. у вас рекурсия всегодня ан одних и тех же данных вызывается, что неверно

def calculating_math_func_2(data, cache={}):
    cache = cache if isinstance(cache, dict) else dict()
    if data in cache:
        return cache[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    cache[data] = result
    return cache[data]