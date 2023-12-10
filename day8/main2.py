#!/usr/bin/env python

from math import lcm
import re

def get_headings(data):
    headings = []
    for key in data.keys():
        match = re.search(r'..A', key)
        if match:
            headings.append(match.group())

    return headings

def check_last_heading(head):
    match = re.search(r'..Z', head)
    if match:
        headings.append(match.group())

    return match != None




def navigation_counter(direction, data, headings):
    count = 0
    count_list = []
    direction_len = len(direction) - 1 
    j = 0 
    last_heading = [head for head in headings]
    run_loop = True
    
    while run_loop:


        if j == direction_len:
            i = direction[j] 
            j = 0 
        else:
            i = direction[j]
            j += 1

        all_counts = check_last_heading(last_heading)
        if all_counts:
            count_list.append(count)
        elif len(count_list) == len(headings):
            break

        for h in range(len(headings)):

            if i == 'R':
                last_heading[h] = data[last_heading[h]][1] 
            else:
                last_heading[h] = data[last_heading[h]][0]
        count += 1

    print(lcm(*count_list))



    


def load_file(file):
    """
    :returns file data by reading lines
    """

    with open(file) as f:
        data = f.readlines()

    directions = data[0].strip()

    data = {k: v.split(", ") for k,v in [line.strip().replace('(', '').replace(')','').split(" = ") for line in data[1:] if line != '\n']}
    return directions, data


if __name__ == "__main__":
    # directions, data = load_file("./input.txt")
    directions,data = load_file("./test3.txt")
    headings = get_headings(data)
    print(navigation_counter(directions, data, headings))
