site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def uniq_site(struct, name):
    if "title" in struct:
        struct["title"] = "Куплю/продам {} недорого".format(name)
    if "h2" in struct:
        struct["h2"] = 'У нас самая низкая цена на {}'.format(name)


    for substruct in struct.values():
        if isinstance(substruct, dict):
            uniq_site(substruct, name)

    return struct

amount = int(input("Кол-во сайтов: "))
for n in range(amount):
    name_phone = input("Название телефона: ")
    print("Сайт для {}: ".format(name_phone))
    print(uniq_site(site, name_phone))

# зачет
