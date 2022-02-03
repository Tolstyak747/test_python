def sum(*numerials, all=0):
        for elem in numerials:
            if isinstance(elem, int):
                all += elem
            else:
                for i in elem:
                    if isinstance(i,int):
                        all += i
                    elif isinstance(i, list):
                        for sub_i in i:
                            all += sub_i
        return all

print("Ответ: ", sum([1, 2, [3]], [1], [3],[[1]]))
print("Ответ: ", sum(1, 2, 3, 4, 5))
