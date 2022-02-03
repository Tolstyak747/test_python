# def shortest(str, n):
#     return min(len(str), len(n))
#
# string = input("Введите строку: ")
# nums = input("Введите числа: ").split()
# nums = [int(x) for x in nums]
# nums = tuple(nums)
#
# # print(list(zip(string, nums)))
#
#
# dic = ((string[i_symb], nums[i_symb])
#     for i_symb in range(shortest(string, nums)))
#
# print(dic)
#
# print("Результат: ")
# for i_elem in dic:
#     print(i_elem)


def generation(string,nums):
generation("привет",[1, 2, 3, 4])

# Не понимаю, как это делать без условного оператора

# вы же уже написали в закомментированных строках верную программу. Вот что ожидали от вас:
def shortest_sequence_range(*args):
    return range(len(sorted(args, key=len)[0]))


def my_zip(first, second):
    ans = ((first[i], second[i]) for i in shortest_sequence_range(first, second))
    return ans
