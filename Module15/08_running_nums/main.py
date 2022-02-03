amount = int(input("Кол-во элементов: "))
start_n_ls = []
for _ in range(amount):
    num = int(input("Введите символ: "))
    start_n_ls.append(num)

shift = int(input("Введите сдвиг: "))
finish_n_ls = []

for i in range(amount):
    finish_n_ls.append(start_n_ls[i - shift])

print(finish_n_ls)