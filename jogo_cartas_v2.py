from typing import List, Tuple, Dict, Set

import random

SUITS = '♠ ♥ ♣ ♦'.split()
CARDS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARD = Tuple[str, str]
DECK = List[CARD]

# Observação: Em Python, as constantes são escritas
# em uppercase.

def create_deck(shuffle_deck: bool = False) -> DECK:
	"""Create a deck with fifty-two cards."""
	
	deck: DECK = [(suit, card) for card in CARDS for suit in SUITS]
	
	if shuffle_deck:
		random.shuffle(deck)
	
	return deck


print(CARDS)
print(SUITS)

print(create_deck())

print(30 * '-')


def distribute_cards(deck: DECK) -> Tuple[DECK, DECK, DECK, DECK]:
	"""Manages the hand of cards according to the generated deck."""
	return deck[0::4], deck[1::4], deck[2::4], deck[3::4]



deck = create_deck(shuffle_deck = True)
print(distribute_cards(deck))
print(30 * '-')


def play_cards() -> None:
	"""Start a 4-player card game."""
	cards: DECK = create_deck(shuffle_deck = True)
	players: List[str] = 'P1 P2 P3 P4'.split()
	hands: Dict['str', DECK] = {player: hand for player , hand
	         in zip(players, distribute_cards(cards))}
	
	for player, hand in hands.items():
		card_str: str = ' '.join(f"{suit}{card}" for (suit , card) in hand)
		print(f"{player}: {card_str}")


if __name__ == '__main__':
	play_cards()