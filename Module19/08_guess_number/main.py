n = int(input("Введите максимальное число: "))
n_ls = {x for x in range(1, n + 1)}

while True:
    print("Нужное число есть среди этих чисел: ", end="")
    numbers = input()
    if numbers != "Помогите!":
        numbers = numbers.split()
        numbers = [int(x) for x in numbers]
        numbers = set(numbers)
        print("Ответ Артёма: ", end="")
        artem_answer = input()
        if artem_answer == "Нет":
            n_ls = n_ls.difference(numbers)
            print()
        else:
            n_ls = n_ls.intersection(numbers)
            print()
    else:
        print("Артём мог загадать следующие числа: ", end="")
        for x in n_ls:
            print(x, end=" ")
        break

# делается лаконичней
max_number = int(input('Введите максимальное число: '))
all_nums = set(range(1, max_number + 1))
possible_nums = all_nums

while True:
    guess = input('Нужное число есть среди вот этих чисел:')
    if guess == 'Помогите!':
        break
    guess = {int(i_num) for i_num in guess.split()}
    answer = input('Ответ Артёма: ').lower()
    if answer == 'да':
        possible_nums &= guess
    else:
        possible_nums -= guess

print('Артём мог загадать следующие числа:', sorted(possible_nums))
