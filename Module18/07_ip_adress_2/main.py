ipadress= input("Введите IP: ").split('.')
count = 0
correct = 0
for symb in ipadress:
    count += 1
    if not symb.isdigit():
        print(symb, "- не целое число")
        correct += 1
    else:
        if not 0 <= int(symb) <= 255:
            print(symb, "не входит в диапазон от 0 до 255")
            correct += 1
if count != 4:
    print("Адрес - это четыре числа, разделенные точками")
    correct += 1
if correct == 0:
    print("IP-адрес корректен")


#зачет





