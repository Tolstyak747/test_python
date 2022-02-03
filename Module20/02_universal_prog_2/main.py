def is_prime(n):
    d = 2
    while d != n:
        reminder = n % d
        if reminder == 0:
            if d == n:
                return n
            else:
                return 0
        else:
            d += 1
    return n


ls = input("Элементы: ")
solve = []
for i, v in enumerate(ls):
    if i >= 2:
        if i == is_prime(i):
            solve.append(v)

print("Cписок: ", solve)

# Ok
