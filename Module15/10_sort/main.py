amount = int(input("Введите кол-во элементов:"))
n_ls = []
count = 0
for _ in range(amount):
    num = int(input("Введите число: "))
    n_ls.append(num)
    count += 1

for i in range(count):
    for n in range(i, count):
        if n_ls[i] > n_ls[n]:
            n_ls[i], n_ls[n] = n_ls[n], n_ls[i]

print(n_ls)