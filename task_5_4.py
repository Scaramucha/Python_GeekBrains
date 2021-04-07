src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
sort_scr = [elem for elem in src if elem > src[src.index(elem) - 1] and src.index(elem) > 0]
print(sort_scr)
