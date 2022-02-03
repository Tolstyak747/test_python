import random

ls = []

n = int(input("Кол-во палок: "))
k = int(input("Кол-во бросков: "))

for i in range(k):
    R_i = random.randint(1, n)
    ls.append(R_i)
    L_i = random.randint(1, R_i)
    ls.append(L_i)
    print("Бросок", i + 1, ". Сбиты палки с номера", L_i, "по номер", R_i)

a = max(ls)
b = min(ls)

result = [x for x in range(b, a + 1)]
print()
print("Результат: ", end="")
for num in range(1, n + 1):
    if num in result:
        print(".", end="")
    else:
        print("I", end="")
#зачет