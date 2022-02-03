amount = int(input("Количество цифр:"))
num_list = []
for _ in range(amount):
    num = int(input("Введите число: "))
    num_list.append(num)

print(num_list)

new_ls = [elem for elem in num_list if elem > 0]
num_list = [elem for elem in num_list if elem == 0]
new_ls.extend(num_list)
print(new_ls)
new_ls = [elem for elem in new_ls if elem > 0]
print(new_ls)
#зачет
