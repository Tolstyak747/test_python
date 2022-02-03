n = int(input("Введите количество пар слов: "))
dictt = {}
for l in range(1, n + 1):
    print(l, 'пара: ', end ="")
    para = input().lower().split(' - ')
    dictt[para[0]] = para[1]

word = input("Введите слово: ").lower()
for x in dictt:
    if x == word:
        print("Cиноним: ", dictt[x])
        break
    elif dictt[x] == word:
        print("Cиноним: ", x)
        break
    else:
        print("Такого слова в словаре нет.")
        break

#зачет
