def reverse_file(file):
    with open(file, "r") as f:
        data = f.readlines()
        for i_line in data[::-1]:
            print(i_line)


reverse_file("zen.txt")


# зачет
