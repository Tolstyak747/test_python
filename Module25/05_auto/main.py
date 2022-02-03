class Auto:
    def __init__(self, x, y, injection):
        self.x = x
        self.y = y
        self.injection = injection

    def move(self, reversal, distance):
        if self.injection == reversal:
            print(f"Автомобиль продолжает движение в том же направлении еще {distance} км")
        else:
            print(f"Автомобиль повернул на {reversal} градусов и продолжил своё движение еще {distance} км")


class Bus(Auto):
    dif = 0

    def __init__(self, x, y, injection, passengers=0, money=0):
        super().__init__(x, y, injection)
        self.passengers = passengers
        self.money = money

    def to_come_in(self, amount, ):
        self.passengers += amount
        self.dif = amount

    def to_come_out(self, amount):
        self.passengers -= amount
        self.dif = 0
        if self.passengers < 0:
            raise Exception("Недопустимое значение")

    def move(self, reversal, distance):

        if self.injection == reversal:
            print(f"Автобус продолжает движение c {self.passengers} пассажирами в том же направлении еще {distance} км")
        else:
            print(
                f"Автобус повернул на {reversal} градусов и продолжил своё движение с {self.passengers} пассажирами еще {distance} км")
            self.injection = reversal
        self.money += self.dif * distance
        print(f"Денег в кассе: {self.money}")


a = Auto(1, 2, 45)
a.move(30, 10)

b = Bus(10, 2, 45)
b.to_come_in(10)
b.move(10, 2)
b.to_come_in(1)
b.move(10, 1)
b.to_come_out(3)
b.move(10, 1)
b.to_come_in(1)
b.move(10, 3)

# 1км = 1 рубль
