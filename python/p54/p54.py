# http://projecteuler.net/problem=54

from functools import total_ordering
from collections import Counter

@total_ordering
class Card(object):
    def __init__(self, string):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

def sort_cards_by_count(card_counter):
    comparer = lambda card: (card_counter.get(card), card)
    return sorted(card_counter, key=comparer, reverse=True)

def score_royal_flush(cards):
    if has_straight_flush(cards) and cards[0].value == 12:
        return (10, cards)

def score_straight_flush(cards):
    if has_straight(cards) and has_flush(cards):
        return (9, cards)

def score_full_house(cards):
    card_counter = Counter(card.value for card in cards)
    counts = card_counter.values()
    if 2 in counts and 3 in counts:
        return (7, sort_cards_by_count(card_counter))

def score_flush(cards):
    cards.sort(reverse=True)
    if len(set(card.suit for card in cards)) == 1:
        return (6, cards)

def score_straight(cards):
    cards.sort(reverse=True)
    if range(cards[0].value, cards[-1].value - 1, -1) == [card.value for card in cards]:
        return (5, cards)

def score_two_pair(cards):
    card_counter = Counter(card.value for card in cards)
    if [1, 2, 2] == sorted(card_counter.values()):
        return (3, sort_cards_by_count(card_counter))

def score_n_of_a_kind(cards):
    card_counter = Counter(card.value for card in cards)
    card_counts = card_counter.values()
    sorted_cards = sort_cards_by_count(card_counter)

    if 4 in card_counts:
        return (8, sorted_cards)
    elif 3 in card_counts:
        return (4, sorted_cards)
    elif 2 in card_
        return (2, sorted_cards)
    else
        return (1, sorted_cards)

def score_hand(cards):
    scoring = [score_royal_flush, score_straight_flush, score_full_house, \
               score_flush, score_straight, score_two_pair, score_n_of_a_kind]

    for method in scoring:
        score = method(cards)
        if score:
            return score

