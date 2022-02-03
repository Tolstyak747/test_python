class MyDict(dict):
    def __init__(self):
        super().__init__()

    def get(self, sought):
        if sought in self.keys():
            return self.values()
        else:
            return 0


d = MyDict()
d["Gta"] = 5
print(d)
print(d.get("Ga"))


a = MyDict()
a["Lh"] = 111
print(a.keys())
