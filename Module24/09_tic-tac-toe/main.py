class Player1:
    ls = []

    def __init__(self, name):
        self.name = name
        self.krestik = "X"

    def append(self, n):
        self.ls.append(n)


class Player2:
    ls = []

    def __init__(self, name):
        self.name = name
        self.nul = "0"

    def append(self, n):
        self.ls.append(n)


def check_win(list):
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
    for elem in win:
        cnt = 0
        for symb in list:
            if symb in elem:
                cnt += 1
        if cnt == 3:
            return True


def lets_go(player):
    try:
        choice = int(input(f"{player.name}, ваш ход! Куда поставим? "))
        if choice in pole:
            pole.remove(choice)
            player.append(choice)
        else:
            print("Там уже занято. Повторите ваш выбор.")
            print()
            return lets_go(player)
    except ValueError:
        print("Введите число от 1 до 9!")
        print()
        return lets_go(player)


def play(player_1, player_2):
    for i in range(5):
        if i >= 2:
            lets_go(player_1)
            if check_win(p1.ls):
                print(f"Вы выиграли, {player_1.name}")
                return 1
            if i == 4:
                return 0
            else:
                lets_go(player_2)
                if check_win(player_2.ls):
                    print(f"Вы выиграли, {player_2.name}")
                    return 1
        else:
            lets_go(player_1)
            lets_go(player_2)


board = range(1, 10)
for i in range(3):
    print("-" * 13)
    print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
print("-" * 13)

p1 = Player1("Сергей")
p2 = Player2("Алена")
pole = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if play(p1, p2) == 0:
    print("Ничья!")

#Всё работает, но графически не понимаю как выстроить.
