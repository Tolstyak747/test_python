import random


class War:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def info(self):
        print("Воин {}, у него {} здоровья".format(self.name, self.health))

    def punch(self, war):
        self.health -= 20
        if self.health == 0:
            print("{} прикончил {}".format(war.name, self.name))
        else:
            print("{} нанес удар, у {} осталось {} здоровья".format(war.name, self.name, self.health))
        return self.health


def duel(warrior_1, warrior_2):
    random_n = random.randint(1, 2)
    if random_n == 1:
        health = war_1.punch(warrior_2)
        return health
    elif random_n == 2:
        health = war_2.punch(warrior_1)
        return health


war_1 = War("Володя")
war_2 = War("Максим")

while True:
    if duel(war_1, war_2) > 0:
        continue
    else:
        break
