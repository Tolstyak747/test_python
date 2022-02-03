word = input("Введите слово: ")
word_lis = []
count = 0
unique = 0
for sym in word:
    word_lis.append(sym)

for symbol in word_lis:
    for elem in word_lis:
        if symbol == elem:
            count += 1
    if count == 1:
        unique += 1
        count -= count
    else:
        count -= count


print("Кол-во уникальных букв: ", unique)


