import random

from card import Card

'''class Deck:
	def __init__(self):
		self.cards = []

	def generate(self):
		for suit in range(4):
			for rank in range(2, 15):
				self.cards.append(Card(rank, suit))

	def shuffle(self):
		random.shuffle(self.cards)

	def remove(self, card):
		if card in self.cards:
			self.cards.remove(card)

	def pop(self):
		return self.cards.pop()

	def is_empty(self):
		return not len(self.cards)

	def __str__(self):
		s = ""
		for i in range(len(self.cards)):
			s = s + " " * i + str(self.cards[i]) + "\n"
		return s'''

class Deck(list):
	def __init__(self):
		self.generate()

	def generate(self):
		if self.is_empty():
			for suit in range(4):
				for rank in range(2, 15):
					self.append(Card(rank, suit))

	def shuffle(self):
		random.shuffle(self)

	def is_empty(self):
		return not len(self)

	def deal(self, hands, num_cards=999):
		num_hands = len(hands)
		for i in range(num_cards):
			if self.is_empty():
				break
			# Deal one card to each person and repeat
			card = self.pop()
			hand = hands[i % num_hands]
			hand.append(card)

	def __str__(self):
		s = ""
		for i in range(len(self)):
			s = s + " " * i + str(self[i]) + "\n"
		return s

class Hand(Deck):
	def __init__(self, name):
		self.name = name
		
	def __str__(self):
		s = "Hand " + self.name
		if self.is_empty():
			s += " is empty\n"
		else:
			s += " contains\n"
		return s + Deck.__str__(self)

if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()
	hand = Hand("NerdyBread")
	hand2 = Hand("noah-wqq")
	deck.deal([hand, hand2], 10)
	print(hand)