class MyMath:
    @classmethod
    def circle_len(cls, radius):
        return round(2 * 3.14 * radius, 3)

    @classmethod
    def circle_sq(cls, radius):
        return round(3.14 * (radius ** 2), 3)

    @classmethod
    def cube_volume(cls, length):
        return length ** 3

    @classmethod
    def sfura_sq(cls, radius):
        return 3.14 * 4 * (radius ** 2)


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(length=3)
res_4 = MyMath.sfura_sq(radius=4)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
