def list_file(file):
    with open(file, "r") as f:
        return f.readlines()


def cip_letter(symb, n):
    alphabet = "abcdefghijklmnopqrstuvwxwyz"
    a = (alphabet.index(symb) + n)
    return alphabet[a]


def write_f(file, text):
    with open(file, "w") as f:
        f.write(text)

def cipher(input_file, output_file):
    new_cipher = []
    am_word = 0
    for word in list_file(input_file):
        am_word += 1
        for letter in word.lower():
            if letter not in "\n":
                new_cipher.append(cip_letter(letter, am_word))
            else:
                new_cipher.append("\n")
    new_cipher = "".join(new_cipher)
    write_f(output_file, new_cipher)

cipher("text.txt", "cipher_text.txt")

# зачет
