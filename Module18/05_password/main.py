count = 0
count_num = 0
count_big = 0

while True:
    password = input("Придумайте пароль: ")
    for symbol in password:
        count += 1
    if count >= 8:
        for symb in password:
            if symb.isupper() == True:
                count_big += 1
        if count_big >= 1:
            for num in password:
                if num.isdigit() == True:
                    count_num += 1
            if count_num >= 3:
                print("Это надежный пароль!")
                break
            else:
                print("Пароль ненадёжный. Попробуйте ещё раз.")
        else:
            print("Пароль ненадёжный. Попробуйте ещё раз.")
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")


#зачет







