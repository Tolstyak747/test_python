amount = int(input("Кол-во контейнеров: "))
n_ls = []

for i in range(amount):
    weight = float(input("Введите вес контейнера: "))
    a = weight - int(weight)
    if weight > 200 or a > 0:
        print("Ошибка ввода")
    n_ls.append(weight)

new_weight = int(input("Введите вес нового контейнера: "))

for i in range(amount):
    if new_weight > n_ls[i]:
        print("Номер, куда встанет новый контейнер: ", i + 1)
        break