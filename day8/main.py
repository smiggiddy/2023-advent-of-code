#!/usr/bin/env python


def navigation_counter(direction, data):
    count = 0
    direction_len = len(direction) - 1
    j = 0
    heading = "AAA"
    while heading != "ZZZ":
        if j == direction_len:
            i = direction[j]
            j = 0
        else:
            i = direction[j]
            j += 1

        if i == "R":
            heading = data[heading][1]
        else:
            heading = data[heading][0]
        count += 1
        print(heading)

        if heading == "ZZZ":
            return count


def load_file(file):
    """
    :returns file data by reading lines
    """

    with open(file) as f:
        data = f.readlines()

    directions = data[0].strip()

    data = {
        k: v.split(", ")
        for k, v in [
            line.strip().replace("(", "").replace(")", "").split(" = ")
            for line in data[1:]
            if line != "\n"
        ]
    }
    return directions, data


if __name__ == "__main__":
    directions, data = load_file("./input.txt")
    # directions,data = load_file("./test2.txt")
    print(navigation_counter(directions, data))
