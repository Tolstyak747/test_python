text = input("Введите текст: ")
print("Оригинальный словарь частот: ")
d = [x for x in text]
d = set(d)

list = {}
for elem in d:
    list[elem] = text.count(elem)
for x in list:
    print(x, ":", list[x])


a = set(list.values())
print("Инвертированный словарь частот: ")
invert_list = {}

for x in a:
    invert_list[x] = [k for k in list if list[k] == x]

for x in invert_list:
    print(x,":", invert_list[x])

#нужно давать более осмысленные именна переменным
