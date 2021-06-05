class Card:
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
	ranks = [None, None, "2", "3", "4", "5", "6", "7", # Nones are placeholders so 2 = 2, 3 = 3 etc.
			 "8", "9", "10", "Jack", "Queen", "King", "Ace"] # Ace = 14

	def __init__(self, rank=0, suit=0):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return (self.ranks[self.rank] + " of " + self.suits[self.suit])

	def compare(self, other):
		if self.rank > other.rank: return 1
		if self.rank < other.rank: return -1
		# Tie
		return 0

	'''Overload relational operators to compare cards'''
	'''Card(14, 3) > Card(11, 1)'''
	def __eq__(self, other):
		return self.compare(other) == 0

	def __le__(self, other):
		return self.compare(other) <= 0

	def __ge__(self, other):
		return self.compare(other) >= 0

	def __gt__(self, other):
		return self.compare(other) > 0

	def __lt__(self, other):
		return self.compare(other) < 0

	def __ne__(self, other):
		return self.compare(other) != 0