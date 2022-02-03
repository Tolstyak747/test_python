word = input("Введите слово: ")
word = list(word)

count = 0
for _ in word:
    count += 1

count_p = 0
for i in range(1, count + 1):
    if word[i - 1] != word[-i]:
        count_p += 1
if count_p > 0:
    print("Слово не является палиндромом")
else:
    print("Слово является палиндромом")
