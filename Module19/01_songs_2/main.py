violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

how_much = int(input("Сколько песен? "))
sum = 0
for n in range(how_much):
    print("Название {} песни: ".format(n + 1), end="")
    name = input()
    sum += violator_songs[name]

print('Общее время звучания песен: ', round(sum, 2))

#зачет
