rows = 4
cols = 3

ls = [list(range(x, x + rows * (cols - 1) + 1, rows)) for x in range(1, rows + 1)]
print(ls)

#зачет