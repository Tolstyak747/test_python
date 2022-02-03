import random


class Human:
    satiety = 50

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.satiety += 1
        House.decrease_food(food)

    def work(self, money):
        self.satiety -= 1
        House.increase_money(money)

    def play(self):
        self.satiety -= 1

    def death(self):
        print(f"{self.name} умер!")


class House:
    def __init__(self, food=50, money=50):
        self.food = food
        self.money = money

    def decrease_food(self):
        self.food -= 1

    def increase_food(self):
        self.food += 1

    def decrease_money(self):
        self.money -= 1

    def increase_money(self):
        self.money += 1


def one_day(human, house):
    cube = random.randint(1, 7)
    if human.satiety < 0:
        human.death()
        return 0
    elif human.satiety < 20:
        human.eat(house)
    elif house.food < 10:
        house.increase_food()
        house.decrease_money()
    elif house.money < 50:
        human.work(house)
    elif cube == 1:
        human.work(house)
    elif cube == 2:
        human.eat(house)
    else:
        human.play()


p1 = Human("Maks")
p2 = Human("Anya")
h = House()

for i in range(1, 366):
    print(f"Шёл {i} день:")
    if (one_day(p1, h) == 0) or (one_day(p2, h) == 0):
        break
    print(f"Сытость {p1.name}:{p1.satiety}\nСытость {p2.name}:{p2.satiety}\nЕда:{h.food}\nДеньги:{h.money}")
    print()
# # Ни разу не смог похоронить никого из них при таком алгоритме действий
