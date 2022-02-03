import random


class Cards:
    ls = {"двойка": 2,
          "тройка": 3,
          "четверка": 4,
          "пятерка": 5,
          "шестерка": 6,
          "семерка": 7,
          "восьмерка": 8,
          "девятка": 9,
          "десятка": 10,
          "валет": 10,
          "дама": 10,
          "король": 10,
          "туз": 11}

    def random_card(self):
        key = random.choice(list(self.ls.keys()))
        for k, v in self.ls.items():
            if key == k:
                return k, v


class Player:
    summ = 0

    def start(self, cards):
        k, v = Cards.random_card(cards)
        if k == "туз" and self.summ > 21:
            self.summ += 1
        self.summ += v
        print(f"Ваша карта:{k}")

    def info(self):
        print(f"Сумма Ваших карт: {self.summ}")


class Dealer:
    sumD = 0

    def start(self, cards):
        k, v = Cards.random_card(cards)
        self.sumD += v

    def info(self):
        print(f"Сумма карт дилера: {self.sumD}")


def play(player, dealer, cards):
    for _ in range(2):
        player.start(cards)
        dealer.start(cards)
    player.info()
    print()

    while True:
        answer = input("Взять еще карту или остановиться? y/n ")
        if answer.lower() == "n":
            dealer.info()
            if 21 >= player.summ > dealer.sumD:
                print("Вы выиграли!")
            elif (player.summ < dealer.sumD <= 21) or (player.summ > 21):
                print("Вы проиграли!")
            else:
                print("Ничья!")
            break
        elif answer.lower() == "y":
            player.start(cards)
            player.info()
            print()


c = Cards()
p = Player()
d = Dealer()

play(p, d, c)
