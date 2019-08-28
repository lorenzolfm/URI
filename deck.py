from random import shuffle

cards = []



class Card:
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f'{self.value} of {self.suit}'

class Deck:
	def __init__(self):
		suits = ["Hearts","Diamonds","Clubs","Spades"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(value, suit) for suit in suits for value in values]

	def __repr__(self):
		return f'Deck of {self.count()} cards'

	def count(self):
		return len(self.cards)

	def _deal(self,n):
		count = self.count()
		actual = min([count,num])
		if count == 0:
			raise ValueError('All cards have been dealt')
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	def suffle(self):
		if len(self.cards) != 52:
			raise ValueError('Only full decks can be shuffled')
		return random.shuffle(self.cards)

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, num):
		return self._deal(num)


c = Card('Hearts','2')
d = Deck(cards)
print(d.__repr__())
print(d.count())
print(c)