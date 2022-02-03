length = 3
line_cnt = 0
with open("registrations.txt", "r", encoding="utf-8") as reg:
    with open('registrations_good.log', "w", encoding='utf-8') as good:
        with open('registrations_bad.log', "w", encoding='utf-8') as bad:
            for i_line in reg:
                line_cnt += 1
                ls = i_line.split()
                try:
                    if len(ls) != length:
                        raise IndexError
                except IndexError:
                    bad.write("На {} строке ошибка IndexError\n".format(line_cnt))
                else:
                    try:
                        if not ls[0].isalpha():
                            raise NameError
                    except NameError:
                        bad.write("На {} строке ошибка NameError\n".format(line_cnt))
                    else:
                        try:
                            if "@" not in ls[1] or "." not in ls[1]:
                                raise SyntaxError
                        except SyntaxError:
                            bad.write("На {} строке ошибка SyntaxError\n".format(line_cnt))
                        else:
                            try:
                                if not 10 <= int(ls[2]) <= 99:
                                    raise ValueError
                            except ValueError:
                                bad.write("На {} строке ошибка ValueError\n".format(line_cnt))
                            else:
                                good.write(" ".join(ls) + "\n")

# не очень хорошо всю логику держать в активных контекстных менеджерах. Лучше выполнить необходимую логику и уже открыть файлы.