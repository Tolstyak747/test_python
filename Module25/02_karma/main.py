import random


def one_day():
    karma = 0
    while karma < 500:
        karma += random.randint(1, 8)
        print(karma)
        if random.randint(1, 11) == 7:
            raise Exception(random.choice(ls))


ls = ["KillError", "DrunkError", "CarCrashError", "GluttonyError", "DepressionError"]
with open("karma.log", "w") as error:
    for i in ls:
        error.write("{}\n".format(i))

one_day()
