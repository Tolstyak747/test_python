students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

#плохо называть так функцию - очень неинформтаивно. А также dict - это тип данных и ключевое слово в Python. Потому аргумент тоже не надо так называть.
def f(dict):
    lst = []
    string = ""
    for k, v in students.items():
        lst += v["interests"]
        string += v["surname"]
    cnt = len(string)
    return lst, cnt


for k, v in students.items():
    if "age" in v:
        print(k, '-', v["age"])

my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)

#зачет
