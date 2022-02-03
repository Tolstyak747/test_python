n = (1, 10, 3) #сюда вводим любые элементы


cnt = 0
for x in n:
    if type(x) is not int:
        cnt += 1
if cnt > 0:
    print(n)
else:
    n = sorted(n)
    print(tuple(n))

#зачет
