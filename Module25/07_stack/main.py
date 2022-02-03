class Stack:
    def __init__(self):
        self.stack = []

    def append(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)


class TaskManager:
    def __init__(self):
        self.tm = {}

    def new_task(self, k, v):
        if v not in self.tm:
            self.tm[v] = Stack()
        self.tm[v].append(k)

    def __str__(self):
        ls = []
        if self.tm:
            for i in sorted(self.tm.keys()):
                ls.append(f"{str(i)} {self.tm[i]}\n")

        return "".join(ls)


m = Stack()
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
