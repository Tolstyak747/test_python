string1 = input("Первая строка: ")
string2 = input("Вторая строка: ")

count = 0
a = string2 * 2
for symb in a:
    count += 1
    if symb == string1[0]:
        break

if string1 in a:
    print("Первая строка получается из второй со сдвигом ", count - 1)
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

#зачет
