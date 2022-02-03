string = input("Введите строку: ")

ls = []
count = 0
per = string[0]
ls.append(string[0])
for elem in string:
    if elem == per:
        count += 1
        # ls.append(elem)
        per = elem
    else:
        ls.append(count)
        count = 1
        ls.append(elem)
        per = elem
ls.append(count)

string = "".join(str(e) for e in ls)
print("Закодированная срока: ", string)


#зачет

