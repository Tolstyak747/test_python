from collections import Counter

count = 9
scores = [
    ('69485 Jack'),
    ('95715 qwerty'),
    ('95715 Alex'),
    ('83647 M'),
    ('197128 qwerty'),
    ('95715 Jack'),
    ('93289 Alex'),
    ('95715 Alex'),
    ('95715 M'),
]

n = int(input('Сколько записей вносится в протокол? '))
score_board = dict()

if n < 3:
    print('Должно участвовать не менее трёх игроков')
else:
    for step in range(count):
        # score, name = input(f'{step + 1} запись: ').split()
        score, name = scores[step].split()
        if name not in score_board:
            score_board[name] = int(score)
        else:
            if score_board[name] < int(score):
                score_board[name] = int(score)

print()

if len(score_board) < 3:
    print('Необходимо иметь не менее трёх участников')
else:
    k = Counter(score_board)
    best_results = k.most_common(3)
    print('Итоги соревнований:')
    for i_res in range(3):
        print(f'{i_res + 1} {best_results[i_res][0]} {best_results[i_res][1]}')
#Вы используете методы, которые мы еще не проходили, поэтому я там и затроил, не знал как отсортировать, фром колекшнс импорт каунтер увидел вот впервые)

