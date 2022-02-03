def summ(n):
    summa = 0
    while n != 0:
        num = n % 10
        summa += num
        n //= 10
    return summa

def count(n):
    count_n = 0
    while n != 0:
        n //= 10
        count_n += 1
    return count_n


n = int(input("Введите число: "))

print("Сумма цифр: ", summ(n))
print("Кол-во цифр в числе: ", count(n))
difference = abs(summ(n) - count(n))
print("Разность суммы и кол-ва цифр: ", difference)

