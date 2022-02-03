site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, deep):
    # global result
    if deep != 0:
        if key in struct:
            return struct[key]

        deep -= 1
        for substruct in struct.values():
            if isinstance(substruct, dict):
                result = find_key(substruct, key, deep)
                if result:
                    break

        return result
    else:
        return ("Увы, на этом уровне нет вашего ключа")

key = input("Ключ, который Вам нужен: ")
deep_search = int(input("Максимальная глубина поиска: "))

print(find_key(site, key, deep_search))


# Help! не могу дойти до третьего уровня в словаре body, выдает ошибку о локальной переменной