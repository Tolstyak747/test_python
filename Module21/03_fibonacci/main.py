# def num_val(numerial):
#     ls_fb = [1, 1]
#     while len(ls_fb) != numerial:
#         next = []
#         for i, v in enumerate(ls_fb[::-1]):
#             if i == 2:
#                 break
#             else:
#                 next.append(v)
#         next = sum(next)
#         ls_fb.append(next)
#     return ls_fb[-1::]


def num_val(numerial, ls=[1, 1]):
    while numerial == len(ls):
        break
    else:
        ls.append(sum(ls[-2:]))
        num_val(numerial)
    return ls[-1:]

# классическая задача на рекурсию
def fibonacci(num):
    if num in (1, 2):
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)







num_pos = int(input("Введите позицию числа в ряде Фибоначчи: "))
value = num_val(num_pos)
print("Ответ: ", value)
