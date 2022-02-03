s = tuple(input("Введите кортеж: "))
elem = input("Введите элемент: ")
new_s = ()
start_stop = []

if elem not in s:
    print(new_s)
elif s.count(elem) == 1:
   start = s.index(elem)
   new_s = s[start:]
   print(new_s)
elif s.count(elem) == 2:
    for i, v in enumerate(s):
        if v == elem:
            start_stop.append(i)
    new_s = s[start_stop[0]:start_stop[1] + 1]
    print(new_s)


#зачет
