class Circle:
    def __init__(self, x = 0, y = 0, radius = 1):
        self.x = x
        self.y = y
        self.radius = radius

    def square(self):
        sq = 3.14 * self.radius ** 2
        return sq

    def perimetr(self):
        pr = 2 * 3.14 * self.radius
        return pr

    def increase(self, k):
        return self.perimetr() * k

    def persechenie(self, cir):
        if self.x == cir.x:
            if self.radius + cir.radius > abs(self.y - cir.y):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        elif self.y == cir.y:
            if self.radius + cir.radius > abs(self.x - cir.x):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        else:
            if (self.radius + cir.radius) ** 2 > abs((self.x - cir.x) ** 2 - (self.y - cir.y) ** 2):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')


krug = Circle()
krug_2 = Circle(7, 8, 2)


