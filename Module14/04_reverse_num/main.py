def func(n):
    a = int(n) % 10
    b = int(n) // 10 % 10
    c = int(n) // 100
    d = round(n - int(n), 2) * 100
    e = d % 10
    f = d // 10
    g = (10 * e + f) / 100
    num = a * 100 + b * 10 + c + g
    return num


n = float(input("Введите первое число: "))
k = float(input("Введите второе число: "))

print("Первое число наоборот: ", func(n))
print("Второе число наоборот: ", func(k))
summ = func(n) + func(k)
print("Сумма: ", summ)
