n = int(input("Введите число: "))


def least_divisor(n):
    for divider in range(2, n + 1):
        num = n % divider
        if num == 0:
            print("Наименьший делитель, отличный от единицы: ", divider)
            break



least_divisor(n)