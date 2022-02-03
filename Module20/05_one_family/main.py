database = {
    "Сидоров Павел": 29,
    "Антонов Денис": 10,
    "Сидорова Алина": 15,
    "Антонова Анжела": 40,
    "Сидоров Михаил": 44
}

surname = input("Введите фамилию: ").lower()
print()

for k, v in database.items():
    if surname in k.lower():
        print(k, v)

#зачет
