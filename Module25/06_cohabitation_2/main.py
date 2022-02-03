import random


class Human:
    satiety = 30
    hapiness = 100
    __eaten = 0

    def __init__(self, name):
        self.name = name

    def eat(self, house):
        rr = random.randint(1, 31)
        self.satiety += rr
        self.set_eaten(rr)
        house.eat -= rr
        print(f"{self.name} кушает")

    def set_eaten(self, rr):
        self.__eaten += rr

    def get_eaten(self):
        return self.__eaten

    def play_with_pet(self):
        self.hapiness += 5


class Husband(Human):
    __earned_money = 0

    def __str__(self):
        return (f"{self.name}\n"
                f"Сытость: {self.satiety}\n"
                f"Счастье: {self.hapiness}")

    def set_earn(self):
        self.__earned_money += 150

    def get_earn(self):
        return self.__earned_money

    def play(self):
        self.hapiness += 20
        self.satiety -= 10
        print(f"{self.name} решил поиграть")

    def work(self, house):
        house.money += 150
        self.satiety -= 10
        print(f"{self.name} пошел на работу")
        self.set_earn()


class Wife(Human):
    __bought_fur_coat = 0

    def __str__(self):
        return (f"{self.name}\n"
                f"Сытость: {self.satiety}\n"
                f"Счастье: {self.hapiness}")

    def products(self, house):
        house.money -= 80
        house.eat += 60
        house.eat_for_cat += 10
        self.satiety -= 10
        print(f"{self.name} купила продукты")

    def fur_coat(self, house):
        house.money -= 350
        self.hapiness += 60
        self.satiety -= 10
        self.set_bought()
        print(f"{self.name} купила шубу")

    def set_bought(self):
        self.__bought_fur_coat += 1

    def get_bought(self):
        return self.__bought_fur_coat

    def cleaning(self, house):
        house.dirt -= random.randint(1, 101)
        self.satiety -= 10
        print(f"{self.name} убралась")


class Pet:
    satiety = 30

    def __init__(self, name):
        self.name = name

    def eat(self, house):
        rr = random.randint(1, 11)
        self.satiety += rr * 2
        house.eat_for_cat -= rr
        print(f"{self.name} кушает")

    def sleep(self):
        print(f"{self.name} уснул")
        self.satiety -= 10

    def hooligan(self, house):
        house.dirt += 5
        self.satiety -= 10
        print(f"{self.name} дерет обои")


class House:
    money = 100
    eat = 50
    eat_for_cat = 30
    dirt = 0

    def __str__(self):
        return (f"Количество денег: {self.money}\n"
                f"Количество еды: {self.eat}\n"
                f"Количество корма: {self.eat_for_cat}\n"
                f"Количество грязи в доме: {self.dirt}")


def one_day(husband, wife, pet, house):
    for i in range(1, 366):
        print(f"Шёл {i} день: ")
        house.dirt += 5
        if wife.satiety <= 10:
            wife.eat(house)
        elif wife.hapiness <= 15:
            if house.money > 450:
                wife.fur_coat(house)
            else:
                wife.play_with_pet()
        elif house.eat <= 60 or house.eat_for_cat <= 10:
            wife.products(house)
        elif house.dirt >= 89:
            wife.cleaning(house)
        else:
            wife.products(house)

        if husband.satiety <= 10:
            husband.eat(house)
        elif husband.hapiness <= 15:
            husband.play()
        else:
            husband.work(house)

        if pet.satiety <= 15:
            pet.eat(house)
        else:
            rr = random.randint(1, 3)
            if rr == 1:
                pet.sleep()
            else:
                pet.hooligan(house)

        if wife.satiety < 0 or husband.satiety < 0 or pet.satiety < 0:
            print("Похороны")
            break
        elif wife.hapiness < 10 or husband.hapiness < 10:
            print("Депрессия, она такая...")
            break

        print()
    print(f"За этот год муж заработал: {husband.get_earn()}\n"
          f"Еды было съедено: {husband.get_eaten() + wife.get_eaten()}\n"
          f"Шуб было куплено: {wife.get_bought()}")


a = Husband("Игорь")
b = Wife("Лена")
h = House()
c = Pet("Барсик")

one_day(a, b, c, h)
# я чуть изменил условие, если один поход в магазин этого всего 10 еды, а за один день они могут съесть 60, то еда остается в минусе.
# сделал что один поход за продуктами равен 60, или могу рандомно поставить
