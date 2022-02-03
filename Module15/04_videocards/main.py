amount = int(input("Кол-во видеокарт: "))
first_amount_lis = []
for i in range(1, amount +1):
    print(i, "Видеокарта: ", end = "")
    num = input()
    first_amount_lis.append(num)

first_amount_lis = list(first_amount_lis)
second_amount_lis = []

maxim = first_amount_lis[0]
for i in first_amount_lis:
    if i > maxim:
        maxim = i

for i in first_amount_lis:
    if i != maxim:
        second_amount_lis.append(i)




print("Старый список видеокарт: ", first_amount_lis)
print("Новый список видеокарт: ", second_amount_lis)

