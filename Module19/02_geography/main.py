amount = int(input("Кол-во стран: "))
country = dict()

for n in range(amount):
    print(n + 1, "страна: ", end="")
    data = input().split()
    country[n] = data
print(country)

count = 0
for n in range(3):
    print(n + 1, "город: ", end="")
    town = input()
    for num in range(amount):
        if town in country[num]:
            count += 1
            a = num

    if count > 0:
        print("Город {} расположен в стране {}".format(town, country[a][0]))
        count -= count

    else:
        print("По городу {} данных нет.".format(town))

#зачет
