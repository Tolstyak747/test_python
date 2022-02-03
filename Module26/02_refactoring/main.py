list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def func(lis: list, lis_2: list, num: int) -> str:
    for x in lis:
        for y in lis_2:
            result = x * y
            yield x, y, result
            if result == num:
                # зачем писать return и print вместе? так делать не надо 
                print("Found!")


f = func(list_1, list_2, to_find)
print(f)
for i in f:
    print(i)
