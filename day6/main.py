#!/usr/bin/env python

from math import prod


def load_file(file):
    """
    :returns file data by reading lines
    """

    with open(file) as f:
        data = f.readlines()

    data = [
        {"type": line.strip().split()[0], "data": "".join(line.strip(" ").split()[1:])}
        for line in data
    ]
    print(data)
    return data


def distance_traveled(data):
    time = data[0]["data"]
    distance = data[1]["data"]
    winnables = []

    # for i in range(len(time)):
    #     print(time[i])
    possible_outcomes = list(
        map(
            lambda x: x[0] * x[1],
            [item for item in zip(range(0, int(time)), range(int(time), 0, -1))],
        )
    )
    winnables.append(len([race for race in possible_outcomes if race > int(distance)]))

    return prod(winnables)


if __name__ == "__main__":
    data = load_file("./input.txt")
    # data = load_file("./test_input.txt")

    print(distance_traveled(data))
