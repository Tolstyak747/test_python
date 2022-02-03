text = input("Введите текст: ")
# vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"] 
vowels = 'ауоыиэяюёе' #строка - тоже итерируемый объект
text_vow = [elem for elem in text if elem in vowels]
# for i in text:
#     if i in vowels:
#         text_vow.append(i)

print("Список гласных букв: ", text_vow)
print("Длина списка: ", len(text_vow))

#зачет
