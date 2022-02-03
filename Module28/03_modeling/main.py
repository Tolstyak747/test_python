import math


class Triangle:
    """Базовый класс - треугольник."""

    def __init__(self, h: float, base: float) -> None:
        self.__h = h
        self.__base = base
        self.__side = math.sqrt(((self.h / 2) ** 2) + (self.h ** 2))

    @property
    def h(self) -> float:
        return self.__h

    @h.setter
    def h(self, value) -> None:
        self.__h = value

    @property
    def base(self) -> float:
        return self.__base

    @base.setter
    def base(self, value) -> None:
        self.__base = value

    @property
    def side(self) -> float:
        return self.__side

    def perimetr(self) -> float:
        return self.__side * 2 + self.__base

    def square_tr(self) -> float:
        return 0.5 * self.__base * self.h


class Square:
    """Базовый класс - квадрат."""

    def __init__(self, length):
        self._length = length

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value) -> None:
        self._length = value

    def perimetr(self) -> float:
        return self._length * 4

    def square_sq(self) -> float:
        return self._length ** 2


class Cube(Square):
    """3D модель - куб."""

    def __init__(self, length) -> None:
        super().__init__(length)

    def square(self) -> float:
        return 6 * (self.square_sq())


class Pyramid(Triangle):
    """3D модель - пирамида."""
    def __init__(self, h: float, base: float) -> None:
        super().__init__(h, base)

    def square(self) -> float:
        return (4 * self.square_tr()) + (self.base ** 2)

