def input_file(file):
    summ =[]
    with open(file, "r") as numbers:
        for i_line in numbers:
            for elem in i_line:
                if elem.isalnum():
                    summ.append(int(elem))
    return summ

def output_file(file):
    with open(file, "w") as answer:
        answer.write(str(sum(input_file("numbers.txt"))))


input_file("numbers.txt")
output_file("answer.txt")

# зачет
