nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def func(lis,new_ls =[]):
    for i in lis:
        if isinstance(i, int):
            new_ls.append(i)
        else:
            if isinstance(i, list):
                func(i)
    return new_ls




print("Ответ: ", func(nice_list))