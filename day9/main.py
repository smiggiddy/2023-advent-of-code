#!/usr/bin/env python

def load_file(file):
    """
    :returns file data by reading lines
    """

    with open(file) as f:
        data = f.readlines()
        data = [line.strip() for line in data]

    return data

def get_next_num(arr):
    new_arr = []
    for i, _ in enumerate(arr):
        if (i < len(arr)-1):
            new_arr.append((int(arr[i+1]) - int(arr[i])))
            print(new_arr)
        if not all(x == new_arr[0] for x in new_arr) and len(new_arr) == len(arr) - 1:
            return (get_next_num(new_arr) + int(arr[-1]))

    return new_arr[-1] + int(arr[-1])

def get_first_num(arr):
    new_arr = []
    # print(arr, "<- arr at the top")
    for i, _ in enumerate(arr):
        if (i < len(arr)-1):
            new_arr.append((int(arr[i+1]) - int(arr[i])))
        if not all(x == 0 for x in new_arr) and len(new_arr) == len(arr) - 1:
            print(new_arr)
            arr.insert(0, int(arr[0]) - get_first_num(new_arr))

    arr.insert(0, (int(arr[0])-new_arr[0]))
    return int(arr[0]) + new_arr[0]


def sum_nums(data):

    nums = []

    for line in data:
        num = get_first_num((line.split()))
        print(num)
        nums.append(num)

    print(sum(nums))

        



if __name__ == "__main__":
    data = load_file("./input.txt")
    # data = load_file("./test_input.txt")
    sum_nums(data)
