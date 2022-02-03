class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Appartament(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


money = int(input("Введите количество денег: "))
appart = int(input("Введите стоимость квартиры: "))
car = int(input("Введите стоимость машины: "))
house = int(input("Введите стоимость дачи: "))

a = Appartament(appart)
c = Car(car)
h = CountryHouse(house)

all_tax = a.tax() + c.tax() + h.tax()

if money >= all_tax:
    print("Cумма налогов на Ваше имущество составляет: {}".format(all_tax))
else:
    print("Cумма налогов на Ваше имущество составляет: {}\n"
          "Вам не хватает {} рублей".format(all_tax, round(all_tax - money, 2)))




