A = int(input("Введите первый год: "))
B = int(input("Введите второй год: "))
for years in range(A, B + 1):
    a = years % 10
    b = years // 10 % 10
    c = years // 100 % 10
    d = years // 1000
    if (a == b and a == c) or (a == d and a == c) or (b == c and b == d) or (d == b and d ==a):
        print(years)
