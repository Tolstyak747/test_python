films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

films = list(films)
favorite = []
count = 0


your_film = 0
while your_film != "end":
    your_film = input("Введите фильм: ")
    if your_film == "end":
        break
    elif your_film in favorite:
        print("Фильм уже есть в вашем списке")
    else:
        if your_film in films:
            favorite.append(your_film)
        else:
            print("Ошибка")

print("Список любимых фильмов, на которые есть рецензии: ", favorite)
#зачет
