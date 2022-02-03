class Students:
    def __init__(self, name, num_group, grade):
        self.name = name
        self.num_group = num_group
        self.grade = grade

    def average_score(self):
        return round(sum(self.grade) / len(self.grade), 2)

    def __lt__(self, other):
        return self.average_score() < other.average_score()

    def info(self):
        print("Студент {} из группы №{} со средним баллом {}".format(self.name, self.num_group, self.average_score()))


def st_ls(*studens):
    ls = []
    for i in studens:
        ls.append(i)
    return ls


st_1 = Students("Иванов", 1, [5, 5])
st_2 = Students("Петров", 1, [1, 5, 3])
st_3 = Students("Соболев", 2, [5, 3, 5, 3])
st_4 = Students("Квасин", 2, [2, 3, 4])
st_5 = Students("Анюков", 3, [5, 3, 3, 3, 3])
st_6 = Students("Жирков", 3, [1, 1, 2, 5])
st_7 = Students("Павлюченко", 3, [4])
st_8 = Students("Зырянов", 1, [3])
st_9 = Students("Погребняк", 2, [5, 4, 5])
st_10 = Students("Заболотный", 1, [3, 3, 3])

lis = st_ls(st_1, st_2, st_3, st_4, st_5, st_6, st_7, st_8, st_9, st_10)
lis.sort()


for i in lis:
    i.info()
