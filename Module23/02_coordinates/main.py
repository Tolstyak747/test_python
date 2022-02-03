import random

with open("coordinates.txt", "w") as f:
    f.write("2 2\n"
            "5 10\n")



def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            try:
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                try:
                    number = random.randint(0, 100)
                    with open('result.txt', 'w') as file_2:
                        my_list = sorted([res1, res2, number])
                        file_2.write(str(my_list) + "\n")
                except Exception:
                    print("Что-то пошло не так")
            except Exception:
                print("Что-то пошло не так со второй функцией")
except Exception:
    print("Что-то пошло не так с первой функцией")


#Не догоняю как сделать, чтобы файл не перезаписывал, а дополнял, если файл уже создан(про "a" вместо "w" я знаю)

# именно применить аргумент "а"
with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print('Деление на 0 в первой функции')
        else:
            try:
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError:
                print('Деление на 0 во второй функции')
            else:
                number = random.randint(0, 100)
                with open('result.txt', 'a') as file_2:
                    my_list = sorted([res1, res2, number])
                    file_2.write(' '.join(str(x) for x in my_list) + '\n')