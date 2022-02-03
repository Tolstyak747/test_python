import zipfile
import os
import pathlib

def sort_dic(dicct):
    s_d = {}
    sorted_val = sorted(dicct.values())
    for i in sorted_val:
        for k, v in dicct.items():
            if dicct[k] == i:
                s_d[k] = i
    return s_d


def write_to_file(file, dic):
    with open(file, "w", encoding="utf-8") as f:
        for k, v in dic.items():
            f.write(k + "-" + str(v) + "\n")

alphabet_rus = "абвгдеёжзийклмнопрстуфхцыъьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЫЪЬЭЮЯ"
alphabet_lat = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp_rus = []
alp_lat = []

dic_lat = {}
dic_rus = {}

path_to_zip = os.path.abspath("voyna-i-mir.zip")
print(path_to_zip)
with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
    zip_ref.extractall(pathlib.Path.cwd())

voina = open("voyna-i-mir.txt", "r", encoding="utf-8")
for line in voina:
    for word in line:
        for letter in word:
            if letter in alphabet_rus:
                if letter in dic_rus:
                    dic_rus[letter] += 1
                else:
                    dic_rus[letter] = 1
            elif letter in alphabet_lat:
                if letter in dic_lat:
                    dic_lat[letter] += 1
                else:
                    dic_lat[letter] = 1

rus = sort_dic(dic_rus)
lat = sort_dic(dic_lat)
write_to_file("lat.txt", lat)
write_to_file("rus.txt", rus)

