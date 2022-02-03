class Gardener:
    def __init__(self, name):
        self.name = name
        self.garden = []

    def append(self, gryadka):
        self.garden.append(gryadka)

    def care(self):
        for gryadka in self.garden:
            PotatoGarden.grow_all(gryadka)
            PotatoGarden.are_all_ripe(gryadka)

    def collect(self):
        print("Время собирать урожай!")
        print(Potato.zrelaya)


class Potato:
    states = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}
    zrelaya = []

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            self.zrelaya.append(self.index)
            return True
        return False

    def print_state(self):
        print("Картошка № {} имеет степень зрелости: {}".format(self.index, self.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatos = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        for i_potato in self.potatos:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatos:
            if not i_potato.is_ripe():
                print("Картошка еще не созрела!")
            else:
                print("Вся картошка готова!")


i = Gardener("Константин")
my_garden = PotatoGarden(5)
i.append(my_garden)

for _ in range(3):
    i.care()
    print()
i.collect()
