contacts = {
    "Иванов Антон": 800,
    "Смирнов Денис": 500,
    "Котова Анна": 300
}

while True:
    print("Добавить контакт или найти человека в списке: ", end="")
    answer = input().lower()
    if answer == "добавить":
        name = input("Введите Фамилию и Имя: ")
        numbers = int(input("Введите номер телефона: "))
        if name in contacts:
            print("Такой контакт уже есть!")
        else:
            contacts[name] = numbers
            for i_name in contacts:
                print(i_name, contacts[i_name])
    elif answer == "найти":
        surname = input("Введите Фамилию: ").lower()
        for i_name in contacts:
            if surname in i_name.lower():
                print(i_name, contacts[i_name])
    print()

#зачет
