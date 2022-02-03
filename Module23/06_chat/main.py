name = input("Введите имя: ")
while True:
    try:
        answer = int(input("1. Посмотреть текущий текст чата\n"
                           "2. Отправить сообщение\n"
                           "Ответ: "))
    except ValueError:
        print("Хватит вводить непонятные символы!")
    else:
        if answer == 1:
            try:
                with open("Chat.txt", "r") as chat:
                    for i_line in chat:
                        print("{}".format(i_line))
            except FileNotFoundError:
                print("Чат еще пуст!")
        elif answer == 2:
            with open("Chat.txt", "a") as chat:
                message = input("Введите сообщение: ")
                chat.write("{}: {}\n".format(name, message))
        else:
            print("Введите еще раз!")
    print()

# зачет
