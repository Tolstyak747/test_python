n = int(input("Введите ко-во заказов: "))
order_ls = []

for i in range(1, n + 1):
    print(i, "заказ: ", end="")
    order = input().split()
    order_ls.append(order)

fam_ls = [x[0] for x in order_ls]
fam_ls = set(fam_ls)

new_ls = {}
for i in fam_ls:
    new_ls[i] = {}

# for x in order_ls:
#     x[2] = int(x[2])

for i in new_ls:
    for x in order_ls:
        if i == x[0]:
            if x[1] not in new_ls[i]:
                new_ls[i].update({x[1]: x[2]})
            # else:
            #     new_ls[i] = {x[1]: x[2]} Помогите, всю голову сломал, не понимаю как просуммировать значения!


for i in new_ls:
    print(i, ":", new_ls[i])
# как вывести словарь без скобок?

#все ответы на вопросы здесь - в правильном коде:
orders_count = int(input('Введите кол-во заказов: '))
database = dict()
for i_order in range(orders_count):
    customer, pizza_name, count = \
        input('{} заказ: '.format(i_order + 1)).split()

    if customer not in database:
        database[customer] = {pizza_name: int(count)}
    else:
        if pizza_name in database[customer]:
            database[customer][pizza_name] += int(count)
        else:
            database[customer].update({pizza_name: int(count)})

for i_customer in database.keys():
    print('{}:'.format(i_customer))
    for j_pizza in database[i_customer].keys():
        print('     {}: {}'.format(j_pizza, database[i_customer][j_pizza]))
