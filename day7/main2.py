#!/usr/bin/env python
from collections import Counter

class Camel:
    def __init__(self, data) -> None:
        self.data = data
        self.hands = []

        self.create_hand_obj()
        self.rank_hands()
        self.sort_hands()
        self.find_winnings()

    def sort_hand(self):
        return list(sorted(self.data.keys()))

    def create_hand_obj(self):
        for hand in self.data:
            self.hands.append(Hand(hand))

    def rank_hands(self):
        for hand in self.hands:
            hand.score_hand()

    def sort_hands(self):
        # self.ranked_hands = sorted(self.hands, key=lambda x: x.score_type, reverse=True)
        self.hands.sort()
        self.ranked_hands = sorted(self.hands, key=lambda x: x.score_type)
        # for h, o in zip(self.hands, self.ranked_hands):
        #     print(h.hand, h.score_type, o.hand, o.score_type)
        #     # print(Card(hand.hand[0]).ranking.index('A'))

    def find_winnings(self):
        winnings = 0
        for i, _ in enumerate(self.ranked_hands):
            hand_key = self.ranked_hands[i].hand
            winnings += int(self.data[hand_key]) * (i + 1)
        print(winnings)


class Hand:
    def __init__(self, hand) -> None:
        self.hand = hand
        self.score_type = 0

    def __iter__(self):
        yield from self.hand

    def __eq__(self, other) -> bool:
        return self.score_type == other.score_type

    def __lt__(self, other):
        for c, o in zip(self.hand, other.hand):
            c = Card(c)
            o = Card(o)
            if c == o:
                continue
            return c < o

    def score_hand(self):
        _hand = sorted(list(Counter(self.hand).values()))
        joker_count = Counter(self.hand).get('J')
        if joker_count and joker_count == 5:
                pass
        elif joker_count:
            _hand = list(self.hand)
            joker_count = Counter(_hand)['J']
            _hand = [x for x in _hand if x != 'J']
            new_hand = sorted(list(Counter(_hand).values()))
            new_hand[-1] += joker_count
            _hand = new_hand


        if _hand[-1] == 5:
            self.score_type = 7
            return
        if _hand[-1] == 4:
            self.score_type = 6
            return
        elif _hand[-1] == 3:
            if _hand[-2] == 2:
                self.score_type = 5
            else:
                self.score_type = 4
        elif _hand[-1] == 2:
            if _hand[-2] == 2:
                self.score_type = 3
            else:
                self.score_type = 2
        else:
            self.score_type = 1

        


class Card:
    def __init__(self, card) -> None:
        self.card = card
        self.rank = self.assign_rank()

    def assign_rank(self):
        ranking = ["J","2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
        return ranking.index(self.card)

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank


def load_file(file):
    """
    :returns file data by reading lines
    """

    with open(file) as f:
        data = f.readlines()

    data = {k: v for k, v in [line.strip().split() for line in data]}
    return data


if __name__ == "__main__":
    data = load_file("./input.txt")
    # data = load_file("./test_input.txt")
    c = Camel(data)
