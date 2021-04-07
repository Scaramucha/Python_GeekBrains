src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
sorted_str = [element for element in src if src.count(element) == 1]
print(sorted_str)

src_dooble = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_number = set()
repeat_number = set()
for element in src_dooble:
    if element not in repeat_number:
        unique_number.add(element)
    else:
        unique_number.discard(element)
    repeat_number.add(element)
sorted_src_dooble = [element for element in src_dooble if element in unique_number]
print(sorted_src_dooble)
