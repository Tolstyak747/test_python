line = input("Введите строку: ").split()
result = ""

for word in line:
    for i in range(len(word)):
        if i == 0:
            result += word[i].upper()
        else:
            result += word[i].lower()
    result += " "



print("Результат: ", result)

#зачет
