with open("people.txt", "w") as people_file:
    people_file.write("Andrey\n"
                      "Ivan\n"
                      "Ac\n"
                      "Maksim\n")

i_line_cnt = 0
length = 0
summ = 0
try:
    people_file = open("people.txt", "r")
    for i_line in people_file:
        i_line_cnt += 1
        for word in i_line:
            if word.isalpha():
                length += 1
        if length < 3:
            raise BaseException
        else:
            summ += length
            length = 0

except BaseException:
    with open("errors.log", "w", encoding="utf-8") as error:
        error.write("Ошибка в {} строке, длина строки должна быть больше 3х!".format(i_line_cnt))
else:
    print("Общая сумма: ", summ)
finally:
    people_file.close()
    print(people_file.closed)

# зачет
