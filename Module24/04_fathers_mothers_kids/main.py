class Parent:
    age = 30
    name = "Антон"
    children = []

    def deti(self, child):
        self.children.append(child)

    def info(self):
        print("Меня зовут {}, мне {} лет".format(self.name, self.age))

    def feed(self):
        for child in self.children:
            Child.eat(child)

    def calmed_dowm(self):
        for child in self.children:
            Child.calmn_down(child)


class Child:
    calmness = {0: "спокойствия", 1: "возбуждения"}
    hunger = {0: "голода", 1: "сытости"}
    name = "Денис"
    age = 18

    def __init__(self, calmness=0, hunger=0):
        self.calmness = calmness
        self.hunger = hunger

    def proverka_vozrasta(self):
        if Parent.age - self.age < 16:
            print("Вряд ли {} ваш родитель!".format(Parent.name))

    def calmn_down(self):
        if self.calmness > 0:
            self.calmness -= 1
        self.print_calmness()

    def print_calmness(self):
        print("{} в состоянии {}".format(self.name, Child.calmness[self.calmness]))

    def eat(self):
        if self.hunger < 1:
            self.hunger += 1
        self.print_hungred()

    def print_hungred(self):
        print("{} в состоянии {}".format(self.name, Child.hunger[self.hunger]))


i = Parent()
kinder = Child()
i.deti(kinder)
i.info()
print(kinder.name)
kinder.print_calmness()
kinder.print_hungred()
i.feed()
i.calmed_dowm()