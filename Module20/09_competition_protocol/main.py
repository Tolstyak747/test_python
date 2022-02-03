n = int(input("Сколько записей вносится в протокол? "))
if n < 3:
    print("Не хватает игроков!")
else:
    dic = []
    print("Записи (результат и имя): ")
    for cnt in range(1, n + 1):
        player_scores = input("{} запись: ".format(cnt)).split()

        for x in range(len(player_scores)):
            if x == 0:
                player_scores[x] = int(player_scores[x])

        dic.append(player_scores)


    # new_dic = []
    # cnt = len(dic)
    # print(len(dic))
    # while cnt != 0:
    #     a = max(dic)
    #     new_dic.append(a)
    #     dic.pop(dic.index(max(dic)))
    #     a = 0
    #     cnt -= 1

    dic = sorted(dic, reverse = True)



    po_kazhdomy = {}
    for x in dic:
        if x[1] not in po_kazhdomy:
            po_kazhdomy[x[1]] = x[0]
        else:
            for k, v in po_kazhdomy.items():
                if x[1] == k:
                    if x[0] >= v:
                        po_kazhdomy[k] = x[0]
                    else:
                        po_kazhdomy[k] = v


    if len(po_kazhdomy) < 3:
        print("Не хватает игроков!")
    else:
        print("Итоги соревнований:")
        for i, v in enumerate(po_kazhdomy):
            if i < 3:
                print("{}. место: ".format(i + 1), v, po_kazhdomy[v])

# не понимаю как сделать, чтобы при равных значениях выше был тот, кто раньше был в списке
