def all_numbers(num):
    if num >= 1:
        print(num)
        all_numbers(num - 1)

num = int(input("Введите число: "))
all_numbers(num)

# зачет
