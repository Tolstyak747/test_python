import os


direct = os.path.abspath('..')
amount = os.listdir(direct)
size_direct = 0
amount_files = 0


print(len(amount))

for i_elem in os.listdir(direct):
    path_to_files = os.path.abspath(os.path.join(direct, i_elem))
    for files in os.listdir(path_to_files):
        amount_files += 1
        size_direct += os.path.getsize(os.path.join(path_to_files, files))

print("Размер каталога (в Кб): ", round(size_direct / 1024, 2))
print("Количество подкаталогов: ", len(amount))
print("Количество файлов: ", amount_files)

# зачет
