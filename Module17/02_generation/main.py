import  random

n = int(input("Введите длину списка: "))
n_ls = [random.randint(1, 10) for _ in range(n)]
new_ls = [int(n_ls[i]/ n_ls[i]) if i % 2 == 0 else int(n_ls[i] % 5) for i in range(n)]

print("Генерируемый список: ", n_ls)
print("Результат: ", new_ls)


# вы слегка усложнили, можно проще
length = int(input('Введите длину списка: '))
my_list = [1 if i_num % 2 == 0 else i_num % 5 for i_num in range(length)]
print('Результат:', my_list)
