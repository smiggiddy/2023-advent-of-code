#!/usr/bin/env python
import re


def is_part_number(item, string, count):
    """Tests if a symbol is next to the item"""

    is_part = False

    min_index = max(item.span()[0] - 1, 0)
    max_index = min(item.span()[1] + 1, len(string) - 1)
    y_min_index = max(count -1 , 0)
    y_max_index = min(count + 1, len(test_data) - 1)


    for i in range (min_index, max_index):
        if (
            string[i]
            and not string[i].isalnum()
            and string[i] != "."
        ):
            is_part = True

    for i in range(min_index, max_index):
        if (
            not test_data[y_min_index][i].isalnum()
            and test_data[y_min_index][i] != "."
            or
            not test_data[y_max_index][i].isalnum()
            and test_data[y_max_index][i] != "."

        ):
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

print(sum(word_list))



# print(f"WORD {word.group(0)}: {result}")

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
