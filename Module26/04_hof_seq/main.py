class HofstadterIter:
    count = 0

    def change_ls(self) -> list:
        self.ls.append(self.ls[1])
        self.ls[1] = self.ls[0]
        self.ls[0] = 0
        return self.ls

    def __init__(self, num: int, ls: list) -> None:
        self.num = num
        if ls[0] == 1 and ls[1] == 1:
            self.ls = ls
            self.change_ls()
        else:
            raise Exception("Недопустимое значение!")

    def __iter__(self):
        self.hofstader()
        return self

    def hofstader(self):
        for i in range(3, self.num + 1):
            a = self.ls[(i - self.ls[(i - 1)])] + self.ls[(i - self.ls[(i - 2)])]
            self.ls.append(a)

    def __next__(self) -> int:
        if self.count < self.num:
            self.count += 1
            return self.ls[self.count]
        else:
            raise StopIteration("")


a = HofstadterIter(10, [1, 1])
for i in a:
    print(i)
