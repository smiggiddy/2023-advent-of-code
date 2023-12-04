#!/usr/bin/env python
import re

def load_file(file):
    """
    :returns file data by reading lines
    """

    with open(file) as f:
        data = f.readlines()

    data = [line.strip() for line in data]

    return data 

def format_data(data):
    # returns list of dicts object from data 
    lines = [] 

    pattern = r'([Card\w].*):([\d ]*)\|([\d ]*)'
    
    for line in data:
        m = re.search(pattern, line)
        lines.append(
                {
                    'card': m.group(1).strip(),
                    'winning_numbers': m.group(2).strip().split(),
                    'all_numbers': m.group(3).strip().split(),
                    'total_cards': 1
                 }
                )
    return lines

def find_winners(cards):
    total_points = 0
    
    for card in cards:
        print(card)
        count = 0
        for winner in card['winning_numbers']:
            if winner in card['all_numbers']:
                if(count == 0):
                    count = 1
                else:
                    count += count
                print("winners ",winner)
        total_points += count
        print(count)

    print(total_points)


def winning_cards(cards):
    for i in range(len(cards)):
        for _ in range(cards[i]['total_cards']):
            count = 0
            for winner in cards[i]['winning_numbers']:
                if winner in cards[i]['all_numbers']:
                    count += 1
           
            for c in range(1, count+1):
                cards[i+c]['total_cards'] += 1
    sum_cards = [x['total_cards'] for x in cards]

    print(sum(sum_cards))


if __name__ == '__main__':
    data = load_file("./input.txt")
    lines = format_data(data)
    # find_winners(lines)
    winning_cards(lines)
