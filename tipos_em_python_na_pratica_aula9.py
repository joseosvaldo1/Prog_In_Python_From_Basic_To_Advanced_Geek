"""
# Tipos de Dados em Python:
# Aula 9 - Tipos de Dados na Prática:

# -----------------------------------------------------

# Type hitings em conteiners:

# Em lista:
names: list = ['Geek', 'University']

# Em tuplas:
versions: tuple = (3, 4, 7)

# Em dicionários:
options: dict = {'air': True, 'leather_seat': True}

# Em conjuntos - set:
values: set = (3, 4, 5, 6)

print(names)            # => ['Geek', 'University']
print(versions)         # => (3, 4, 7)
print(options)          # => {'air': True, 'leather_seat': True}
print(values)           # => (3, 4, 5, 6)
print(__annotations__)  # => {'names': <class 'list'>, 'versions':
# <class 'tuple'>, 'options': <class 'dict'>, 'values': <class 'set'>}


# -----------------------------------------------------------------------

from typing import List, Dict, Tuple, Set

# Type hitings em conteiners:

# Em lista:
names: List[str] = ['Geek', 'University']

# Em tuplas:
versions: Tuple[int, int, int] = (3, 4, 7)

# Em dicionários:
options: Dict[str, bool] = {'air': True, 'leather_seat': True}

# Em conjuntos - set:
values: Set[int] = (3, 4, 5, 6)

print(names)            # => ['Geek', 'University']
print(versions)         # => (3, 4, 7)
print(options)          # => {'air': True, 'leather_seat': True}
print(values)           # => (3, 4, 5, 6)
print(__annotations__)  # => {'names': typing.List[str], 'versions':
# typing.Tuple[int, int, int], 'options': typing.Dict[str, bool],
# 'values': typing.Set[int]}


# ---------------------------------------------------------------------


# ---------------------------------------------------------------------

# Link com os códigos para os naipes das cartas do baralho:
https://www.alt-codes.net/suit-cards.php


Black Spade   =>      &#9824;
Black Heart   =>      &#9829;
Black Club    =>      &#9827;
Black Diamond =>      &#9830;

White Spade   =>      &#9828;
White Heart   =>      &#9825;
White Club    =>      &#9831;
White Diamond =>      &#9826;



"""

import random

SUITS = '♠ ♥ ♣ ♦'.split()
CARDS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def create_deck(shuffle_deck = False):
	"""Create a deck with fifty-two cards."""
	
	deck = [(suit, card) for card in CARDS for suit in SUITS]
	
	if shuffle_deck:
		random.shuffle(deck)
	
	return deck


print(CARDS)
print(SUITS)

print(create_deck())

print(30 * '-')


def distribute_cards(deck):
	"""Manages the hand of cards according to the generated deck."""
	return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


deck = create_deck(shuffle_deck=True)

print(distribute_cards(deck))

print(30 * '-')


def play_cards():
	"""Start a 4-player card game."""
	cards = create_deck(shuffle_deck = True)
	players = 'P1 P2 P3 P4'.split()
	hands = {player: hand for player, hand
	         in zip(players, distribute_cards(cards))}
	
	for player, hand in hands.items():
		card_str = ' '.join(f"{suit}{card}" for (suit, card) in hand)
		print(f"{player}: {card_str}")


if __name__ == '__main__':
	play_cards()




	
	





