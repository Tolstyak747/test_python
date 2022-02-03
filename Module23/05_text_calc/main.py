with open("calc.txt", "w") as calc:
    calc.write("10 - 34\n"
               "10 x 4\n")

with open("calc.txt", "r") as calc:
    res = []
    for i_line in calc:
        ls = i_line.split()
        try:
            if ls[1] == "+":
                res.append(int(ls[0]) + int(ls[2]))
            elif ls[1] == "x":
                res.append(int(ls[0]) * int(ls[2]))
            elif ls[1] == "-":
                res.append(int(ls[0]) - int(ls[2]))
            elif ls[1] == "/":
                res.append(int(ls[0]) / int(ls[2]))

        except ValueError:
            print("Передано неправльное значение")

print("Результат: ", sum(res))

# зачет
