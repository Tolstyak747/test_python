def shortest(str, n):
    return min(len(str), len(n))

string = input("Введите строку: ")
nums = input("Введите числа: ").split()
nums = [int(x) for x in nums]
nums = tuple(nums)

# print(list(zip(string, nums)))


dic = ((string[i_symb], nums[i_symb])
    for i_symb in range(shortest(string, nums)))

print(dic)

print("Результат: ")
for i_elem in dic:
    print(i_elem)


