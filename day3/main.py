#!/usr/bin/env python
import re


def is_part_number(item, string, count):
    """Tests if a symbol is next to the item"""

    is_part = False

    get_index = item.span()[0]
    if get_index == 0:
        min_index = get_index
    else:
        min_index = get_index - 1

    if item.span()[1] == len(string):
        max_index = item.span()[1]
    else:
        max_index = item.span()[1] + 1

    if count == 0:
        y_min_index = count
    else:
        y_min_index = count - 1

    if count == len(test_data) - 1:
        y_max_index = len(test_data) - 1
    else:
        y_max_index = count + 1

    for i in range(min_index, max_index):
        print(i)
        if string[i] and not string[i].isalnum() and string[i] != ".":
            is_part = True

    for i in range(min_index, max_index):
        if not test_data[y_min_index][i].isalnum() and test_data[y_min_index][i] != ".":
            is_part = True

    for i in range(min_index, max_index):
        if not test_data[y_max_index][i].isalnum() and test_data[y_max_index][i] != ".":
            is_part = True

    return is_part


data = ...

with open("./input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

test_data = data

pattern = r"[\d]+"

list_len = len(test_data)
string_len = len(test_data[0])
word_list = []

print(f"LIST LENGTH: {list_len}\nSTRING LEN:{string_len}")

for count, string in enumerate(test_data):
    match = re.finditer(pattern, test_data[count])
    if match:
        for word in match:
            result = is_part_number(word, test_data[count], count)
            if result:
                word_list.append(int(word.group(0)))
                print(f"WORD {word.group(0)}: {result}")

print(sum(word_list))

# match = re.findall(pattern, test_data[count])
# for m in match_2:
#     print(m.group(0))
#     print(m.span())

# test_input = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """

# test_data = [line for line in test_input.split()]
# test_data = [line for line in test_input]
