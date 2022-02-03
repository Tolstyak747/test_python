import itertools

adress = {}
adress['Ул. Грибоедова'] = (2, 5)
adress['Бейкер стрит'] = (5, 2)
adress['Большая Садовая'] = (6, 6)
adress['Вечнозелёная Аллея'] = (8, 3)


ls = []
ls2 = []
val = itertools.permutations(adress.values(), 4)


for i in val:
    ls.append((0, 2))
    for elem in i:
        ls.append(elem)
    ls.append((0, 2))
    ls2.append(ls)
    ls = []


ls_sum = []
for elem in ls2:
    summ = 0
    for i in range(len(elem)):
        if i < 5:
            distance = ((elem[i + 1][0] - elem[i][0]) ** 2 + (elem[i + 1][1] - elem[i][1]) ** 2) ** 0.5
            summ += distance
    ls_sum.append(summ)


minimum = min(ls_sum)
min_i = ls_sum.index(minimum)
answer = ls2[min_i]


path = []
for i in range(len(answer)):
    if i < 5:
        distance = ((answer[i + 1][0] - answer[i][0]) ** 2 + (answer[i + 1][1] - answer[i][1]) ** 2) ** 0.5
        path.append(distance)


print(f'{answer[0]} -> {answer[1]}[{path[0]}] -> {answer[2]}[{path[1]}] -> {answer[3]}[{path[2]}] -> {answer[4]}[{path[3]}] -> {answer[5]}[{path[4]}] = {minimum}')
