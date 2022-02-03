message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
message_index = []
new_alphabet = []

for symb in message:
    if symb != " ":
        a = alphabet.index(symb) + shift
        if a > 32:
            reminder = a - 32
            reminder -= 1
            message_index.append(reminder)
        else:
            message_index.append(a)
    else:
        message_index.append(" ")

for num in message_index:
    if num != " ":
        new_alphabet.append(alphabet[num])
    else:
        new_alphabet.append(" ")

message = ""
for symb in new_alphabet:
    message += symb
print("Зашифрованное сообщение: ", message)


#можно попроще, используя генераторы списков
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33]
                  if sym != ' ' else ' ')
                 for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char

    return new_str


input_str = input('Введите строку: ')
shift = int(input('Введите сдвиг: '))
output_str = caesar_cipher(input_str, shift)

print('Зашифрованная строка:', output_str)

