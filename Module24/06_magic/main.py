class Water:
    name = "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Air:
    name = "Воздух"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Fire):
            return Dust()


class Fire:
    name = "Огонь"

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()


class Earth:
    name = "Земля"


class Storm:
    def __init__(self):
        print(f"{Water.name} + {Air.name} = Шторм")


class Steam:
    def __init__(self):
        print(f"{Water.name} + {Fire.name} = Пар")


class Dirt:
    def __init__(self):
        print(f"{Water.name} + {Earth.name} = Грязь")


class Lightning:
    def __init__(self):
        print(f"{Air.name} + {Fire.name} = Молния")


class Dust:
    def __init__(self):
        print(f"{Air.name} + {Earth.name} = Пыль")


class Lava:
    def __init__(self):
        print(f"{Fire.name} + {Earth.name} = Молния")


Water() + Air()
Water() + Fire()
Water() + Earth()
Air() + Fire()
Air() + Earth()
Fire() + Earth()