special_symb = "@№$%^&*()"
name = input("Название файла: ")

for symb in special_symb:
    if name.startswith(symb):
        print("Ошибка: название начинается на один из специальных символов")
        break
    else:
        if name.endswith(".txt") or name.endswith(".docx"):
            print("Файл назван верно")
            break
        else:
            print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
            break

#зачет
