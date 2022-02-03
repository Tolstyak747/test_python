def list_file(file):
    with open(file, "r") as f:
        return f.read().splitlines()


def dic(lis):
    scores = {}
    for elem in lis:
        num = ""
        for symb in elem[-2::]:
            num += symb
        num = int(num)
        scores[elem[:-2:].strip()] = num
    return scores


def sort_dic(dictionary):
    new_dic = {}
    sorted_dictionary = {}
    sorted_ls = []
    for key, v in dictionary.items():
        if k < v:
            new_dic[key] = v
    sorted_val = sorted(new_dic.values(), reverse=True)
    for i in sorted_val:
        for key in new_dic:
            if new_dic[key] == i:
                sorted_dictionary[key] = i
    for key, v in sorted_dictionary.items():
        sorted_ls += [[key, str(v)]]

    return sorted_ls


def sec_file(file):
    with open(file, "w") as f:
        for x in range(len(final_list)):
            f.write("{}) {} {}\n".format(x + 1, final_list[x][0], final_list[x][1]))


first_file = open("first_tour.txt", "w")
first_file.write("80\n"
                 "Ivanov Serg 80\n"
                 "Segeev Petr 92\n"
                 "Petrov Vasiliy 98\n"
                 "Vasiliev Maxim 78\n")
first_file.close()

ls = list_file("first_tour.txt")
k = int(ls.pop(0))
dictionary = dic(ls)
final_list = sort_dic(dictionary)

sec_file("second_tour.txt")

# зачет
