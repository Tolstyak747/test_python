import random
n = int(input("Кол-во случайных чисел: "))

nums = [random.randint(0, 100) for x in range(n)]
print("Оргинальный список: ", nums)
ls_1 = [x for x in nums[::2]]
ls_2 = [x for x in nums[1::2]]

new_nums = list(zip(ls_1, ls_2))
print("Новый список: ", new_nums)

#зачет
