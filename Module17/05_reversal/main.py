
line = input("Введите строку: ")
print(line)

start = int(line.index("h"))
stop = int(len(line) - line[::-1].index("h"))
line = line[stop - 2:start:-1]
print("Разворот: ", line)
#зачет