message = input("Сообщение: ")
signs = ".,?!-:;()"
signs_index = []

for symb in signs:
    if symb in message:
        signs_index.append(symb)
        signs_index.append(message.index(symb))

print(signs_index)

message = message.split(" ")

new_ls = ""
for elem in message:
        for symb in elem[::-1]:
            if not symb in signs:
                new_ls += symb
        new_ls += " "

# new_ls = new_ls.split()
print(new_ls)

#зачет
