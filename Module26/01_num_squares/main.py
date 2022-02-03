class Iter:
    def __init__(self, num: int) -> None:
        self.num = num

    def __iter__(self):  # что написать здесь? Что возвращает итератор?
        return self

    def __next__(self) -> None:
        for i in range(1, self.num + 1):
            print(i ** 2)
        raise StopIteration


def gen(nums: int) -> str:#Когда указываю int, то указывает на ошибку
    for i in range(1, nums + 1):
        yield i ** 2


n = int(input("Введите число: "))

first = Iter(n)
for i in first:
    print(i)
print()

for i in gen(n):
    print(i)
print()

expression = (x ** 2 for x in range(1, n + 1))
for i in expression:
    print(i)


# TODO от так должно быть
from typing import Optional, NoReturn, Union, Iterator


class Cubes:
    """

    """
    def __init__(self, n: Optional[int] = 0) -> None:
        """

        :param n:
        """
        self.last = n
        self.first = 1

    def __iter__(self) -> 'Cubes':
        """

        :return:
        """
        self.n = self.first
        return self

    def __next__(self) -> Union[int, NoReturn]:
        """

        :return:
        """
        if self.n <= self.last:
            result = self.n ** 3
            self.n += 1
            return result
        else:
            raise StopIteration


def generator_function(n: int) -> Iterator[int]:
    """
    Генератор для вывода кубов чисел от 1 до n
    :param n:
    :return:
    """
    for number in range(1, n + 1):
        yield number**3
