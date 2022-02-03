amount = int(input("Введите кол-во клеток: "))
n_lis = []
for i in range(1, amount + 1):
    print("Эффективность ", i, "клетки: ", end = "")
    effiency = int(input())
    n_lis.append(effiency)

n_lis = list(n_lis)
sum = []
for i in range(1, amount):
    if i > n_lis[i]:
        sum.append(n_lis[i])
print("Неподходящие значения: ", sum)