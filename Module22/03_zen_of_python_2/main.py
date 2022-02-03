import os


def list_file(file):
    with open(file, "r") as f:
        ls_file = f.readlines()
    return ls_file


def sum_line(file):
    return len(list_file(path_to_file))


def sum_letter(file):
    summ = 0
    file = list_file(path_to_file)
    for line in file:
        for letter in line:
            if letter.isalpha():
                summ += 1

    return summ


def sum_word(file):
    summ = 0
    file = list_file(path_to_file)
    for line in file:
        for symb in line:
            if symb == " ":
                summ += 1
    return summ


def stats(file):
    file = list_file(path_to_file)
    dic = {}
    for line in file:
        line = line.lower()
        for letter in line:
            if letter.isalpha():
                if letter in dic:
                    dic[letter] += 1
                else:
                    dic[letter] = 1
    return dic


def rare_letter(dic):
    dic = stats(path_to_file)
    sorted_val = sorted(dic.values())
    rare_l = {}
    for num in sorted_val:
        for k in dic:
            if dic[k] == num:
                rare_l[k] = num
        break
    return rare_l


path_to_file = os.path.abspath(os.path.join("..", "02_zen_of_python", "zen.txt"))

print("Кол-во строк: ", sum_line(path_to_file))
print("Кол-во букв: ", sum_letter(path_to_file))
print("Кол-во слов: ", sum_word(path_to_file))

stats(path_to_file)
rare_letter(stats)

for k, v in rare_letter(stats(path_to_file)).items():
    print("Буква {} встречается всего {} раза.".format(k, v))

# зачет
