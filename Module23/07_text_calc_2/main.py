def solve(spisok):
    try:
        if spisok[1] == "+":
            res.append(int(ls[0]) + int(ls[2]))
        elif spisok[1] == "x":
            res.append(int(ls[0]) * int(ls[2]))
        elif spisok[1] == "-":
            res.append(int(ls[0]) - int(ls[2]))
        elif spisok[1] == "/":
            res.append(int(ls[0]) / int(ls[2]))
        else:
            print("Обнаружена ошибка в строке: {}".format(i_line), end="")
            answer = input("Хотите исправить? ")
            if answer.lower() == "да":
                corrected = input("Введите исправленную строку: ").split()
                solve(corrected)
            elif answer.lower() == "нет":
                res.append(0)
    except ValueError:
        print("Передано неправльное значение")
    return res


with open("calc.txt", "w") as calc:
    calc.write("10 *- 34\n"
               "10 x 4\n")

with open("calc.txt", "r") as calc:
    res = []
    for i_line in calc:
        ls = i_line.split()
        solve(ls)
print("Результат: ", sum(res))

# зачет
