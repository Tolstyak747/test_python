n = int(input("Введите количество человек: "))

pair_dic = {}
for nums in range(1, n):
    print(nums, "пара: ", end="")
    pair = input().split()
    pair_dic[pair[0]] = pair[1]
    print(pair_dic)

new_dic = {}
new_dic[pair[1]] = 0
print(new_dic)


for x in pair_dic:
    for y in new_dic:
        if pair_dic[x] == y:
            new_dic[x] = new_dic.get(x, 0)
print(new_dic)

# думал сделать два списка, но когда добавляю во второй список значения типа Алекс:0, то выскакивает ошибка
# dictionary changed size during iteration, я понимаю, что это связано с тем, что я меняю список во время итерации, но не могу по-другому найти решение этой задачи

#конечно. вы пытаетесь изменить словарь во время итерации. Так не делается.

num = int(input('Введите количество человек: '))

tree = dict()
family = dict()

for i_index in range(num - 1):
    couple = input(f'{i_index + 1} пара: ').split()
    tree[couple[0]] = couple[1]

for child, parent in tree.items():
    if parent in tree:
        family[child] = family[parent] + 1
    else:
        family[parent] = 0
        family[child] = 1

for i_key in sorted(family):
    print(i_key, family[i_key])
