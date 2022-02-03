alphabet = "abcdefghijklmnopqrstuvwxyz"

file = open("text.txt", 'w')
file.write("Mama yla ramu.")
file.close()


def string(dict):
    string_d = ""
    for k, v in dict.items():
        string_d += k + " " + str(v)
        string_d += "\n"
    return string_d


def sort_dic(dictionaary):
    sort_val = sorted(dictionaary.values(), reverse=True)
    part = 1 / sum(sort_val)
    for k, v in dictionaary.items():
        dictionaary[k] = round(v * part, 3)
    sort_val = [round(x * part, 3) for x in sort_val]
    sorted_dic = {}
    for i in sort_val:
        for k, v in dictionaary.items():
            if dictionaary[k] == i:
                sorted_dic[k] = i

    return string(sorted_dic)



def dic(file):
    dicct = {}
    with open(file, "r") as f:
        ls = f.readlines()
    for line in ls:
        for letter in line.lower():
            if letter.isalpha():
                if letter in dicct:
                    dicct[letter] += 1
                else:
                    dicct[letter] = 1
    return sort_dic(dicct)



def analysis(input, output):
    with open(output, "w") as f:
        f.write(dic(input))


analysis("text.txt", "analysis.txt")
# Не смог отсортировать по алфавиту при равных значениях


# такой подход
import os

def run_path():
    return os.path.abspath('./')

def get_file_path(file_name):
    return os.path.join(run_path(), file_name)

def write_output(output_file_path, chars_freq):
    output_file_path = get_file_path(output_file_path)

    with open(output_file_path, 'w') as output_file:
        for char, freq in chars_freq:
            line = '{:s} {:.03f}\n'.format(char, freq)
            output_file.write(line)

def count_chars(chars_freq, file_name):
    file_path = get_file_path(file_name)

    with open(file_path, 'r') as input_file:
        for line in input_file.readlines():
            # Не уверен нужно ли считать символы в верхнем регистре
            for char in line.strip().lower():
                if char not in chars_freq:
                    chars_freq[char] = 0
                chars_freq[char] += 1

def get_char_freq(char_pair):
    return char_pair[1]

def main(input_filename, output_filename):
    chars_freq = dict()
    count_chars(chars_freq, input_filename)

    all_chars_qty = sum(chars_freq.values())
    chars_freq = {k:v/all_chars_qty for k,v in chars_freq.items()}
    chars_freq = sorted(chars_freq.items(), key=get_char_freq, reverse=True)

    write_output(output_filename, chars_freq)


main('text.txt', 'analysis.txt')

